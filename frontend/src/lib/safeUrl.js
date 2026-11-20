/**
 * Return an HTTPS URL for rendering in an href, or null.
 *
 * Fixture `portal_link` values come from the upstream feed. React escapes text,
 * but it does not stop a `javascript:` href from executing when a user clicks
 * it, so protocol validation is the boundary here.
 */
export function safeHttpsUrl(value) {
  if (typeof value !== "string" || !value.trim()) return null;
  try {
    const url = new URL(value);
    return url.protocol === "https:" ? url.href : null;
  } catch {
    return null;
  }
}
