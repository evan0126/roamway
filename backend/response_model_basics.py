from pydantic import ValidationError

from models import TripOutput


def main():
    # 手动提供编号用于模型练习，这里尚未保存行程。
    trip = TripOutput(
        id=1,
        title="杭州一日游",
        destination="杭州",
        days=1,
        budget=300,
        daily_plans=[
            {
                "day": 1,
                "morning": "游西湖",
                "afternoon": "逛博物馆",
                "evening": "湖边散步",
            }
        ],
    )

    print("正常创建：")
    print(trip.model_dump())

    data = trip.model_dump()
    data["id"] = 0
    print("\n编号为 0：")
    try:
        TripOutput(**data)
    except ValidationError as e:
        # 捕获预期的校验错误，让后面的练习继续执行。
        print(e)
    else:
        raise AssertionError("编号为 0 时应校验失败")

    del data["id"]
    print("\n缺少编号：")
    try:
        TripOutput(**data)
    except ValidationError as e:
        print(e)
    else:
        raise AssertionError("缺少编号时应校验失败")

    print("\n原对象的编号仍然是：", trip.id)


if __name__ == "__main__":
    main()
