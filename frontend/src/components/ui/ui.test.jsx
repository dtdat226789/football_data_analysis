import { fireEvent, render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";

import { BackLink, Badge, Card, CardHeader, PageHeader, TableShell, Tabs } from "./index.js";
import { renderPage } from "../../test/render.jsx";

describe("shared UI primitives", () => {
  it("keeps the back arrow out of the link's accessible name", () => {
    renderPage(<BackLink to="/teams">Back to teams</BackLink>);

    const link = screen.getByRole("link", { name: "Back to teams" });
    expect(link).toHaveAttribute("href", "/teams");
    expect(link.querySelector("span[aria-hidden='true']")).toHaveTextContent("←");
  });

  it("keeps the page heading and its subtitle under the same parent", () => {
    render(<PageHeader title="Dashboard" subtitle="0 leagues" />);

    const heading = screen.getByRole("heading", { name: "Dashboard" });
    expect(heading.parentElement.textContent).toContain("0 leagues");
    expect(heading.closest(".page-head")).toBeInTheDocument();
  });

  it("places page actions beside the heading", () => {
    render(
      <PageHeader title="Matches" actions={<button type="button">Filter</button>} />,
    );

    expect(screen.getByRole("button", { name: "Filter" }).closest(".page-head-actions")).toBeInTheDocument();
  });

  it("renders a card as a section by default and honours an alternate element", () => {
    const { container, rerender } = render(<Card>content</Card>);
    expect(container.querySelector("section.card")).toBeInTheDocument();

    rerender(<Card as="div">content</Card>);
    expect(container.querySelector("div.card")).toBeInTheDocument();
    expect(container.querySelector("section.card")).not.toBeInTheDocument();
  });

  it("renders a card header with a title and actions", () => {
    render(
      <Card>
        <CardHeader title="Standings" actions={<span>season</span>} />
      </Card>,
    );

    const heading = screen.getByRole("heading", { name: "Standings" });
    expect(heading.closest(".card-head")).toBeInTheDocument();
    expect(heading.closest("section.card")).toHaveTextContent("season");
  });

  it("composes badge tone classes", () => {
    const { container } = render(
      <>
        <Badge>plain</Badge>
        <Badge tone="green">ready</Badge>
      </>,
    );

    expect(container.querySelector("span.badge")).toHaveTextContent("plain");
    expect(container.querySelector("span.badge.green")).toHaveTextContent("ready");
  });

  it("keeps tabs as buttons and reports the active one", () => {
    const onChange = vi.fn();
    render(
      <Tabs
        items={[
          { key: "a", label: "First" },
          { key: "b", label: "Second" },
        ]}
        active="a"
        onChange={onChange}
        label="Sections"
        trailing={<span className="tab-spacer" />}
      />,
    );

    const first = screen.getByRole("button", { name: "First" });
    const second = screen.getByRole("button", { name: "Second" });
    expect(first).toHaveAttribute("aria-pressed", "true");
    expect(first).toHaveClass("active");
    expect(second).toHaveAttribute("aria-pressed", "false");
    expect(document.querySelector(".tabs .tab-spacer")).toBeInTheDocument();

    fireEvent.click(second);
    expect(onChange).toHaveBeenCalledWith("b");
  });

  it("wraps tables in a keyboard-scrollable shell", () => {
    render(
      <TableShell>
        <table>
          <tbody>
            <tr>
              <td>cell</td>
            </tr>
          </tbody>
        </table>
      </TableShell>,
    );

    const shell = screen.getByText("cell").closest(".table-shell");
    expect(shell).toHaveAttribute("tabindex", "0");
    expect(shell.querySelector("table")).toBeInTheDocument();
  });
});
