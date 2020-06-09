import time
import asyncio
from asyncio import Task

now = lambda: time.time()


async def do_some_work(x):
    print("waiting: ", x)
    await asyncio.sleep(x) # Blocking
    return "Done after {}s".format(x)


def callback(future: Task):
    print("callback: ", future.result())


if __name__ == '__main__':
    start = now()

    coroutine1 = do_some_work(4)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(1)

    task1 = asyncio.ensure_future(coroutine1)
    task1.add_done_callback(callback)

    task2 = asyncio.ensure_future(coroutine2)
    task2.add_done_callback(callback)

    task3 = asyncio.ensure_future(coroutine3)
    task3.add_done_callback(callback)

    tasks = [task1, task2, task3]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(task1, task2, task3))

    for task in tasks:
        print("Task ret:", task.result())

    print("Time: ", now() - start)
