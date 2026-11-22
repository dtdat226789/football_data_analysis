#!/usr/bin/env bash
#
# Daily refresh of the Football Charts dataset (raw -> Postgres -> analysis -> dashboard -> ML).
#
#   1. collect_all_leagues.py --active-only --overwrite   results + tables for live seasons
#   2. fetch_fixtures.py --overwrite                     upcoming fixtures + model_predictions
#   3. fetch_fixture_details.py                          per-match detail cache
#   4. validate_raw_data.py  (one league per run)        raw-data findings
#   5. build_all_leagues.py                              Postgres rebuild + analysis, all leagues
#   6. build_dashboard.py                                all-league HTML dashboard
#   7. generate_ml_artifacts.sh                          dataset, gated model, predictions
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
VALIDATION_STATUS="$LOG_DIR/.validation_status.json"
SUMMARY_FILE="$LOG_DIR/refresh_summary.json"
STAGE_TSV="$LOG_DIR/.stage_results.tsv"
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
        # Prefer the configured DSN so the check follows DATABASE_URL when it
        # points at a remote server (Neon in CI). The Python steps load it from
        # .env, but the shell only sees it when the caller exports it.
        if [ -n "${DATABASE_URL:-}" ]; then
            if pg_isready -q -d "$DATABASE_URL"; then
                say "postgres: ready (DATABASE_URL)"
            else
                say "FATAL: PostgreSQL at DATABASE_URL is not accepting connections."
                pg_isready -d "$DATABASE_URL" || true
                fail=1
            fi
        elif pg_isready -q; then say "postgres: ready"
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
: > "$STAGE_TSV"

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
    printf '%s\t%s\t%s\n' "$name" "${STAGE_RESULTS[-1]}" "$((t1 - t0))" >> "$STAGE_TSV"
}

# ------------------------------------------------------------------- stage 1
run_stage "collect raw (active seasons)" \
    "$PYTHON" backend/scripts/collect_all_leagues.py --active-only --overwrite

# ------------------------------------------------------------------- stage 2
run_stage "fetch fixtures" \
    "$PYTHON" backend/scripts/fetch_fixtures.py --overwrite

# ------------------------------------------------------------------- stage 3
run_stage "fetch fixture details" \
    "$PYTHON" backend/scripts/fetch_fixture_details.py --overwrite

# ------------------------------------------------------------------- stage 4
# validate_raw_data.py takes a single --league and writes to the same
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
    local league s args seasons league_failed=0
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
        # Archive only when the report is actually scoped to this league. The
        # path is hardcoded, so a crashed run could leave the previous league's
        # report behind and silently mislabel it. A non-zero validator exit
        # means errors were found; the report is still trustworthy and the
        # baseline decides whether those errors are new.
        if [ -f "$CANONICAL_REPORT" ] && "$PYTHON" -c "import json,sys
try: sys.exit(0 if json.load(open(sys.argv[1])).get('scope',{}).get('league')==sys.argv[2] else 1)
except Exception: sys.exit(1)" "$CANONICAL_REPORT" "$league"; then
            if [ "$vcode" -ne 0 ]; then
                say "  $league: validator reported errors (exit $vcode)"
            fi
            cp -f "$CANONICAL_REPORT" "$BY_LEAGUE/$league.json"
            "$PYTHON" -c "import json,sys
try:
    o=json.load(open(sys.argv[1])).get('overall',{})
    print('%s %s %s' % (sys.argv[2], o.get('errors',0), o.get('warnings',0)))
except Exception: print('%s - -' % sys.argv[2])" "$BY_LEAGUE/$league.json" "$league" >> "$tally"
        else
            say "  $league: validator exit $vcode or report scope mismatch; not archived"
            printf '%s - -\n' "$league" >> "$tally"
            league_failed=$((league_failed + 1))
        fi
    done < <("$PYTHON" -c "import json,sys
c=json.load(open(sys.argv[1]))
print('\\n'.join(sorted(k for k,v in c.items() if int(v.get('teams',0))>0)))" "$CATALOG" 2>/dev/null || true)

    # validate_raw_data.py exits 1 when it finds errors; the baseline decides
    # whether those errors are a new regression or part of the known backlog.
    "$PYTHON" backend/scripts/validation_baseline.py \
        --tally "$tally" --baseline "$BASELINE_FILE" --status "$VALIDATION_STATUS"
    rm -f "$tally"
    blocked="$("$PYTHON" -c "import json,sys
print('1' if json.load(open(sys.argv[1])).get('blocking') else '0')" "$VALIDATION_STATUS")"
    if [ "$blocked" -ne 0 ] || [ "$league_failed" -ne 0 ]; then
        say "  validation regressed or produced unusable reports; refusing to publish."
        return 1
    fi
    return 0
}

run_stage "validate raw (per league)" validate_all_leagues

# ------------------------------------------------------------------- stage 5
# Full rebuild: 00_reset.sql drops the schema on the first league, then every
# league is loaded and analysed. Expensive (~20-35 min) but self-healing.
run_stage "build database + analysis (all leagues)" \
    "$PYTHON" backend/scripts/build_all_leagues.py --reset-local

# ------------------------------------------------------------------- stage 6
run_stage "build dashboard" \
    "$PYTHON" backend/scripts/build_dashboard.py

# ------------------------------------------------------------------- stage 7
run_stage "generate ML artifacts" \
    bash scripts/generate_ml_artifacts.sh

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

"$PYTHON" - "$STAGE_TSV" "$SUMMARY_FILE" "$today" "$overall" << 'PY'
import json
import sys

tsv_path, out_path, today, overall = sys.argv[1:]
stages = []
with open(tsv_path, encoding="utf-8") as fh:
    for line in fh:
        parts = line.rstrip("\n").split("\t")
        if len(parts) == 3:
            stages.append({"name": parts[0], "result": parts[1], "seconds": int(parts[2])})
payload = {
    "date": today,
    "overall": "ok" if overall == "0" else "failed",
    "stage_count": len(stages),
    "stages": stages,
}
with open(out_path, "w", encoding="utf-8") as fh:
    json.dump(payload, fh, indent=2)
print(f"stage summary: {out_path} ({payload['overall']}, {len(stages)} stages)")
PY

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
