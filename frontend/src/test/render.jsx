import { render } from "@testing-library/react";
import { MemoryRouter, Routes } from "react-router-dom";
import { I18nProvider } from "../i18n/I18nProvider.jsx";

/**
 * Both wrappers mount the i18n provider so components under test resolve their
 * strings and formatters through the real pipeline, not the bare fallback. The
 * provider defaults to English and Asia/Ho_Chi_Minh, which is also what a fresh
 * visitor sees — a test that wants a different language or zone overrides the
 * persisted values in `localStorage` before rendering.
 */
export function renderPage(ui, { route = "/" } = {}) {
  return render(
    <I18nProvider>
      <MemoryRouter initialEntries={[route]}>
        {ui}
      </MemoryRouter>
    </I18nProvider>,
  );
}

/**
 * For a component that reads its own route params, so the test has to supply the
 * real `<Routes>` rather than render the page bare. Kept beside `renderPage` so
 * every router in the suite carries the same provider and route resolution as
 * the app.
 *
 * @param {React.ReactNode} routes The `<Route>` elements to mount.
 * @param {object} [options]
 * @param {string} [options.route] The URL to start on.
 */
export function renderRoutes(routes, { route = "/" } = {}) {
  return render(
    <I18nProvider>
      <MemoryRouter initialEntries={[route]}>
        <Routes>{routes}</Routes>
      </MemoryRouter>
    </I18nProvider>,
  );
}