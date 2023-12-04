import * as React from "react";
import { files } from "./data";
import Folder from "./Folder";
import "./style.css";

export default function App() {
  return (
    <div>
      <div className="container">
        <Folder files={files} />
      </div>
    </div>
  );
}
