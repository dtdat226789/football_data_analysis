import { describe, expect, it } from "vitest";

import en from "../../i18n/en.js";
import { interactiveChart } from "./chartData.js";

const t = (key) => en[key] ?? key;

const reports = {
  goals_analysis: {
    goals_distribution: {
      buckets: [
        { goals: 0, count: 12, pct: 24 },
        { goals: 1, count: 25, pct: 50 },
        { goals: 2, count: 13, pct: 26 },
        { goals: null, count: 9, pct: 0 },
      ],
    },
    goals_per_season: [
      { season: "2023-2024", avg_home: 1.6, avg_away: 1.1 },
      { season: "2024-2025", avg_home: 1.7, avg_away: null },
      { season: "", avg_home: 2, avg_away: 2 },
    ],
  },
  season_trends: {
    champions: [
      { season: "2023-2024", champion: "Arsenal", champion_pts: 84 },
      { season: "2024-2025", champion: "Chelsea", champion_pts: null },
      { season: "2025-2026", champion: "City", champion_pts: 91 },
    ],
  },
  teams_analysis: {
    teams: [
      { team: "Arsenal", points: 84 },
      { team: "City", points: 91 },
      { team: "Broken", points: null },
    ],
  },
};

describe("interactiveChart", () => {
  it("returns null for charts without an adapter or usable data", () => {
    expect(interactiveChart("unknown.png", reports, t)).toBeNull();
    expect(interactiveChart("goals_analysis_distribution.png", {}, t)).toBeNull();
  });

  it("maps the goals distribution into a bar spec and skips malformed buckets", () => {
    const spec = interactiveChart("goals_analysis_distribution.png", reports, t);

    expect(spec).toMatchObject({
      kind: "bar",
      labels: ["0", "1", "2"],
      horizontal: false,
      valueLabel: "matches",
      categoryLabel: "total goals per match",
    });
    expect(spec.series[0]).toMatchObject({ label: "Matches", values: [12, 25, 13] });
  });

  it("maps seasons into stacked home and away series with missing values treated as zero", () => {
    const spec = interactiveChart("goals_analysis_avg_per_season.png", reports, t);

    expect(spec.kind).toBe("stacked");
    expect(spec.labels).toEqual(["2023-2024", "2024-2025"]);
    expect(spec.series.map((item) => item.values)).toEqual([[1.6, 1.7], [1.1, 0]]);
  });

  it("maps champion points into a line spec and keeps champion names as details", () => {
    const spec = interactiveChart("season_trends_champion_points.png", reports, t);

    expect(spec.kind).toBe("line");
    expect(spec.labels).toEqual(["2023-2024", "2025-2026"]);
    expect(spec.details).toEqual(["Arsenal", "City"]);
    expect(spec.series[0].values).toEqual([84, 91]);
  });

  it("maps the top ten teams by points in descending order", () => {
    const manyTeams = Array.from({ length: 12 }, (_, index) => ({
      team: `Team ${index}`,
      points: index * 3,
    }));
    const spec = interactiveChart("teams_analysis_top_points.png", {
      teams_analysis: { teams: manyTeams },
    }, t);

    expect(spec.kind).toBe("bar");
    expect(spec.horizontal).toBe(true);
    expect(spec.labels).toHaveLength(10);
    expect(spec.labels[0]).toBe("Team 11");
    expect(spec.series[0].values[0]).toBe(33);
  });
});
