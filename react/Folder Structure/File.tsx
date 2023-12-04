import React from "react";
import Icon from "./Icon";

export function File({ data }) {
  return (
    <div className="indented file-name">
      <Icon width="12px" name={`${data?.name.split(".")[1]}`} />
      <span>{data?.name}</span>
    </div>
  );
}
