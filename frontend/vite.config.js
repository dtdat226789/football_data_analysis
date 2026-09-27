import { loadEnv } from "vite";
import { defineConfig } from "vitest/config";
import react from "@vitejs/plugin-react";

// The API port is configured in one place: API_PORT, read from frontend/.env or
// the environment. The default matches uvicorn's, so nothing changes unless you
// set it. Start the API with the matching port, e.g. `uvicorn ... --port 8010`.
export default defineConfig(({ mode }) => {
  const fileEnv = loadEnv(mode, process.cwd(), ["API_PORT"]);
  const apiPort = process.env.API_PORT || fileEnv.API_PORT || "8000";
  const target = `http://localhost:${apiPort}`;

  return {
    plugins: [react()],
    server: {
      port: 5173,
      proxy: {
        "/api": {
          target,
          changeOrigin: true,
        },
        "/health": {
          target,
          changeOrigin: true,
        },
      },
    },
    test: {
      environment: "jsdom",
      globals: true,
      setupFiles: "./src/test/setup.js",
    },
  };
});
