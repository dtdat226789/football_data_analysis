import { render } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";

export function renderPage(ui, { route = "/" } = {}) {
  return render(<MemoryRouter initialEntries={[route]}>{ui}</MemoryRouter>);
}