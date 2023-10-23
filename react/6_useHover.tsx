import { Ref, useRef, useEffect, useState } from 'react';

export function useHover(): [React.RefObject<any>, boolean] {
  const divRef = useRef();
  const [hover, toggleHover] = useState(false);
  
  const handleMouseEnter = (): void => { toggleHover(true) }
  const handleMouseLeave = (): void => { toggleHover(false) }

  useEffect(() => {
    const curr = divRef.current;

    if (curr) {
      curr.addEventListener('mouseover', handleMouseEnter);
      curr.addEventListener('mouseout', handleMouseLeave);
    }

    return () => {
        if (curr) {
          curr.removeEventListener('mouseover', handleMouseEnter);
          curr.removeEventListener('mouseout', handleMouseLeave);
        }
    }
    
  }, [divRef.current])


  return [divRef, hover];
}