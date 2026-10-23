/**
 * React Router v7 opt-ins, shared by the app and the test harness.
 *
 * Declared once so the app and the tests resolve routes identically — a flag set
 * in only one of the two means the tests pass against a router the app does not
 * run. Both warnings were printed on every single test run, which is the kind of
 * noise that trains people to ignore the log.
 */
export const ROUTER_FUTURE = {
  v7_startTransition: true,
  v7_relativeSplatPath: true,
};
