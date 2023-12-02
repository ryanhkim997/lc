import * as React from 'react';
import LinkPreviewer from './LinkPreviewer';
import './style.css';

export default function App() {
  return (
    <div>
      <div className="container">
        <LinkPreviewer
          url={`https://api.microlink.io/?url=https%3A%2F%2Fgithub.com%2Fryanhkim997&screenshot=true&embed=screenshot.url`}
        >
          Github
        </LinkPreviewer>
      </div>
    </div>
  );
}
