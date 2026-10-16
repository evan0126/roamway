# 从 trip.py 模块中，取出 create_trip 函数。 模块名不用写 .py
from trip import create_trip

def main():
    try:
        trip = create_trip("杭州", days=3, budget=3000)
        print(trip)
    except ValueError as e:
        print(f"创建失败：{e}")

# 含义："当前文件是不是本次程序直接启动的文件？」 如果是，就调用 main()
# 该判断可用于防止main导入的时候执行代码
if __name__ == "__main__":
    main()