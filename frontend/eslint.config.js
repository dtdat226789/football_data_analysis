import js from "@eslint/js";
import reactHooks from "eslint-plugin-react-hooks";
import reactRefresh from "eslint-plugin-react-refresh";
import globals from "globals";

/**
 * The vitest globals `globals: true` in vite.config.js puts in scope, spelled
 * out because the linter cannot read that setting.
 */
const VITEST_GLOBALS = {
  afterAll: "readonly",
  afterEach: "readonly",
  beforeAll: "readonly",
  beforeEach: "readonly",
  describe: "readonly",
  expect: "readonly",
  it: "readonly",
  test: "readonly",
  vi: "readonly",
};

/**
 * There was no linter at all, so nothing checked the hooks rules or flagged a
 * dead import — the bugs this file now guards against were all found by reading
 * pages by hand. `npm run lint` runs this; CI runs it too.
 */
export default [
  { ignores: ["dist/**", "coverage/**", "node_modules/**"] },
  js.configs.recommended,
  reactHooks.configs.flat.recommended,

  {
    files: ["**/*.{js,jsx}"],
    languageOptions: {
      ecmaVersion: 2023,
      sourceType: "module",
      globals: { ...globals.browser, ...globals.es2023 },
      parserOptions: {
        ecmaFeatures: { jsx: true },
      },
    },
    plugins: {
      "react-refresh": reactRefresh,
    },
    rules: {
      // A hook that closes over a value it does not list keeps a stale closure
      // alive until something else re-renders it.
      "react-hooks/exhaustive-deps": "warn",
      // Unused vars are how a dead import survives a refactor; arguments are
      // left alone because a rest-arg signature often has to stay positional.
      "no-unused-vars": ["error", { argsIgnorePattern: "^_", varsIgnorePattern: "^_" }],
      eqeqeq: ["error", "smart"],
      "no-console": ["warn", { allow: ["warn", "error"] }],
      // Off for now. These two are React Compiler rules for code this app does
      // not have: reading a render-phase value into another one, or mutating
      // during render. Neither is a defect in this codebase today, and leaving
      // them on would bury the rules that are.
      "react-hooks/immutability": "off",
      "react-hooks/purity": "off",
      // A warning, not an error, and the debt is deliberate for now. Six places
      // copy a URL param into local state — `?tab=`, `?season=`, `?league=` — and
      // two set a loading or debounce flag at the top of an effect. Removing them
      // means deriving state during render instead, which is a real refactor of
      // the page/param plumbing rather than a lint fix, so it stays visible here
      // instead of being switched off.
      "react-hooks/set-state-in-effect": "warn",
      // Off: this module exports a component alongside the constants it uses
      // (UPCOMING_OFFSET_PARAM, DEFAULT_PAGE_SIZE, and similar). The rule only
      // costs a full reload on hot update, and splitting each constant into its
      // own module to satisfy it would be churn without a payoff.
      "react-refresh/only-export-components": "off",
    },
  },

  {
    files: ["**/*.test.{js,jsx}", "src/test/**"],
    languageOptions: {
      globals: { ...globals.browser, ...globals.node, ...VITEST_GLOBALS },
    },
  },

  {
    // Build and tool config runs in node, not the browser.
    files: ["*.config.js", "eslint.config.js"],
    languageOptions: {
      globals: { ...globals.node },
    },
  },
];
