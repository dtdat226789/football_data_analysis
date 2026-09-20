import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import App from "./App.jsx";
import { LeaguesProvider } from "./state/LeaguesContext.jsx";
import "./index.css";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <BrowserRouter>
      <LeaguesProvider>
        <App />
      </LeaguesProvider>
    </BrowserRouter>
  </React.StrictMode>,
);