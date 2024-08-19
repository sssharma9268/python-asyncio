import asyncio

async def greet(name, delay):
    print(f"Greeting {name}")
    await asyncio.sleep(delay)
    print(f"hello {name}, after {delay} seconds!")

async def main():
    task1 = asyncio.create_task(greet("Alice",1))
    task2 = asyncio.create_task(greet("Bob",2))

    await task1
    await task2

asyncio.run(main())