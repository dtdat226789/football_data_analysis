// Guards against referencing a CSS custom property that is never defined.
// A `var(--typo)` has no fallback, so the browser silently falls back to
// inherited/initial value: the element renders in the wrong colour (or no
// colour) and nothing in the test suite notices. TeamDetail's loss colour used
// `var(--danger)` while the palette only ever defined `--red`.
import { readdirSync, readFileSync, statSync } from "node:fs";
import { join, relative, resolve } from "node:path";
import { describe, expect, it } from "vitest";

const SRC = resolve(process.cwd(), "src");
const CSS_FILES = ["index.css"];

function walk(dir, out = []) {
  for (const entry of readdirSync(dir)) {
    const full = join(dir, entry);
    if (statSync(full).isDirectory()) {
      if (entry === "node_modules" || entry === "test") continue;
      walk(full, out);
    } else if (/\.(jsx?|css)$/.test(entry)) {
      out.push(full);
    }
  }
  return out;
}

function definedProps() {
  const found = new Set();
  for (const file of CSS_FILES) {
    const css = readFileSync(join(SRC, file), "utf8");
    for (const m of css.matchAll(/(--[\w-]+)\s*:/g)) found.add(m[1]);
  }
  return found;
}

function usedProps() {
  const uses = [];
  for (const file of walk(SRC)) {
    if (CSS_FILES.includes(file.slice(SRC.length + 1))) continue;
    const src = readFileSync(file, "utf8");
    for (const m of src.matchAll(/var\(\s*(--[\w-]+)/g)) {
      uses.push({ prop: m[1], file: relative(SRC, file) });
    }
  }
  return uses;
}

describe("CSS custom properties", () => {
  it("declares a non-trivial palette", () => {
    expect(definedProps().size).toBeGreaterThan(3);
  });

  it("only uses custom properties that are actually defined", () => {
    const defined = definedProps();
    const undefinedUses = usedProps().filter((u) => !defined.has(u.prop));

    expect(
      undefinedUses.map((u) => `var(${u.prop}) in ${u.file}`),
    ).toEqual([]);
  });

  it("renders the loss colour from a defined variable", () => {
    const teamDetail = readFileSync(join(SRC, "pages/TeamDetail.jsx"), "utf8");
    const loss = teamDetail.match(/LOSS_COLOR\s*=\s*"var\((--[\w-]+)\)"/);
    expect(loss).not.toBeNull();
    expect(definedProps()).toContain(loss[1]);
    // and it must differ from the win colour, or W/D/L is not actually encoded
    const win = teamDetail.match(/WIN_COLOR\s*=\s*"var\((--[\w-]+)\)"/);
    expect(loss[1]).not.toBe(win[1]);
  });
});
