import time
import asyncio
from threading import Thread

now = lambda: time.time()


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


def more_work(x):
    print('More work:', x)
    time.sleep(x)
    print('Finished more work:', x)


async def do_some_work(x):
    print('Waiting {}'.format(x))
    await asyncio.sleep(x)
    print('Done after {}s'.format(x))


if __name__ == '__main__':
    start = now()
    new_loop = asyncio.new_event_loop()
    thread = Thread(target=start_loop, args=(new_loop,))
    thread.start()
    print("TIME: {}".format(time.time() - start))

    # new_loop.call_soon_threadsafe(more_work, 4)
    # new_loop.call_soon_threadsafe(more_work, 3)

    asyncio.run_coroutine_threadsafe(do_some_work(5), new_loop)
    asyncio.run_coroutine_threadsafe(do_some_work(2), new_loop)
