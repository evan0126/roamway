"use client";

import { useState } from "react";
import type { DailyPlan } from "@/data/trips";
import DailyPlanCard from "@/components/daily-plan-card";

type Props = {
  initialPlans: DailyPlan[];
};

export default function DailyPlansEditor({ initialPlans }: Props) {
  const [plans, setPlans] = useState(initialPlans);
  const [draftPlans, setDraftPlans] = useState(initialPlans);
  const [isEditing, setIsEditing] = useState(false);
  const [error, setError] = useState("");

  function handleEdit() {
    setDraftPlans(plans);
    setError("");
    setIsEditing(true);
  }

  function updatePlan(
    day: number,
    field: "morning" | "afternoon" | "evening",
    value: string,
  ) {
    // 只替换草稿中的目标对象，避免修改已确认的安排。
    setDraftPlans((currentPlans) =>
      currentPlans.map((plan) =>
        plan.day === day ? { ...plan, [field]: value } : plan,
      ),
    );
    setError("");
  }

  function handleConfirm() {
    const nextPlans = draftPlans.map((plan) => ({
      ...plan,
      morning: plan.morning.trim(),
      afternoon: plan.afternoon.trim(),
      evening: plan.evening.trim(),
    }));

    const invalidPlan = nextPlans.find(
      (plan) => !plan.morning || !plan.afternoon || !plan.evening,
    );

    if (invalidPlan) {
      setError(`请补全第 ${invalidPlan.day} 天的上午、下午和晚上安排`);
      return;
    }

    setPlans(nextPlans);
    setError("");
    setIsEditing(false);
  }

  function handleCancel() {
    setDraftPlans(plans);
    setError("");
    setIsEditing(false);
  }

  if (plans.length === 0) {
    return <p>暂无每日行程安排。</p>;
  }

  return (
    <div>
      {isEditing ? (
        <div>
          {draftPlans.map((plan) => (
            <section key={plan.day}>
              <h3>第 {plan.day} 天</h3>

              <label>
                上午：
                <input
                  value={plan.morning}
                  onChange={(event) =>
                    updatePlan(plan.day, "morning", event.target.value)
                  }
                />
              </label>

              <label>
                下午：
                <input
                  value={plan.afternoon}
                  onChange={(event) =>
                    updatePlan(plan.day, "afternoon", event.target.value)
                  }
                />
              </label>

              <label>
                晚上：
                <input
                  value={plan.evening}
                  onChange={(event) =>
                    updatePlan(plan.day, "evening", event.target.value)
                  }
                />
              </label>
            </section>
          ))}

          {error && <p role="alert">{error}</p>}

          <button type="button" onClick={handleConfirm}>
            确认
          </button>
          <button type="button" onClick={handleCancel}>
            取消
          </button>
        </div>
      ) : (
        <div>
          {plans.map((plan) => (
            <DailyPlanCard key={plan.day} plan={plan} />
          ))}

          <button type="button" onClick={handleEdit}>
            编辑每日安排
          </button>
        </div>
      )}
    </div>
  );
}