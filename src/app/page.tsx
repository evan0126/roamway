"use client";

import { useState } from "react";

type TripPreviewProps = {
  destination: string;
  days: number | null;
  budget: number;
};

function TripPreview({ destination, days, budget }: TripPreviewProps) {
  return (
    <section>
      <h2>旅行需求预览</h2>
      <p>目的地：{destination}</p>
      <p>旅行天数：{days} 天</p>
      <p>预算：{budget} 元</p>
    </section>
  );
}

export default function Home() {
  const title = "旅行助手";
  const [destination, setDestination] = useState("成都");
  const [days, setDays] = useState("3");
  const [budget, setBudget] = useState(2000);

  const destinationError = destination.trim() === "" ? "请输入目的地" : "";
  // 保留原始输入以支持清空，校验通过后才向预览传递数字。
  const parsedDays = Number(days);
  const daysError =
    days.trim() !== "" && Number.isInteger(parsedDays) && parsedDays > 0
      ? ""
      : "旅行天数必须是正整数";
  const budgetError = budget <= 0 ? "请输入有效的预算" : "";

  return (
    <main>
      <h1>{title}</h1>

      <label>
        目的地：
        <input
          value={destination}
          onChange={(event) => setDestination(event.target.value)}
        />
        {destinationError && <p role="alert">{destinationError}</p>}
      </label>

      <label>
        天数：
        <input
          value={days}
          onChange={(event) => setDays(event.target.value)}
        />
        {daysError && <p role="alert">{daysError}</p>}
      </label>

      <label>
        预算：
        <input
          value={budget}
          onChange={(event) => setBudget(Number(event.target.value))}
        />
        {budgetError && <p role="alert">{budgetError}</p>}
      </label>

      <TripPreview
        destination={destination}
        days={daysError ? null : parsedDays}
        budget={budget}
      />
    </main>
  );
}
