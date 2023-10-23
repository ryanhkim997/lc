import React, { useState } from 'react'

export function App() {
  const [counter, setCounter] = useState(0);
  return (
    <div>
      <button onClick={() => setCounter(counter - 1)} data-testid="decrement-button">-</button>
      <button onClick={() => setCounter(counter + 1)} data-testid="increment-button">+</button>
      <p>clicked: {counter}</p>
    </div>
  )
}