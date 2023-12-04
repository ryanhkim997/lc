import React, { useEffect, useState } from "react";

export function useKeyPress(key) {
  let [pressed, isPressed] = useState(false);

  useEffect(() => {
    const keyDownCallback = (e) => {
      e.stopPropagation();
      if (e.key === key) {
        isPressed(true);
      }
    };

    const keyUpCallback = (e) => {
      e.stopPropagation();
      if (e.key === key) {
        isPressed(false);
      }
    };

    window.addEventListener("keydown", keyDownCallback);
    window.addEventListener("keyup", keyUpCallback);

    return () => {
      window.removeEventListener("keydown", keyDownCallback);
      window.removeEventListener("keyup", keyUpCallback);
    };
  });
  return pressed;
}
