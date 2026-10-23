#!/usr/bin/env bash
#
# Daily refresh of the Football Charts dataset (raw -> Postgres -> analysis -> dashboard).
#
#   1. collect_all_leagues.py --active-only --overwrite   results + tables for live seasons
#   2. fetch_fixtures.py --overwrite                     upcoming fixtures + model_predictions
#   3. validate_raw_data.py  (one league per run)        raw-data findings
#   4. build_all_leagues.py                              Postgres rebuild + analysis, all leagues
#   5. build_dashboard.py                                all-league HTML dashboard
#
# Driven by the "FootballDataRefresh" Windows scheduled task (install_task.ps1),
# which wakes this distro through wsl.exe. Also runnable by hand:
#
#   bash scripts/refresh_data.sh [--dry-run] [--force]
#
# Design notes:
#   * Uses the system python3. The repo's venv/ is a Windows venv (venv/Scripts,
#     no venv/bin) and cannot be used from WSL.
#   * Once per calendar day: a stamp file records the date of the last run in which
#     every stage succeeded, so a second trigger the same day is a cheap no-op.
#     --force ignores the stamp. Failed runs never stamp.
#   * Fail-soft between stages: a failing stage is logged and skipped so one bad
#     league cannot abort the sweep. Only preflight failures are fatal.
#   * Never invokes git. The working tree is left dirty for human review.
#
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

PYTHON="${PYTHON:-python3}"
CATALOG="data/raw/league_teams.json"
LOG_DIR="logs"
LOG_FILE="$LOG_DIR/refresh_$(date +%Y%m%d).log"
LATEST_LINK="$LOG_DIR/refresh_latest.log"
LOCK_FILE="$LOG_DIR/.refresh.lock"
STAMP_FILE="$LOG_DIR/.last_success_date"
BASELINE_FILE="$LOG_DIR/.validation_baseline.json"
VALIDATION_DIR="data/validation"
BY_LEAGUE="$VALIDATION_DIR/by-league"
CANONICAL_REPORT="$VALIDATION_DIR/poc_validation_report.json"

DRY_RUN=0
FORCE=0

while [ $# -gt 0 ]; do
    case "$1" in
        --dry-run) DRY_RUN=1 ;;
        --force)   FORCE=1 ;;
        -h|--help) sed -n '3,26p' "${BASH_SOURCE[0]}" | sed 's/^#\{1,2\} \{0,1\}//'; exit 0 ;;
        *) echo "unknown argument: $1" >&2; exit 2 ;;
    esac
    shift
done

mkdir -p "$LOG_DIR"
ln -sfn "$(basename "$LOG_FILE")" "$LATEST_LINK"

# Mirror everything to the terminal and the log. tee is a background child, so
# it must be drained before the script exits: WSL tears down the session when
# wsl.exe returns and kills tee mid-flush, which silently dropped the final
# summary lines (seen on 2026-10-04 and 2026-10-13). Closing our write end in
# the EXIT trap lets tee see EOF, and waiting on it guarantees a complete log.
exec > >(tee -a "$LOG_FILE") 2>&1
TEE_PID=$!
drain_log() { exec 1>&- 2>&-; wait "$TEE_PID" 2>/dev/null || true; }
trap drain_log EXIT

say()  { printf '%s\n' "$*"; }
rule() { say "------------------------------------------------------------"; }

# Single-instance lock. The task already sets MultipleInstancesPolicy=IgnoreNew,
# but that only suppresses runs that overlap; this covers everything else.
exec 9>"$LOCK_FILE"
if ! flock -n 9; then
    say "$(date -Is) another refresh run holds $LOCK_FILE; exiting."
    exit 0
fi

say "============================================================"
say "refresh_data.sh start ($(date -Is))"
say "root=$ROOT_DIR python=$PYTHON dry_run=$DRY_RUN force=$FORCE"
rule

today="$(date +%F)"
if [ -f "$STAMP_FILE" ]; then
    last="$(cat "$STAMP_FILE" 2>/dev/null || true)"
    # The stamp is always reported so --dry-run can show whether the next real
    # run would be skipped, but it is only enforced outside a dry run.
    if [ "$last" = "$today" ]; then
        if [ "$DRY_RUN" -eq 1 ]; then
            say "$(date -Is) stamp: a successful refresh already ran today ($today)."
            say "  -> the next real run would SKIP (use --force to override)."
        elif [ "$FORCE" -eq 0 ]; then
            say "$(date -Is) a successful refresh already ran today ($today); skipping."
            say "Re-run with --force to refresh again."
            exit 0
        fi
    else
        say "$(date -Is) stamp: last successful refresh was ${last:-unknown}; next run will proceed."
    fi
else
    say "$(date -Is) stamp: none yet; the next run will proceed."
fi

# ---------------------------------------------------------------- preflight
fail=0
command -v "$PYTHON" >/dev/null 2>&1 || { say "FATAL: '$PYTHON' not on PATH."; fail=1; }

if [ -f .env ]; then
    for key in FOOTBALL_CHARTS_API_KEY DATABASE_URL; do
        [ -n "$(grep -E "^${key}=" .env | head -1 | cut -d= -f2- || true)" ] \
            || { say "FATAL: .env has no value for $key"; fail=1; }
    done
else
    say "FATAL: no .env at $ROOT_DIR/.env"; fail=1
fi

if [ -f "$CATALOG" ]; then
    league_count="$("$PYTHON" -c "import json,sys
try:
    c=json.load(open(sys.argv[1])); print(sum(1 for m in c.values() if int(m.get('teams',0))>0))
except Exception: print(0)" "$CATALOG" 2>/dev/null || echo 0)"
    say "catalog: ${league_count:-0} league(s) with team data"
    [ "${league_count:-0}" -gt 0 ] || { say "FATAL: $CATALOG yielded no leagues."; fail=1; }

    # Season-rollover check. collect_all_leagues.py resolves seasons from the
    # catalog plus whatever is already on disk, then falls back to the newest
    # one when none is in progress (collect_all_leagues.py:85-88). So once a
    # league's seasons all close and the next one is not yet declared, the job
    # keeps re-fetching a finished season and silently goes stale. The catalog
    # is only rewritten by build_league_config.py, which is not part of this
    # pipeline, so this is the one thing a human has to do at each rollover.
    # Purely local: no API calls.
    stale="$("$PYTHON" -c "import json,sys
from datetime import date
sys.path.insert(0,'backend/scripts')
try:
    from db_common import is_season_active
except Exception:
    sys.exit(0)
today=date.today()
cat=json.load(open(sys.argv[1]))
out=[lg for lg,m in cat.items()
     if (list(m.get('seasons') or [])) and not any(is_season_active(s,today) for s in m['seasons'])]
print(' '.join(sorted(out)))" "$CATALOG" 2>/dev/null || true)"
    if [ -n "$stale" ]; then
        say "WARN: no in-progress season declared for: $stale"
        say "      These will keep refreshing a finished season. Run once:"
        say "        python3 backend/scripts/build_league_config.py"
    fi
else
    say "FATAL: no league catalog at $CATALOG (run build_league_config.py)"; fail=1
fi

if [ "$DRY_RUN" -eq 0 ]; then
    if command -v pg_isready >/dev/null 2>&1; then
        if pg_isready -q; then say "postgres: ready"
        else say "FATAL: PostgreSQL is not accepting connections."; pg_isready || true; fail=1; fi
    else
        say "WARN: pg_isready not found; skipping the database preflight."
    fi
fi

if [ "$fail" -ne 0 ]; then
    say "Preflight failed; no stages were run."
    exit 1
fi
say "preflight ok"
rule

# ------------------------------------------------------------- stage runner
STAGE_NAMES=(); STAGE_RESULTS=(); STAGE_SECONDS=()

run_stage() {
    local name="$1"; shift
    rule
    say "[$(date -Is)] stage: $name"
    say "  \$ $*"
    local t0 t1 code
    t0="$(date +%s)"
    if [ "$DRY_RUN" -eq 1 ]; then
        code=0
    else
        set +e; "$@"; code=$?; set -e
    fi
    t1="$(date +%s)"
    STAGE_NAMES+=("$name"); STAGE_SECONDS+=("$((t1 - t0))")
    if [ "$code" -eq 0 ]; then
        STAGE_RESULTS+=("ok"); say "  [ok] $name ($((t1 - t0))s)"
    else
        STAGE_RESULTS+=("failed(exit $code)"); say "  [FAILED exit $code] $name ($((t1 - t0))s)"
    fi
}

# ------------------------------------------------------------------- stage 1
run_stage "collect raw (active seasons)" \
    "$PYTHON" backend/scripts/collect_all_leagues.py --active-only --overwrite

# ------------------------------------------------------------------- stage 2
run_stage "fetch fixtures" \
    "$PYTHON" backend/scripts/fetch_fixtures.py --overwrite

# ------------------------------------------------------------------- stage 3
# validate_raw_data.py takes a single --league and always writes to the same
# hardcoded report path (validate_raw_data.py:50-51), so a loop over leagues
# would leave only the last report behind. Run one league at a time and archive
# each report under by-league/ before the next run overwrites it.
#
# Its default seasons are the hardcoded European run 2020-2021..2025-2026
# (collect_raw_data.py:50-57), but the dataset is heterogeneous: premier uses
# 2020-2021..2026-2027 while brazil1 uses calendar seasons 2025 and 2026.
# Validating the defaults would report six seasons that do not exist as
# FILE_MISSING and never look at the real data, so seasons are discovered from
# disk instead.
validate_all_leagues() {
    mkdir -p "$BY_LEAGUE"
    local tally; tally="$(mktemp)"
    : > "$tally"
    local league s args seasons
    while read -r league; do
        [ -n "$league" ] || continue
        mapfile -t seasons < <("$PYTHON" -c "import os,re,sys
try: print('\\n'.join(sorted(x for x in os.listdir(sys.argv[1]) if re.fullmatch(r'(19|20)[0-9]{2}(-[0-9]{4})?', x))))
except Exception: pass" "data/raw/$league" 2>/dev/null || true)
        if [ "${#seasons[@]}" -eq 0 ]; then
            say "  $league: no season directories under data/raw/$league; skipping"
            printf '%s 0 0\n' "$league" >> "$tally"
            continue
        fi
        args=(); for s in "${seasons[@]}"; do args+=(--season "$s"); done
        say "  $league: ${seasons[*]}"
        set +e
        "$PYTHON" backend/scripts/validate_raw_data.py --league "$league" "${args[@]}" >/dev/null 2>&1
        vcode=$?
        set -e
        # Archive the report only when the validator exited 0 AND the report it
        # wrote is actually scoped to this league. The report path is hardcoded,
        # so a crashed or failed run would otherwise leave the previous league's
        # report in place and silently mislabel it under this league's name,
        # poisoning the baseline and hiding a real regression.
        if [ "$vcode" -eq 0 ] && [ -f "$CANONICAL_REPORT" ] && "$PYTHON" -c "import json,sys
try: sys.exit(0 if json.load(open(sys.argv[1])).get('scope',{}).get('league')==sys.argv[2] else 1)
except Exception: sys.exit(1)" "$CANONICAL_REPORT" "$league"; then
            cp -f "$CANONICAL_REPORT" "$BY_LEAGUE/$league.json"
            "$PYTHON" -c "import json,sys
try:
    o=json.load(open(sys.argv[1])).get('overall',{})
    print('%s %s %s' % (sys.argv[2], o.get('errors',0), o.get('warnings',0)))
except Exception: print('%s - -' % sys.argv[2])" "$BY_LEAGUE/$league.json" "$league" >> "$tally"
        else
            say "  $league: validator exit $vcode or report scope mismatch; not archived"
            printf '%s - -\n' "$league" >> "$tally"
        fi
    done < <("$PYTHON" -c "import json,sys
c=json.load(open(sys.argv[1]))
print('\\n'.join(sorted(k for k,v in c.items() if int(v.get('teams',0))>0)))" "$CATALOG" 2>/dev/null || true)

    # validate_raw_data.py always exits 0, even when it reports errors (main()
    # returns 0 unconditionally), so the finding counts are the only signal.
    "$PYTHON" - "$tally" "$BASELINE_FILE" << 'PY'
import json, os, sys

tally_path, baseline_path = sys.argv[1], sys.argv[2]
current = {}
missing = []
with open(tally_path) as fh:
    for line in fh:
        parts = line.split()
        if len(parts) != 3:
            continue
        league = parts[0]
        # "-" marks a league whose validator run could not be trusted, so it is
        # recorded as "no data" rather than as zero errors.
        if "-" in (parts[1], parts[2]):
            current[league] = None
            missing.append(league)
        else:
            current[league] = (int(parts[1]), int(parts[2]))

scored = {k: v for k, v in current.items() if v is not None}
total_e = sum(v[0] for v in scored.values())
total_w = sum(v[1] for v in scored.values())
print("  leagues requested: %d  scored: %d  errors: %d  warnings: %d"
      % (len(current), len(scored), total_e, total_w))
if missing:
    print("  note: no usable report for %d league(s): %s"
          % (len(missing), ", ".join(missing)))

baseline = {}
if os.path.exists(baseline_path):
    try:
        with open(baseline_path) as fh:
            raw = json.load(fh).get("counts", {})
        baseline = {k: (None if None in v else tuple(v)) for k, v in raw.items()}
    except Exception:
        baseline = {}

if not baseline:
    print("  no baseline yet; recording this run's counts for future comparison")
else:
    worsened = [(k, baseline[k][0], scored[k][0]) for k in sorted(scored)
                if baseline.get(k) is not None and scored[k][0] > baseline[k][0]]
    improved = [k for k in sorted(scored)
                if baseline.get(k) is not None and scored[k][0] < baseline[k][0]]
    if worsened:
        print("  WARNING: error count increased for %d league(s):" % len(worsened))
        for league, before, after in worsened:
            print("    %s: %d -> %d" % (league, before, after))
    if improved:
        print("  note: error count decreased for %d league(s)" % len(improved))
    if not worsened and not improved:
        print("  error counts unchanged since the last run")

os.makedirs(os.path.dirname(baseline_path) or ".", exist_ok=True)
with open(baseline_path, "w") as fh:
    json.dump({"counts": {k: list(v) for k, v in current.items()},
               "totals": {"errors": total_e, "warnings": total_w}}, fh, indent=2)
print("  baseline written to %s" % baseline_path)
PY
    rm -f "$tally"
}

run_stage "validate raw (per league)" validate_all_leagues

# ------------------------------------------------------------------- stage 4
# Full rebuild: 00_reset.sql drops the schema on the first league, then every
# league is loaded and analysed. Expensive (~20-35 min) but self-healing.
run_stage "build database + analysis (all leagues)" \
    "$PYTHON" backend/scripts/build_all_leagues.py

# ------------------------------------------------------------------- stage 5
run_stage "build dashboard" \
    "$PYTHON" backend/scripts/build_dashboard.py

# ------------------------------------------------------------------- summary
rule
say "[$(date -Is)] summary"
say "| stage | result | seconds |"
say "|-------|--------|---------|"
overall=0
for i in "${!STAGE_NAMES[@]}"; do
    say "| ${STAGE_NAMES[$i]} | ${STAGE_RESULTS[$i]} | ${STAGE_SECONDS[$i]} |"
    case "${STAGE_RESULTS[$i]}" in failed*) overall=1 ;; esac
done
rule

if [ "$DRY_RUN" -eq 1 ]; then
    say "DRY RUN complete; nothing was executed and no stamp was written."
    exit 0
fi

if [ "$overall" -eq 0 ]; then
    printf '%s\n' "$today" > "$STAMP_FILE"
    say "All stages succeeded. Stamp written to $STAMP_FILE ($today)."
    exit 0
fi

say "One or more stages failed; no stamp written, so the next trigger will retry."
exit 1
