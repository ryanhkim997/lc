import React, { useState } from 'react';

export function Input({ label, value, setField }) {
  const [inputVal, setInputVal] = useState('');

  function handleChange(e) {
    // setInputVal(e.target.value);
    setField(e.target.value);
  }

  return (
    <div>
      <label>{label}</label>
      <input required type="text" value={value} onChange={handleChange} />
    </div>
  );
}
