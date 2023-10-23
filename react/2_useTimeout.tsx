import { useRef, useEffect } from "react";

export function useTimeout(callback: () => void, delay: number) {
  const timerRef = useRef(null);

  useEffect(() => {
    if (timerRef.current) {
      clearTimeout(timerRef.current);
    }

    timerRef.current = setTimeout(callback, delay);

    return () => {
      if (timerRef.current) {
        clearTimeout(timerRef.current);
      }
    }
  }, [delay])

  return () => {
    if (timerRef.current) {
      clearTimeout(timerRef.current)
    }
  }
}