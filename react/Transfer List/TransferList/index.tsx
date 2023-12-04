import React, { useState, useEffect } from "react";
import { data } from "../TransferList/data";
import { Controls } from "./Controls";

export const TransferList = () => {
  const [sampleData, setSampleData] = useState(data);
  const [leftData, setLeftData] = useState<any[]>(sampleData);
  const [rightData, setRightData] = useState<any[]>([]);

  function checkItem(item, column) {
    const listToCheck = column === "left" ? leftData : rightData;
    const listObj = listToCheck.map((li) => {
      if (li.id === item.id) {
        li.checked = !li.checked;
      }
      return li;
    });

    if (column === "left") {
      setLeftData(listObj);
    } else {
      setRightData(listObj);
    }
  }

  function moveItems(column) {
    let leftItems = leftData;
    let rightItems = rightData;
    if (column === "left") {
      rightItems = rightData.filter(({ checked }) => !checked);
      rightData.forEach((item) => {
        if (item.checked) {
          item.checked = false;
          leftItems.push(item);
        }
      });
    } else {
      leftItems = leftData.filter(({ checked }) => !checked);
      leftData.forEach((item) => {
        if (item.checked) {
          item.checked = false;
          rightItems.push(item);
        }
      });
    }
    setLeftData(leftItems);
    setRightData(rightItems);
  }

  return (
    <div className="flex flex-row justify-center align-center">
      <ul>
        {leftData.map((li) => {
          return (
            <li
              className={`${
                li.checked && "bg-black text-white"
              } hover:cursor-pointer`}
              onClick={() => checkItem(li, "left")}
            >
              <span>{li.title}</span>
            </li>
          );
        })}
      </ul>
      <Controls
        moveRight={(right) => moveItems(right)}
        moveLeft={(left) => moveItems(left)}
      />
      <ul>
        {rightData.map((li) => (
          <li
            className={`${
              li.checked && "bg-black text-white"
            } hover:cursor-pointer`}
            onClick={() => checkItem(li, "right")}
          >
            <span>{li.title}</span>
          </li>
        ))}
      </ul>
    </div>
  );
};
