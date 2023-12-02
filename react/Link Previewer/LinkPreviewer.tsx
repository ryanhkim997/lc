import React, { useState } from 'react';
import './style.css';

export default function LinkPreviewer({ url, children }) {
  // Write your code here
  // Documentation on how to screenshot any website:
  // https://microlink.io/screenshot
  const [isPreviewShowing, setIsPreviewShowing] = useState(false);

  return (
    <div style={{ display: 'relative' }}>
      Check out my
      {isPreviewShowing && <img className="preview" src={url} />}
      <span
        className="children"
        onMouseEnter={() => setIsPreviewShowing(true)}
        onMouseLeave={() => setIsPreviewShowing(false)}
      >
        {children}
      </span>
      profile
    </div>
  );
}
