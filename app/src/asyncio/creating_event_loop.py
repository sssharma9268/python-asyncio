import asyncio

async def my_coroutine():
    print("Coroutine started")
    await asyncio.sleep(1)
    print("Coroutine completed")


loop = asyncio.new_event_loop()
try:
    loop.run_until_complete(my_coroutine())
finally:
    loop.close()