import React, { useState, useEffect } from "react";

export const ColorCodes = () => {
  const [targetHex, setTargetHex] = useState("");
  const [hexes, setHexes] = useState([]);
  const [currentGuess, setCurrentGuess] = useState(null);

  function generateHex() {
    let hexString = "#";
    const hexVals = [
      "0",
      "1",
      "2",
      "3",
      "4",
      "5",
      "6",
      "7",
      "8",
      "9",
      "a",
      "b",
      "c",
      "d",
      "e",
      "f"
    ];

    for (let i = 0; i < 6; i++) {
      hexString += hexVals[Math.floor(Math.random() * 16)];
    }

    return hexString;
  }

  function resetGame() {
    const generatedHexes = [generateHex(), generateHex(), generateHex()];
    setHexes(generatedHexes);
    setTargetHex(generatedHexes[Math.floor(Math.random() * 3)]);
    setCurrentGuess(null);
  }

  function handleColorClick(hex) {
    if (hex === targetHex) {
      setCurrentGuess("correct");
    } else {
      setCurrentGuess("incorrect");
    }
  }

  function handleButtonClick() {
    resetGame();
  }

  useEffect(() => {
    resetGame();
  }, []);

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center"
      }}
    >
      <h1>Color Codes</h1>
      {/* Randomly generate the HEX below. */}
      <h2>{targetHex}</h2>
      <h2>What color is this?</h2>

      <div data-testid="color-container" style={{ display: "flex" }}>
        {hexes.map((hex, i) => {
          return (
            <div
              key={`${hex}-${i}`}
              data-testid={
                hex === targetHex ? "correct-color" : "incorrect-color"
              }
              style={{ backgroundColor: hex, width: "100px", height: "100px" }}
              onClick={() => handleColorClick(hex)}
            />
          );
        })}
      </div>
      {currentGuess && (
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center"
          }}
        >
          {currentGuess === "correct" ? <h2>Correct!</h2> : <h2>Incorrect!</h2>}
          <button onClick={handleButtonClick}>Play Again</button>
        </div>
      )}
    </div>
  );
};
