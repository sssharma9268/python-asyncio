[![Python application](https://github.com/sssharma9268/python-asyncio/actions/workflows/python-app.yml/badge.svg)](https://github.com/sssharma9268/python-asyncio/actions/workflows/python-app.yml)



- Understanding the Event Loop:
1. The Event loop is a fundamental concept in asynchronous programming. It is a central piece that coordinates and manages the execution of asynchronous tasks, ensuring that they run efficiently and without blocking the main program flow.
2. It is a programming construct that continously monitors and process events from various sources, such as user input, network requests, or timer events. It acts as a central hub that dispatches these events to the appropriate event handlers or callbacks.

-Event Loop in Action:
1. The asyncio.run function creates an event loop and runs the given coroutine, also handles the cleanup of resources and event loop closing.
2. The given coroutine creates instances of the given sub-task coroutines and awaits their completion using asyncio.gather.
3. The event loop manages the execution of these tasks, scheduling them and switching them and switching between them as needed.

- Event Loop Responsibilities:
1. Scheduling and executing async tasks (coroutines).
2. Handling I/O operations (e.g., network, file I/O).
3. Managing timeouts and delays.
4. Dispatching events to appropriate callbacks or handlers.

- Event Loop and Concurrency
1. It enables concurrency by allowing multiple async tasks to run simultaneously without blocking the main thread.
2. This is achieved through coperative multitasking, where tasks voluntarily yield control back to the event loop when they encounter an awaitable operation.
3. Asyncio uses a single-threaded event loop to manage tasks, while multi-threading uses multiple threads.

- Coroutines
1. A coroutine is a special type of function defined using the async keyword.
2. Coroutines can be suspended and resumed, allowing for concurrent execution.
3. The await keyword is used within coroutines to await the result of an async operation.

- Running Async Code with Callbacks
1. In some cases, you may want to run an asynchronous operation and receive the result in a callback function.
2. The async.ensure_future function schedules the coroutine for execution and returns a Future object.
3. The add_done_callback method on the Future object allows you to register a callback function to be called when the coroutine completes.