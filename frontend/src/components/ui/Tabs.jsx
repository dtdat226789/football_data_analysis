/**
 * @param {{ items: { key: string, label: import("react").ReactNode, disabled?: boolean }[],
 *   active?: string, onChange: (key: string) => void,
 *   trailing?: import("react").ReactNode, label?: string }} props
 */
export default function Tabs({ items, active, onChange, trailing, label }) {
  return (
    <div className="tabs" role="group" aria-label={label}>
      {items.map((item) => (
        <button
          key={item.key}
          type="button"
          className={item.key === active ? "active" : undefined}
          aria-pressed={item.key === active}
          disabled={item.disabled}
          onClick={() => onChange(item.key)}
        >
          {item.label}
        </button>
      ))}
      {trailing}
    </div>
  );
}
