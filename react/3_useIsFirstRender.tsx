import { useRef, useEffect } from 'react'

export function useIsFirstRender(): boolean {
  const renderRef = useRef(false);

  useEffect(() => {
    if (!renderRef.current) {
      renderRef.current = true;
    }
  }, [])

  if (renderRef.current) {
    return false;
  } else {
    return true;
  }
}