import time
import asyncio

now = lambda : time.time()


async def do_some_work(x):
    print("waiting: ", x)


if __name__ == '__main__':

    start = now()

    # Declare a coroutine but not execute
    coroutine = do_some_work(2)

    # Create a event loop
    loop = asyncio.get_event_loop()

    # Create Task from coroutine
    task = loop.create_task(coroutine)
    print(task) # Pending task

    # Add task to event loop
    loop.run_until_complete(task)
    print(task) # Finished task

    print("Time: ", now() - start)

