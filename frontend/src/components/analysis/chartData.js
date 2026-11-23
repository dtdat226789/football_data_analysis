import { asArray, asRecord, asText, isRecord } from "../../lib/shape.js";

const finite = (value) =>
  typeof value === "number" && Number.isFinite(value) ? value : null;

const nonNegative = (value) => (value === null ? 0 : Math.max(0, value));

function cleanRows(value, toRow) {
  const rows = [];
  for (const item of asArray(value)) {
    if (!isRecord(item)) continue;
    const row = toRow(item);
    if (row && row.label) rows.push(row);
  }
  return rows;
}

function goalsDistribution(reports, t) {
  const buckets = cleanRows(asRecord(asRecord(reports.goals_analysis).goals_distribution).buckets, (item) => {
    const label = String(item.goals ?? "");
    const count = finite(item.count);
    if (!label || count === null) return null;
    return { label, value: nonNegative(count) };
  });

  if (!buckets.length) return null;
  return {
    kind: "bar",
    labels: buckets.map((row) => row.label),
    series: [
      {
        label: t("analysis.chart.series.matches"),
        values: buckets.map((row) => row.value),
        color: "var(--accent)",
      },
    ],
    valueLabel: t("analysis.chart.unit.matches"),
    categoryLabel: t("analysis.chart.axis.goalsPerMatch"),
    horizontal: false,
  };
}

function goalsPerSeason(reports, t) {
  const seasons = cleanRows(asRecord(reports.goals_analysis).goals_per_season, (item) => {
    const label = asText(item.season).trim();
    const home = finite(item.avg_home);
    const away = finite(item.avg_away);
    if (!label || (home === null && away === null)) return null;
    return { label, home: nonNegative(home), away: nonNegative(away) };
  });

  if (!seasons.length) return null;
  return {
    kind: "stacked",
    labels: seasons.map((row) => row.label),
    series: [
      {
        label: t("analysis.chart.series.home"),
        values: seasons.map((row) => row.home),
        color: "var(--green)",
      },
      {
        label: t("analysis.chart.series.away"),
        values: seasons.map((row) => row.away),
        color: "var(--accent)",
      },
    ],
    valueLabel: t("analysis.chart.unit.goalsPerMatch"),
  };
}

function championPoints(reports, t) {
  const champions = cleanRows(asRecord(reports.season_trends).champions, (item) => {
    const points = finite(item.champion_pts);
    if (points === null) return null;
    return {
      label: asText(item.season).trim(),
      value: points,
      detail: asText(item.champion).trim(),
    };
  });

  if (!champions.length) return null;
  return {
    kind: "line",
    labels: champions.map((row) => row.label),
    details: champions.map((row) => row.detail),
    series: [
      {
        label: t("analysis.chart.series.points"),
        values: champions.map((row) => row.value),
        color: "var(--accent)",
      },
    ],
    valueLabel: t("analysis.chart.unit.points"),
  };
}

function topPoints(reports, t) {
  const teams = cleanRows(asRecord(reports.teams_analysis).teams, (item) => {
    const points = finite(item.points);
    if (points === null) return null;
    return { label: asText(item.team).trim(), value: points };
  });
  teams.sort((a, b) => b.value - a.value);
  const top = teams.slice(0, 10);

  if (!top.length) return null;
  return {
    kind: "bar",
    labels: top.map((row) => row.label),
    series: [
      {
        label: t("analysis.chart.series.points"),
        values: top.map((row) => row.value),
        color: "var(--accent)",
      },
    ],
    valueLabel: t("analysis.chart.unit.points"),
    horizontal: true,
  };
}

const BUILDERS = {
  "goals_analysis_distribution.png": goalsDistribution,
  "goals_analysis_avg_per_season.png": goalsPerSeason,
  "season_trends_champion_points.png": championPoints,
  "teams_analysis_top_points.png": topPoints,
};

export function interactiveChart(name, reports, t) {
  const builder = BUILDERS[name];
  return builder ? builder(asRecord(reports), t) : null;
}

export const INTERACTIVE_CHART_NAMES = Object.keys(BUILDERS);
