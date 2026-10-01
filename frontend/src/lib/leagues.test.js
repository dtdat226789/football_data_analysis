import { describe, expect, it } from "vitest";

import { leagueLabel, leagueNameMap } from "./leagues.js";

describe("leagueNameMap", () => {
  it("reads the /leagues shape of slug + name", () => {
    const names = leagueNameMap([
      { slug: "wsweden", name: "Allsvenskan Women" },
      { slug: "premier", name: "Premier League" },
    ]);
    expect(names.get("wsweden")).toBe("Allsvenskan Women");
    expect(names.get("premier")).toBe("Premier League");
  });

  it("also reads the team-membership shape of league + league_name", () => {
    const names = leagueNameMap([{ league: "wgermany1", league_name: "Bundesliga Women" }]);
    expect(names.get("wgermany1")).toBe("Bundesliga Women");
  });

  it("survives a missing, empty or malformed list", () => {
    expect(leagueNameMap(undefined).size).toBe(0);
    expect(leagueNameMap([]).size).toBe(0);
    expect(leagueNameMap([null, {}, { slug: "" }]).size).toBe(0);
  });
});

describe("leagueLabel", () => {
  const names = leagueNameMap([{ slug: "wsweden", name: "Allsvenskan Women" }]);

  it("resolves a known slug to its name", () => {
    expect(leagueLabel("wsweden", names)).toBe("Allsvenskan Women");
  });

  it("falls back to the slug so a label is never blank", () => {
    expect(leagueLabel("not-a-league", names)).toBe("not-a-league");
    expect(leagueLabel("premier", undefined)).toBe("premier");
  });

  it("returns null for no league, so an unscoped feed stays distinguishable", () => {
    expect(leagueLabel("", names)).toBeNull();
    expect(leagueLabel(null, names)).toBeNull();
    expect(leagueLabel(undefined, names)).toBeNull();
  });
});
