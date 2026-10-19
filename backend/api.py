from models import TripInput

# 导入 FastAPI 类，用于创建接口应用。
from fastapi import FastAPI

# 创建应用实例；启动命令 api:app 中的 app 就是这个对象。
app = FastAPI()


# 注册 GET /health 路由，请求到达时由 FastAPI 调用下面的函数。
@app.get("/health")
def health() -> dict:
    # 健康检查用于确认服务能响应请求；字典会自动转换为 JSON 响应。
    return {"status": "ok"}


@app.post("/trips")
def create_trip(trip: TripInput) -> dict:
    # 请求体先经过校验；本节只返回数据，尚未保存行程。
    return trip.model_dump()