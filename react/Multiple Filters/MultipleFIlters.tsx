import React, { useEffect, useState } from "react";
import { items as defaultItems } from "./items";
import "./style.css";

export default function MultipleFilters() {
  const [items, setItems] = useState(defaultItems);
  const [activeFilters, setActiveFilters] = useState<any[]>([]);

  function handleClick(filter) {
    if (activeFilters.includes(filter)) {
      const filters = activeFilters.filter((e) => e !== filter);
      setActiveFilters(filters);
    } else {
      setActiveFilters((prevState) => [...prevState, filter]);
    }
  }

  function handleFilter() {
    if (activeFilters.length < 1) {
      setItems(defaultItems);
    } else {
      const filteredItems: any[] = [];
      activeFilters.forEach((filter) => {
        defaultItems.forEach((item) => {
          if (item.category === filter) {
            filteredItems.push(item);
          }
        });
      });
      console.log(filteredItems);
      setItems(filteredItems);
    }
  }

  useEffect(() => {
    handleFilter();
  }, [activeFilters]);

  let filters = ["Bags", "Watches", "Sports", "Sunglasses"];

  return (
    <div>
      <h2 style={{ textAlign: "center" }}>Algochurn Filters</h2>
      <div className="buttons-container">
        {filters.map((filter, idx) => (
          <button
            className={`button ${activeFilters.includes(filter) && "active"}`}
            key={`filters-${idx}`}
            onClick={() => {
              handleClick(filter);
            }}
          >
            {filter}
          </button>
        ))}
      </div>
      <div className="items-container">
        {items.map((item, idx) => (
          <div key={`items-${idx}`} className="item">
            <p>{item.name}</p>
            <p className="category">{item.category}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
