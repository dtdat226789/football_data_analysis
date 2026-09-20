export function FormPills({ results }) {
  if (!results || results.length === 0) return <span className="muted">—</span>;
  return (
    <span className="formline">
      {results.map((r, i) => (
        <span key={i} className={`pill ${r.team_result}`} title={`${r.home_team} ${r.home_score}-${r.away_score} ${r.away_team}`}>
          {r.team_result}
        </span>
      ))}
    </span>
  );
}