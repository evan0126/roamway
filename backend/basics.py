print("--- 变量与输出 ---")
destination = "杭州"
days = 3
budget = 2000.5
need_hotel = True
remark = None

print(destination)
print(days)
print(budget)
print(need_hotel)
print(remark)
print(f"去{destination}玩{days}天，预算{budget}元")


print("\n--- 条件判断 ---")

if days <= 0:
    print("旅行天数必须大于零")
else:
    print(f"计划去{destination}玩{days}天")

if days <= 0:
    print("天数不合法")
elif days <= 3:
    print("适合短途旅行")
else:
    print("可以安排长途旅行")


print("\n--- 列表 ---")

places = ["西湖", "灵隐寺", "京杭大运河"]

print(places[0])
print(len(places))
places.append("西溪湿地")
print(f"景点数量：{len(places)}")

for place in places:
    print(f"计划游览：{place}")



print("\n--- 字典 ---")

trip = {
    "destination": "杭州",
    "days": 3,
    "budget": 2000,
}

print(trip["destination"])

trip["days"] = 5
trip["need_hotel"] = True

print(trip)

# remark（备注）可能不存在，使用 get() 安全读取
print(trip.get("remark", "暂无备注"))
print(trip.get("remark")) # 键不存在，返回 None
# print(trip["remark"])  # 键不存在，抛出 KeyError


print("\n--- 遍历字典 ---")

trip["remark"] = "尽量安排轻松一些"
for key, value in trip.items():
    print(f"{key}：{value}")



print("\n--- 函数 ---")

def show_trip(destination, days):
    print(f"去{destination}玩{days}天")

show_trip("杭州", 3)
show_trip("成都", 5)



print("\n--- 返回值、默认参数 ---")

def create_trip(destination, days=2, budget=2000):
    return {
        "destination": destination,
        "days": days,
        "budget": budget
    }

trip = create_trip("杭州", 3, 5000)
trip2 = create_trip("成都", 5)
trip3 = create_trip("成都", budget=3000)

print(trip)
print(trip2)
print(trip3)



print("\n--- 类型标注 ---")

# 完整形式：def 函数名(参数名: 类型 = 默认值) -> 返回类型:
#     return 返回值
# 返回类型：str 字符串，dict 字典；无默认值的参数放在前面。
def create_trip(
    destination: str,
    days: int = 3,
    budget: float = 2000,
) -> dict:
    if days <= 0:
        raise ValueError("旅行天数必须大于零")
    return {
        "destination": destination,
        "days": days,
        "budget": budget,
    }


trip = create_trip("杭州", budget=3000)
print(trip)




print("\n--- 异常处理 ---")

# 0 触发值错误，字符串触发类型错误，3 正常返回。
for days in [0, "三天", 3]:
    try:
        trip = create_trip("杭州", days)
        print(trip)
    except ValueError as e:
        print(f"值错误：{e}")
    except TypeError as e:
        print(f"类型错误：{e}")