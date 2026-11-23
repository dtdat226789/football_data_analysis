export function niceMax(values) {
  const max = values.reduce((highest, value) => Math.max(highest, value), 0);
  if (!Number.isFinite(max) || max <= 0) return 1;
  const magnitude = 10 ** Math.floor(Math.log10(max));
  const steps = [1, 2, 2.5, 5, 10];
  const step = steps.find((candidate) => candidate * magnitude >= max) ?? 10;
  return step * magnitude;
}

export function labelStep(count, maxLabels) {
  return Math.max(1, Math.ceil(count / maxLabels));
}

export function formatTick(value, num, dec) {
  return Number.isInteger(value) ? num(value) : dec(value, 1);
}
