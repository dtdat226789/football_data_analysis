let activeSignal = null;

export function withRequestSignal(signal, loader) {
  const previous = activeSignal;
  activeSignal = signal;
  try {
    return loader();
  } finally {
    activeSignal = previous;
  }
}

export function currentRequestSignal() {
  return activeSignal;
}
