import type { DailyPlan } from "@/data/trips";
type Props = {
  plan: DailyPlan;
};
export default function DailyPlanCard({ plan }: Props) {
  return (
    <section>
      <h3>第 {plan.day} 天</h3>
      <p>上午：{plan.morning}</p>
      <p>下午：{plan.afternoon}</p>
      <p>晚上：{plan.evening}</p>
    </section>
  );
}