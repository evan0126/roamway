print(f"trip 模块被加载了，当前模块名称：{__name__}")

def create_trip(
    destination: str,
    days: int = 3,
    budget: float = 2000,
) -> dict:
    print("创建行程")
    # 非法天数直接报错，由调用方决定如何提示。
    if days <= 0:
        raise ValueError("旅行天数必须大于零")

    return {
        "destination": destination,
        "days": days,
        "budget": budget,
    }