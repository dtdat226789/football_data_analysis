import { api as realApi } from "../api/client.js";

/**
 * The mocked client, as the tests see it.
 *
 * A test file imports `api` from here rather than from the client module itself.
 * `vi.mock` swaps the implementation at runtime but cannot swap the type, so
 * importing it straight from the client made every `api.fixtures.mockResolvedValue`
 * in the suite a type error — 82 of them, and no way to tell a real typo from the
 * mock. This re-export resolves to the same mocked module at runtime and carries
 * the mock-shaped type, so a wrong method name is now caught by `npm run typecheck`.
 *
 * @type {import("vitest").Mocked<typeof realApi>}
 */
export const api = /** @type {import("vitest").Mocked<typeof realApi>} */ (realApi);
