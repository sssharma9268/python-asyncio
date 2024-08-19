import asyncio

async def my_coroutine(number):
    print(f"Started coroutine with number: {number}")
    await asyncio.sleep(1)
    print(f"Finished coroutine with number: {number}")
    return number ** 2


async def main():
    numbers = [1,2,3,4,5]
    squared_numbers = [await my_coroutine(n) for n in numbers]
    print(squared_numbers)

asyncio.run(main())