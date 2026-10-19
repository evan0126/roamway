import { notFound } from "next/navigation";
import { trips } from "@/data/trips";
import DailyPlanCard from "@/components/daily-plan-card";
import TripTitleEditor from "@/components/trip-title-editor";
import DailyPlansEditor from "@/components/daily-plans-editor";

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
      <TripTitleEditor key={trip.id} initialTitle={trip.title} />
      <p>行程编号：{trip.id}</p>
      <p>{trip.content}</p>
      <h2>每日行程安排</h2>
      <DailyPlansEditor initialPlans={trip.dailyPlans} />
    </main>
  );
}
