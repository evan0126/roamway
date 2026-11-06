import random

from mock_data import trip_samples
from models import TripInput, TripOutput

# 导入 FastAPI 类，用于创建接口应用。
from fastapi import FastAPI, HTTPException

# 创建应用实例；启动命令 api:app 中的 app 就是这个对象。
app = FastAPI()

trips: dict[int, TripOutput] = {}
next_trip_id = 1


# 注册 GET /health 路由，请求到达时由 FastAPI 调用下面的函数。
@app.get("/health")
def health() -> dict:
    # 健康检查用于确认服务能响应请求；字典会自动转换为 JSON 响应。
    return {"status": "ok"}


# 无需请求体，从 mock 数据随机抽取行程，保存后返回带编号的行程。
@app.post("/trips", response_model=TripOutput)
def create_trip() -> TripOutput:
    # global next_trip_id 表示函数中要修改的是函数外的编号变量
    global next_trip_id

    # 将随机抽取的字典转换为输入模型，执行字段校验。
    trip = TripInput(**random.choice(trip_samples))

    # 将校验后的行程与服务端生成的编号组合成输出对象。
    saved_trip = TripOutput(
        id=next_trip_id,
        **trip.model_dump(),
    )

    # 保存行程，并为下一次创建准备编号。
    trips[saved_trip.id] = saved_trip
    next_trip_id += 1

    return saved_trip


# 注册 GET /trips 路由，返回所有行程列表。
@app.get("/trips", response_model=list[TripOutput])
def list_trips() -> list[TripOutput]:
    return list(trips.values())


# 注册 GET /trips/{trip_id} 路由，返回指定编号的行程。
@app.get("/trips/{trip_id}", response_model=TripOutput)
def get_trip(trip_id: int) -> TripOutput:
    trip = trips.get(trip_id)

    if trip is None:
        raise HTTPException(status_code=404, detail="行程不存在")

    return trip
