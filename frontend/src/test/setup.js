import "@testing-library/jest-dom/vitest";
import { configure } from "@testing-library/react";
import { clearApiCache } from "../hooks/useApi.js";

configure({ asyncUtilTimeout: 5000 });

beforeEach(() => {
  clearApiCache();
});