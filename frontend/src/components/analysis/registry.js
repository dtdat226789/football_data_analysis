import BarChart from "./BarChart.jsx";
import LineChart from "./LineChart.jsx";
import StackedBarChart from "./StackedBarChart.jsx";

const COMPONENTS = {
  bar: BarChart,
  stacked: StackedBarChart,
  line: LineChart,
};

export function chartComponent(kind) {
  return COMPONENTS[kind] ?? null;
}
