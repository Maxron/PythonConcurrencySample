import time
import asyncio
from asyncio import Task

now = lambda: time.time()


async def do_some_work(x):
    print("waiting: ", x)
    await asyncio.sleep(x)  # Blocking
    return "Done after {}s".format(x)


def callback(future: Task):
    print("callback: ", future.result())


async def main():
    coroutine1 = do_some_work(4)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(1)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]

    for task in asyncio.as_completed(tasks):
        result = await task
        print("Task ret: {}".format(result))


if __name__ == '__main__':
    start = now()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    print("Time: ", now() - start)
