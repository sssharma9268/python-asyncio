import asyncio

async def task():
    print("Task started")
    await asyncio.sleep(1)
    print("Task completed")

async def main():
    """
    1. The asyncio.run function creates an event loop and runs the main coroutine.
    2. The main coroutine creates 3 instances of the task coroutine and awaits their completion using asyncio.gather.
    3. The event loop manages the execution of these tasks, scheduling them and switching them and switching between them as needed.
    """
    await asyncio.gather(task(),task(),task())


if __name__ == "__main__":
    asyncio.run(main())