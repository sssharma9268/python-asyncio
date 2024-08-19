import asyncio

async def task(name,delay):
    print(f"Task {name} starting with delay of {delay}")
    await asyncio.sleep(delay)
    print(f"Task {name} finished")
    return f"Task {name} result"

async def main():
    tasks = [
        task("A",1),
        task("B",2),
        task("C",3)
    ]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

asyncio.run(main())

