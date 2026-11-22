export function isRecord(value) {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}

export function asRecord(value) {
  return isRecord(value) ? value : {};
}

export function asArray(value) {
  return Array.isArray(value) ? value : [];
}

export function asText(value, fallback = "") {
  return typeof value === "string" ? value : fallback;
}

export function asNumber(value, fallback = 0) {
  return typeof value === "number" && Number.isFinite(value) ? value : fallback;
}
