import React, { useEffect, useState, useRef } from 'react';
import CodeMirror from '@uiw/react-codemirror';
import { staticCode } from './sampleCode';

export default function TextGenerate() {
  const [isGenerating, setIsGenerating] = useState(false);
  const [code, setCode] = useState('');
  const intervalRef = useRef();

  const generate = function () {
    let i = 0;
    let generatedCode = '';
    intervalRef.current = setInterval(() => {
      if (!staticCode[i]) {
        clearInterval(intervalRef.current);
        setIsGenerating(false);
        i = 0;
      }
      generatedCode += staticCode[i];
      setCode(generatedCode);
      i++;
    }, 1);
  };

  useEffect(() => {
    if (isGenerating) {
      setTimeout(generate, 10);
    }

    return () => {};
  }, [isGenerating]);
  return (
    <div>
      <div className="container">
        <h1>Algochurn: Generate Text On The Go</h1>
        <div className="buttonsContainer">
          <button
            className="button"
            onClick={() => {
              if (isGenerating) {
                return;
              }
              setIsGenerating(true);
            }}
          >
            Start Generating
          </button>
          <button
            className="button"
            onClick={() => {
              setCode('');
              setIsGenerating(false);
              clearInterval(intervalRef.current);
            }}
          >
            Reset
          </button>
        </div>
        <div style={{ width: '100%' }}>
          <CodeMirror
            value={code}
            theme="dark"
            placeholder="// Click Start Generating to see magic"
            height="100%"
          />
        </div>
      </div>
    </div>
  );
}
