import asyncio

async def fun():
    print("HELLO")
    return 0
async def sum():
    data = []

    await asyncio.sleep(5)
    for i in range(10000):
        data.append(i)
    return data
print(asyncio.run(sum()))
print(asyncio.run(fun()))
