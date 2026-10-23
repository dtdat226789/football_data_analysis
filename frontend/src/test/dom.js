/**
 * `querySelector`, `querySelectorAll` and `closest` are declared to return
 * `Element`, but almost every use in this suite is handed straight to
 * `within()`, or reads `.style` and `.textContent` off the result. Narrowing once
 * here is clearer than a cast at each of those sites.
 *
 * A `<HTMLElement>` type argument would be the other way to say this, but these
 * files are `.jsx`, where TypeScript reads `<T>` as the start of a JSX tag.
 */

/** @returns {NodeListOf<HTMLElement>} */
export const qsa = (root, selector) =>
  /** @type {NodeListOf<HTMLElement>} */ (root.querySelectorAll(selector));

/** @returns {HTMLElement | null} */
export const qs = (root, selector) => /** @type {HTMLElement | null} */ (root.querySelector(selector));

/** @returns {HTMLElement | null} */
export const closest = (element, selector) => /** @type {HTMLElement | null} */ (element.closest(selector));
