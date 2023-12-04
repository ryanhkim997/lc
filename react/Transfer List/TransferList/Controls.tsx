import React from "react";
import { RightArrow } from "./assets/RightArrow";
import { LeftArrow } from "./assets/LeftArrow";

export function Controls({ moveRight, moveLeft }) {
  return (
    <div className="flex flex-col">
      <div onClick={() => moveRight("right")}>
        <RightArrow />
      </div>
      <div onClick={() => moveLeft("left")}>
        <LeftArrow />
      </div>
    </div>
  );
}
