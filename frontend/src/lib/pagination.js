/**
 * The "start–end of total" caption under a paged list.
 *
 * Three lists wrote their own copy and each clamped differently, so the same
 * offset could read as a valid range on one page and as a row that is not on
 * screen on another. `pageRange` returns `null` for the case that has no honest
 * caption — an offset past the last page, where a clamp would report the last row
 * twice ("150–150 of 150") above an empty table.
 */
export function pageRange(pageSize, offset, total) {
  if (!total) return { start: 0, end: 0, total: 0 };
  if (offset >= total) return null;
  return { start: offset + 1, end: Math.min(offset + pageSize, total), total };
}

export function pageLabel(pageSize, offset, total, { empty = "0 results", past = "no rows on this page" } = {}) {
  const range = pageRange(pageSize, offset, total);
  if (range === null) return past;
  if (!range.total) return empty;
  return `${range.start}–${range.end} of ${range.total}`;
}