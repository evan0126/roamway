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
  return (
    <main>
      <h1>{title}</h1>
      <TripPreview destination="成都" days={3} budget={2000} />
    </main>
  );
}
