import asyncio

def callback(future):
    print(f"Callback received result: {future.result()}")

async def my_coroutine():
    await asyncio.sleep(1)
    return 42

loop = asyncio.new_event_loop()

try:
    coroutine = my_coroutine()
    future = asyncio.ensure_future(coroutine)
    future.add_done_callback(callback)
    loop.run_until_complete(future)
finally:
    loop.close()