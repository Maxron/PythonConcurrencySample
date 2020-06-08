import time
import asyncio

now = lambda : time.time()


async def do_some_work(x):
    print("waiting: ", x)


if __name__ == '__main__':

    start = now()

    # Declare a coroutine but not execute
    coroutine = do_some_work(2)
    print(coroutine)

    # Create a event loop
    loop = asyncio.get_event_loop()

    # Add coroutine to event loop
    loop.run_until_complete(coroutine)

    print("Time: ", now() - start)

