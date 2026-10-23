import { Link } from "react-router-dom";

import { ErrorBox, TableSkeleton } from "./State.jsx";
import { TeamLink } from "./TeamLink.jsx";
import { useFormatters } from "../i18n/useFormatters.js";

/**
 * The finished-match table, shared by the matches page and a league's Matches tab.
 *
 * It was written out twice and the copies drifted: the league page had no empty
 * state at all, so an uncollected season rendered a bare table under its heading
 * and said nothing, and both skeletons were a column short of their own header.
 * Owning the header, the skeleton, the error and the empty row together is what
 * stops those from disagreeing again — the column count is derived from
 * `showLeague` instead of being typed in three more places.
 *
 * `state` is a `useApi` result (`{ data, loading, error }`). It is passed whole
 * rather than as three props so the skeleton, the error and the table can never
 * be rendered from different ideas of what the request is doing.
 *
 * @param {object} props
 * @param {any} props.state A `useApi` result.
 * @param {boolean} [props.showLeague]
 * @param {string} [props.emptyMessage] Overrides the default empty-state line.
 * @param {number} [props.skeletonRows]
 */
export default function MatchTable({ state, showLeague = false, emptyMessage, skeletonRows = 6 }) {
  const { t, plainDay } = useFormatters();
  const columns = showLeague ? 6 : 5;
  const rows = state?.data?.matches || [];

  return (
    <>
      {state?.loading && <TableSkeleton rows={skeletonRows} cols={columns} />}
      {state?.error && <ErrorBox error={state.error} />}
      {state?.data && (
        <table className="data">
          <thead>
            <tr>
              <th>{t("common.date")}</th>
              <th>{t("common.home")}</th>
              <th className="num">{t("common.score")}</th>
              <th>{t("common.away")}</th>
              {showLeague && <th>{t("common.league")}</th>}
              <th>{t("common.detail")}</th>
            </tr>
          </thead>
          <tbody>
            {rows.map((m) => (
              <tr key={m.api_id}>
                {/* A played match, so the stored calendar day is the day it was
                    played — not converted, unlike a kickoff. */}
                <td>{plainDay(m.match_date)}</td>
                <td>
                  <TeamLink name={m.home_team} />
                </td>
                <td className="num">
                  <strong>
                    {m.home_score} – {m.away_score}
                  </strong>
                </td>
                <td>
                  <TeamLink name={m.away_team} />
                </td>
                {showLeague && <td className="muted">{m.league_name || m.league}</td>}
                <td>
                  <Link className="link" to={`/match/${m.api_id}`}>
                    {t("common.view")}
                  </Link>
                </td>
              </tr>
            ))}
            {rows.length === 0 && (
              <tr>
                <td colSpan={columns} className="muted">
                  {emptyMessage || t("page.matches.noFinished")}
                </td>
              </tr>
            )}
          </tbody>
        </table>
      )}
    </>
  );
}