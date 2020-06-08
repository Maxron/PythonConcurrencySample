import time
import asyncio
from asyncio import Task

now = lambda: time.time()


async def do_some_work(x):
    print("waiting: ", x)
    return "Done after {}s".format(x)


def callback(future: Task):
    print("callback: ", future.result())


if __name__ == '__main__':
    start = now()

    # Declare a coroutine but not execute
    coroutine = do_some_work(2)

    # Create a event loop
    loop = asyncio.get_event_loop()

    # Create Task from coroutine
    task = loop.create_task(coroutine)
    print(task)  # Pending task

    # Add callback
    task.add_done_callback(callback)
    print(task)

    # Add task to event loop
    loop.run_until_complete(task)
    print(task)  # Finished task

    print("Time: ", now() - start)
