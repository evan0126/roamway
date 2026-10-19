from pydantic import BaseModel, Field, model_validator


# 表示一天的安排。
class DailyPlan(BaseModel):
    day: int = Field(gt=0)
    morning: str = Field(min_length=1)
    afternoon: str = Field(min_length=1)
    evening: str = Field(min_length=1)


class TripInput(BaseModel):
    title: str = Field(min_length=1)
    destination: str = Field(min_length=1)
    days: int = Field(gt=0)
    budget: float = Field(ge=0, allow_inf_nan=False)

    # 至少一条安排，每条都按 DailyPlan 校验。
    daily_plans: list[DailyPlan] = Field(min_length=1)
    
    @model_validator(mode="after")
    def validate_daily_plans(self) -> "TripInput":
        # 先检查安排数量是否与旅行天数一致。
        if len(self.daily_plans) != self.days:
            raise ValueError("每日安排数量必须与旅行天数一致")

        actual_days = [plan.day for plan in self.daily_plans]
        expected_days = list(range(1, self.days + 1))

        # 比较编号和顺序，避免重复、跳号或越界。
        if actual_days != expected_days:
            raise ValueError("每日安排必须按第 1 天到最后一天依次排列")

        # 校验成功后，返回当前模型对象。
        return self
    