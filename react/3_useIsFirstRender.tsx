import { useRef, useEffect } from 'react'

export function useIsFirstRender(): boolean {
  const renderRef = useRef(true);
  
  if (renderRef.current) {
    return true;
  }

  return false;
}