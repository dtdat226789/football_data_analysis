"""Static HTML dashboard builder for the Common Data Analysis Framework.

Reads the per-league analysis reports (``data/analysis/{league}/``) produced by
``run_analysis.py`` and emits a single self-contained ``dashboard.html`` with:

* a league switcher across every league in the config (empty-state for leagues
  that have not been collected/analysed yet),
* interactive Chart.js charts (outcome split, goals per season, goal
  distribution, top scorelines, champion points, top teams by points),
* headline stats and the consolidated findings list.

Chart.js is vendored at build time: ``chart.umd.min.js`` is downloaded once
into ``<analysis_dir>/vendor/``. On offline builds the dashboard still renders
but charts degrade to a placeholder notice.

    python backend/scripts/build_dashboard.py
    python backend/scripts/build_dashboard.py --league premier --out-dir data/
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from analysis_common import ROOT_DIR  # noqa: E402
from db_common import LEAGUE_CONFIG  # noqa: E402

CHARTJS_URL = "https://cdn.jsdelivr.net/npm/chart.js@4.4.7/dist/chart.umd.min.js"
CHARTJS_VERSION = "4.4.7"

MODULE_STEMS = [
    "database_profile", "matches_analysis", "goals_analysis", "teams_analysis",
    "season_trends", "scoreline_analysis", "relationships", "findings",
]


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the static analysis HTML dashboard.")
    parser.add_argument("--league", default=None,
                        help="only include this league (default: every league with reports)")
    parser.add_argument("--analysis-dir", type=Path, default=ROOT_DIR / "data" / "analysis",
                        help="directory holding per-league reports (default: data/analysis)")
    parser.add_argument("--out-dir", type=Path, default=ROOT_DIR / "data" / "analysis",
                        help="where dashboard.html is written (default: analysis dir)")
    parser.add_argument("--refresh-vendor", action="store_true",
                        help="re-download Chart.js even if already vendored")
    return parser.parse_args(argv)


def load_reports(league_dir: Path) -> dict:
    reports: dict = {}
    for stem in MODULE_STEMS:
        path = league_dir / f"{stem}.json"
        if path.exists():
            try:
                reports[stem] = json.loads(path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                continue
    return reports


def extract_chart_data(reports: dict) -> dict:
    """Pull small, browser-ready datasets out of the report JSONs.

    Every accessor is defensive so a partially generated league still renders
    whatever is available.
    """
    charts: dict = {}
    keys: list[str] = []
    seen = set()

    m = reports.get("matches_analysis", {})
    overall = m.get("overall", {}) or {}
    if overall.get("n_matches") is not None:
        charts["outcome"] = {
            "labels": ["Home wins", "Draws", "Away wins"],
            "values": [overall.get("home_wins", 0), overall.get("draws", 0),
                       overall.get("away_wins", 0)],
        }
        seen.add("outcome")

    g = reports.get("goals_analysis", {})
    gps = g.get("goals_per_season", []) or []
    if gps:
        charts["avg_goals"] = {
            "labels": [x["season"] for x in gps],
            "home": [x.get("avg_home") or 0 for x in gps],
            "away": [x.get("avg_away") or 0 for x in gps],
            "avg": [x.get("avg_goals") or 0 for x in gps],
        }
        seen.add("avg_goals")
    buckets = g.get("goals_distribution", {}).get("buckets", []) or []
    if buckets:
        charts["goals_dist"] = {
            "labels": [str(x["goals"]) for x in buckets],
            "values": [x["count"] for x in buckets],
        }
        seen.add("goals_dist")

    s = reports.get("scoreline_analysis", {})
    top = (s.get("scoreline_frequency", {}).get("top", []) or [])[:10]
    if top:
        charts["scorelines"] = {
            "labels": [x["scoreline"] for x in top],
            "values": [x["count"] for x in top],
        }
        seen.add("scorelines")

    t = reports.get("season_trends", {})
    champs = t.get("champions", []) or []
    if champs:
        charts["champions"] = {
            "labels": [x["season"] for x in champs],
            "values": [x.get("champion_pts", 0) for x in champs],
            "names": [x.get("champion", "") for x in champs],
        }
        seen.add("champions")

    tm = reports.get("teams_analysis", {})
    teams = (tm.get("teams", []) or [])
    if teams:
        leaders = sorted(teams, key=lambda x: x.get("points", 0), reverse=True)[:10]
        charts["top_teams"] = {
            "labels": [x["team"] for x in leaders],
            "values": [x.get("points", 0) for x in leaders],
        }
        seen.add("top_teams")

    keys = [k for k in (
        "outcome", "avg_goals", "goals_dist", "scorelines", "champions", "top_teams"
    ) if k in seen]
    return {"charts": charts, "order": keys}


def headline_stats(reports: dict) -> dict:
    g = reports.get("goals_analysis", {})
    gps = g.get("goals_per_season", []) or []
    overall = reports.get("matches_analysis", {}).get("overall", {}) or {}
    total_goals = (overall.get("home_goals", 0)
                   + (overall.get("away_goals") if "away_goals" in overall else 0))
    return {
        "n_matches": overall.get("n_matches"),
        "home_win_pct": overall.get("home_win_pct"),
        "draw_pct": overall.get("draw_pct"),
        "away_win_pct": overall.get("away_win_pct"),
        "total_goals": total_goals or None,
        "avg_goals": gps[-1].get("avg_goals") if gps else None,
        "n_seasons": len(gps) or None,
    }


def collect_leagues(config: dict, analysis_dir: Path, only: str | None) -> list[dict]:
    """One entry per configured league; has_data only where reports exist."""
    leagues: list[dict] = []
    for slug, meta in config.items():
        if only and slug != only:
            continue
        league_dir = analysis_dir / slug
        reports = load_reports(league_dir) if league_dir.is_dir() else {}
        has_data = bool(reports)
        entry = {
            "slug": slug,
            "name": meta.get("name", slug),
            "country": meta.get("country", ""),
            "teams": meta.get("teams", 20),
            "format": meta.get("format", "round-robin"),
            "has_data": has_data,
        }
        if has_data:
            data = extract_chart_data(reports)
            entry["stats"] = headline_stats(reports)
            entry["charts"] = data["charts"]
            entry["chart_order"] = data["order"]
            entry["findings"] = (reports.get("findings", {}).get("key_findings", []) or [])
            entry["generated_at"] = reports.get("findings", {}).get("generated_at", "")
            entry["reports"] = sorted(reports)
        leagues.append(entry)
    return leagues


def vendor_chartjs(vendor_dir: Path, refresh: bool) -> Path | None:
    """Download Chart.js UMD once; return the target path or None when offline."""
    vendor_dir.mkdir(parents=True, exist_ok=True)
    target = vendor_dir / "chart.umd.min.js"
    if target.exists() and not refresh:
        return target
    try:
        with urllib.request.urlopen(CHARTJS_URL, timeout=30) as resp:
            body = resp.read()
        if len(body) < 50_000 or b"Chart" not in body[:2000]:
            raise ValueError("unexpected Chart.js payload")
        target.write_bytes(body)
        return target
    except Exception as exc:  # noqa: BLE001 - offline builds must still work
        print(f"build_dashboard: could not vendor Chart.js ({exc}); charts will be disabled")
        return None


def build_html(leagues: list[dict], vendor_ok: bool, analysis_dir: Path, out_dir: Path) -> str:
    vendor_rel = "vendor/chart.umd.min.js"
    if out_dir.resolve() != analysis_dir.resolve():
        try:
            vendor_rel = str(Path("vendor").relative_to(Path(".")))
        except ValueError:
            vendor_rel = ""
    payload = json.dumps(
        {"leagues": leagues, "chartjs": bool(vendor_ok), "chartjs_version": CHARTJS_VERSION,
         "built_at": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    )
    html = _HTML.replace("__VENDOR_SRC__", vendor_rel if vendor_ok else "")
    html = html.replace("__DATA_JSON__", payload)
    return html


_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Football Charts - Common Data Analysis Framework</title>
<script src="__VENDOR_SRC__"></script>
</head>
<body>
<header class="top">
  <div>
    <h1>Football Charts</h1>
    <p class="sub">Common Data Analysis Framework &middot; interactive report dashboard</p>
  </div>
  <div class="controls">
    <label for="league">League</label>
    <select id="league"></select>
    <span id="gen"></span>
  </div>
</header>
<main>
  <section id="kpis" class="kpi-row"></section>
  <section id="charts" class="chart-grid"></section>
  <section id="findings-card" class="card">
    <h2>Key findings</h2>
    <ol id="findings"></ol>
  </section>
  <section id="empty" class="empty hidden">
    <h2>No analysis reports for this league yet</h2>
    <p>Run the data collection and <code>run_analysis.py --league <span id="empty-league"></span></code> to generate reports for this league.</p>
  </section>
  <footer>Built at <span id="built"></span> &middot; Chart.js v<span id="chartjs-ver"></span></footer>
</main>
<script>
const DATA = __DATA_JSON__;
const LEAGUES = DATA["leagues"];
const map = Object.fromEntries(LEAGUES.map(l => [l["slug"], l]));
const sel = document.getElementById("league");
for (const l of LEAGUES) {
  const opt = document.createElement("option");
  opt.value = l["slug"];
  opt.textContent = l["slug"] + " - " + l["name"] + (l["country"] ? " (" + l["country"] + ")" : "") + (l["has_data"] ? "" : " (no data)");
  sel.appendChild(opt);
}
const chartEls = {
  "outcome": "chart-outcome", "avg_goals": "chart-avg-goals", "goals_dist": "chart-goals-dist",
  "scorelines": "chart-scorelines", "champions": "chart-champions", "top_teams": "chart-top-teams"
};
const emptyKeys = ["outcome", "avg_goals", "goals_dist", "scorelines", "champions", "top_teams"];
function chartSpec(key, entry) {
  const c = entry["charts"][key];
  if (key === "outcome") return {type: "doughnut", data: {
      labels: c["labels"], datasets: [{data: c["values"], backgroundColor: ["#34d399", "#94a3b8", "#f87171"]}]},
      options: {responsive: true, plugins: {legend: {position: "bottom"}}}};
  if (key === "avg_goals") return {type: "line", data: {
      labels: c["labels"],
      datasets: [
        {label: "Total", data: c["avg"], borderColor: "#38bdf8", tension: .3, fill: false},
        {label: "Home", data: c["home"], borderColor: "#34d399", tension: .3, fill: false},
        {label: "Away", data: c["away"], borderColor: "#f87171", tension: .3, fill: false}]},
      options: {responsive: true, plugins: {legend: {position: "bottom"}}}};
  if (key === "goals_dist") return {type: "bar", data: {
      labels: c["labels"], datasets: [{label: "Matches", data: c["values"], backgroundColor: "#38bdf8"}]},
      options: {responsive: true, plugins: {legend: {display: false}}, scales: {x: {title: {display: true, text: "Goals"}}}}};
  if (key === "scorelines") return {type: "bar", data: {
      labels: c["labels"], datasets: [{label: "Matches", data: c["values"], backgroundColor: "#a78bfa"}]},
      options: {indexAxis: "y", responsive: true, plugins: {legend: {display: false}}}};
  if (key === "champions") return {type: "line", data: {
      labels: c["labels"], datasets: [{label: "Champion points", data: c["values"], borderColor: "#fbbf24", tension: .3, fill: false}]},
      options: {responsive: true, plugins: {legend: {display: false},
        tooltip: {callbacks: {title: (items) => c["labels"][items[0]["dataIndex"]], label: (i) => c["names"][i["dataIndex"]] + " - " + c["values"][i["dataIndex"]] + " pts"}}}};
  if (key === "top_teams") return {type: "bar", data: {
      labels: c["labels"], datasets: [{label: "Points", data: c["values"], backgroundColor: "#34d399"}]},
      options: {indexAxis: "y", responsive: true, plugins: {legend: {display: false}}}};
  return null;
}
let charts = {};
function render(slug) {
  const entry = map[slug];
  const empty = document.getElementById("empty");
  const chGrid = document.getElementById("charts");
  const findCard = document.getElementById("findings-card");
  document.getElementById("kpis").innerHTML = "";
  chGrid.innerHTML = "";
  document.getElementById("findings").innerHTML = "";
  document.getElementById("gen").textContent = "";
  if (!entry || !entry["has_data"]) {
    document.getElementById("empty-league").textContent = slug;
    empty.classList.remove("hidden");
    chGrid.classList.add("hidden"); findCard.classList.add("hidden");
    return;
  }
  empty.classList.add("hidden"); chGrid.classList.remove("hidden"); findCard.classList.remove("hidden");
  document.getElementById("gen").textContent = "generated " + (entry["generated_at"] || "").slice(0, 19).replace("T", " ");
  for (const c of Object.values(charts)) { if (c) c.destroy(); }
  charts = {};
  const s = entry["stats"] || {};
  const kpis = [
    ["Matches", s["n_matches"]], ["Home win", fmtPct(s["home_win_pct"])],
    ["Draw", fmtPct(s["draw_pct"])], ["Away win", fmtPct(s["away_win_pct"])],
    ["Goals total", s["total_goals"]], ["Avg goals/game", s["avg_goals"]], ["Seasons", s["n_seasons"]]];
  const kpiRow = document.getElementById("kpis");
  for (const [k, v] of kpis) {
    if (v === null || v === undefined || v === "") continue;
    const cell = document.createElement("div"); cell.className = "kpi";
    cell.innerHTML = "<span class=\"kpi-v\">" + v + "</span><span class=\"kpi-k\">" + k + "</span>";
    kpiRow.appendChild(cell);
  }
  if (DATA["chartjs"]) {
    for (const key of (entry["chart_order"] || emptyKeys)) {
      const spec = chartSpec(key, entry);
      if (!spec) continue;
      const div = document.createElement("div"); div.className = "card chart";
      div.id = "wrap-" + chartEls[key];
      div.innerHTML = "<h2>" + chartTitle(key) + "</h2><canvas id=\"" + chartEls[key] + "\"></canvas>";
      chGrid.appendChild(div);
      charts[key] = new Chart(document.getElementById(chartEls[key]), spec);
    }
  } else {
    chGrid.appendChild(placeholderCard("Chart.js unavailable", "The build ran offline; run build_dashboard.py with network access to vendor Chart.js."));
  }
  const list = document.getElementById("findings");
  for (const f of (entry["findings"] || [])) {
    const li = document.createElement("li");
    const imp = f["importance"] || "info";
    li.innerHTML = "<span class=\"badge " + imp + "\">" + imp + "</span> <b>" +
      escapeHtml(String(f["finding"] || "")) + "</b> <span class=\"det\">" +
      escapeHtml(String(f["detail"] || "")) + "</span>";
    list.appendChild(li);
  }
  if ((entry["findings"] || []).length === 0) {
    const li = document.createElement("li"); li.textContent = "No findings compiled.";
    list.appendChild(li);
  }
}
function chartTitle(key) {
  return {"outcome": "Result split", "avg_goals": "Goals per season", "goals_dist": "Goals per match",
    "scorelines": "Most common scorelines", "champions": "Champion points", "top_teams": "Top teams by points"}[key] || key;
}
function fmtPct(v) { return (v === null || v === undefined) ? "-" : v + "%"; }
function placeholderCard(title, msg) {
  const div = document.createElement("div"); div.className = "card";
  div.innerHTML = "<h2>" + title + "</h2><p class=\"det\">" + msg + "</p>";
  return div;
}
function escapeHtml(s) { return s.replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c])); }
sel.addEventListener("change", () => render(sel.value));
document.getElementById("built").textContent = DATA["built_at"];
document.getElementById("chartjs-ver").textContent = DATA["chartjs_version"];
render(sel.value);
</script>
<style>
:root { color-scheme: dark; }
* { box-sizing: border-box; }
body { margin: 0; font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif; background: #0f172a; color: #e2e8f0; }
header.top { display: flex; justify-content: space-between; align-items: center; gap: 16px; flex-wrap: wrap; padding: 20px 28px; background: #0b1120; border-bottom: 1px solid #1e293b; position: sticky; top: 0; z-index: 5; }
header.top h1 { margin: 0; font-size: 22px; letter-spacing: .5px; }
.sub { margin: 2px 0 0; color: #94a3b8; font-size: 13px; }
.controls { display: flex; align-items: center; gap: 8px; }
.controls label { color: #94a3b8; font-size: 13px; }
select { background: #1e293b; color: #e2e8f0; border: 1px solid #334155; border-radius: 6px; padding: 7px 10px; font-size: 14px; max-width: 320px; }
#gen { color: #64748b; font-size: 12px; }
main { max-width: 1200px; margin: 0 auto; padding: 24px 28px 40px; }
.kpi-row { display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 12px; margin-bottom: 20px; }
.kpi { background: #111c33; border: 1px solid #1e293b; border-radius: 10px; padding: 14px 16px; }
.kpi-v { display: block; font-size: 22px; font-weight: 700; color: #38bdf8; }
.kpi-k { font-size: 12px; color: #94a3b8; text-transform: uppercase; letter-spacing: .5px; }
.chart-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 16px; }
.card { background: #111c33; border: 1px solid #1e293b; border-radius: 10px; padding: 16px 18px; }
.card h2 { margin: 0 0 12px; font-size: 15px; color: #cbd5e1; }
.chart canvas { max-height: 300px; }
#findings-card { margin-top: 20px; }
#findings { padding-left: 20px; line-height: 1.55; }
#findings li { margin-bottom: 8px; }
.det { color: #94a3b8; font-size: 13px; }
.badge { display: inline-block; font-size: 11px; font-weight: 700; padding: 1px 7px; border-radius: 999px; text-transform: uppercase; vertical-align: 1px; }
.badge.critical, .badge.high { background: #7f1d1d; color: #fca5a5; }
.badge.medium { background: #713f12; color: #fcd34d; }
.badge.low, .badge.info { background: #1e3a5f; color: #93c5fd; }
.empty { background: #111c33; border: 1px dashed #334155; border-radius: 10px; padding: 40px; text-align: center; }
.empty h2 { margin-top: 0; }
.hidden { display: none !important; }
code { background: #1e293b; padding: 2px 6px; border-radius: 4px; font-size: 13px; }
footer { margin-top: 28px; color: #475569; font-size: 12px; }
</style>
</body>
</html>
"""


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    analysis_dir = args.analysis_dir.resolve()
    out_dir = args.out_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    vendor_dir = analysis_dir / "vendor"
    vendored = vendor_chartjs(vendor_dir, args.refresh_vendor)

    leagues = collect_leagues(LEAGUE_CONFIG, analysis_dir, args.league)
    with_data = [l for l in leagues if l["has_data"]]

    html = build_html(leagues, vendored is not None, analysis_dir, out_dir)
    out_path = out_dir / "dashboard.html"
    out_path.write_text(html, encoding="utf-8")

    print(f"build_dashboard: wrote {out_path}")
    print(f"  leagues in config : {len(leagues)}")
    print(f"  leagues with data : {len(with_data)} ({', '.join(l['slug'] for l in with_data) or '-'})")
    print(f"  chart.js vendored : {vendored is not None and ('refresh' if args.refresh_vendor else 'reused')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
