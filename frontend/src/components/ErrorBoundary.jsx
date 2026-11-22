import { Component } from "react";

import { useI18n } from "../i18n/I18nProvider.jsx";

function ErrorFallback({ reset }) {
  const { t } = useI18n();
  return (
    <div className="error-box" role="alert">
      <strong>{t("page.error.title")}</strong>
      <span> — {t("page.error.hint")}</span>{" "}
      <button type="button" className="link-button" onClick={reset}>
        {t("common.reload")}
      </button>
    </div>
  );
}

export default class ErrorBoundary extends Component {
  state = { error: null };

  static getDerivedStateFromError(error) {
    return { error };
  }

  componentDidCatch(error, info) {
    console.error("UI render error", error, info);
  }

  render() {
    if (this.state.error) {
      return <ErrorFallback reset={() => this.setState({ error: null })} />;
    }
    return this.props.children;
  }
}
