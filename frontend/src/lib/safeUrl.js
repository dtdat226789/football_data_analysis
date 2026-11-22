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

const CHART_NAME = /^[A-Za-z0-9_-]+\.png$/;

export function isValidChartName(value) {
  return typeof value === "string" && CHART_NAME.test(value);
}

export function safeImageUrl(value) {
  if (typeof value !== "string" || !value.trim()) return null;
  if (value.startsWith("/") && !value.startsWith("//") && !value.startsWith("/\\")) {
    return value;
  }
  return safeHttpsUrl(value);
}
