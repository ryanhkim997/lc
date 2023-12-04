import React, { Fragment, useState } from "react";
import Icon from "./Icon";
import { File } from "./File";

const Folder = ({ files }) => {
  const [showContents, setShowContents] = useState(false);
  console.log(files);
  return (
    <div className="indented">
      <div className="file-name" onClick={() => setShowContents(!showContents)}>
        <Icon name={showContents ? "caretDown" : "caretRight"} width="12px" />
        <span>{files.name}</span>
      </div>
      {showContents &&
        files.children.map((child) =>
          child.isFolder ? <Folder files={child} /> : <File data={child} />
        )}
    </div>
  );
};

export default Folder;
