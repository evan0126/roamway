"use client";

import { useState } from "react";

type TripPreviewProps = {
  destination: string;
  days: number;
  budget: number;
};

function TripPreview({
  destination,
  days,
  budget,
}: TripPreviewProps) {
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
  const [days, setDays] = useState(3);
  const [budget, setBudget] = useState(2000);

  return (
    <main>
      <h1>{title}</h1>

      <label>
        目的地：
        <input
          value={destination}
          onChange={(event) => setDestination(event.target.value)}
        />
      </label>

      <label>
        天数：
        <input
          value={days}
          onChange={(event) => setDays(Number(event.target.value))}
        />
      </label>

      <label>
        预算：
        <input
          value={budget}
          onChange={(event) => setBudget(Number(event.target.value))}
        />
      </label>

      <TripPreview destination={destination} days={days} budget={budget} />
    </main>
  );
}
