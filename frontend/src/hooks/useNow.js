import { useSyncExternalStore } from "react";

const listeners = new Set();
let snapshot = Date.now();
let timer = null;

function tick() {
  snapshot = Date.now();
  for (const listener of [...listeners]) listener();
}

function subscribe(listener) {
  snapshot = Date.now();
  listeners.add(listener);
  if (timer === null) {
    timer = setInterval(tick, 1000);
  }
  return () => {
    listeners.delete(listener);
    if (listeners.size === 0 && timer !== null) {
      clearInterval(timer);
      timer = null;
    }
  };
}

function getSnapshot() {
  return snapshot;
}

export function useNow() {
  return useSyncExternalStore(subscribe, getSnapshot, getSnapshot);
}
