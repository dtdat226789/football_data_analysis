/** League slug -> human-readable name.
 *
 * Every league-scoped API row already carries `league_name`, but a few places
 * only ever hold the slug: a league filter read back out of the URL, or a tab
 * title built from the selected filter. These resolve a slug against a league
 * list so those labels read as "Allsvenskan Women" rather than "wsweden".
 *
 * Both league shapes are accepted, because the two sources in the app differ:
 * `GET /leagues` returns `{slug, name}` while a team's season memberships
 * return `{league, league_name}`. An unknown slug falls back to itself so a
 * label is never blank, and a missing slug is null so an unscoped feed stays
 * distinguishable from a real one.
 */

export function leagueNameMap(leagues) {
  const map = new Map();
  for (const entry of leagues || []) {
    const slug = entry?.slug ?? entry?.league;
    if (slug) map.set(slug, entry?.name ?? entry?.league_name ?? slug);
  }
  return map;
}

export function leagueLabel(slug, names) {
  if (!slug) return null;
  return names?.get(slug) ?? slug;
}
