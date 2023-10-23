import { useRef } from "react";

export function usePrevious<T>(value: T): T | undefined {
  const prevRef = useRef(undefined);

  const previous = prevRef.current;
  prevRef.current = value;

  return previous;
}