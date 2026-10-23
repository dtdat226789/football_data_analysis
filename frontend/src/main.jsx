import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import App from "./App.jsx";
import { I18nProvider } from "./i18n/I18nProvider.jsx";
import { ROUTER_FUTURE } from "./routerFuture.js";
import "./index.css";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    {/* Outside the router: the settings controls in the topbar and the pages
        both read the language and the zone, and neither needs a route. */}
    <I18nProvider>
      <BrowserRouter future={ROUTER_FUTURE}>
        <App />
      </BrowserRouter>
    </I18nProvider>
  </React.StrictMode>,
);