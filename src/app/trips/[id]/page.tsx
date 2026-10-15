import { notFound } from "next/navigation";

const trips = [
  {
    id: "1",
    title: "杭州三日游",
    content: "这是一个关于杭州三日游的详细行程安排。",
  },
  {
    id: "2",
    title: "成都五日游",
    content: "这是一个关于成都五日游的详细行程安排。",
  },
];

export default async function TripDetailPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;

  const trip = trips.find((item) => item.id === id);

  // 地址中的编号可能不存在，交给 Next.js 展示 404 页面。
  if (!trip) {
    notFound();
  }

  return (
    <main>
      <h1>{trip.title}</h1>
      <p>行程编号：{trip.id}</p>
      <p>{trip.content}</p>
    </main>
  );
}
