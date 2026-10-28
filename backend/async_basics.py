import asyncio


async def get_destination() -> str:
    print("2. 开始读取目的地")

    # 模拟异步等待；等待期间允许事件循环处理其他已调度任务。
    await asyncio.sleep(1)

    print("3. 读取完成")
    return "杭州"


async def main():
    print("1. 开始")

    result = await get_destination()

    print("4. 结果：", result)


if __name__ == "__main__":
    asyncio.run(main())

# --------------------------------------------

async def generate_trip():
    print("开始生成行程")
    await asyncio.sleep(4)  # 模拟等待模型返回。
    print("行程生成完成")


async def show_progress():
    for i in range(3):
        await asyncio.sleep(1)
        print(f"正在等待……  {i+1}s")


async def main():
    await asyncio.gather(
        generate_trip(),
        show_progress(),
    )


if __name__ == "__main__":
    asyncio.run(main())