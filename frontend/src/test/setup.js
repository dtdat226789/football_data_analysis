import "@testing-library/jest-dom/vitest";
import { clearApiCache } from "../hooks/useApi.js";

beforeEach(() => {
  clearApiCache();
});