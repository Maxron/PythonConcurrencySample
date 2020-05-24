import multiprocessing
import time
import random
from threading import current_thread

import rx
from rx import operators as ops
from rx.scheduler import ThreadPoolScheduler



def intense_calculation(value):
    # sleep for a random short duration between 0.5 to 2.0 seconds to simulate a long-running calculation
    time.sleep(random.randint(5, 20) * 0.1)
    return value


# calculate number of CPUs, then create a ThreadPoolScheduler with that number of threads
optimal_thread_count = multiprocessing.cpu_count()
pool_scheduler = ThreadPoolScheduler(optimal_thread_count)


def process_1():
    rx.of("Alpha", "Beta", "Gamma", "Delta", "Epsilon").pipe(
        ops.map(lambda s: intense_calculation(s)),
        ops.subscribe_on(pool_scheduler)
    ).subscribe(
        on_next=lambda s: print("PROCESS 1:{0} {1}".format(current_thread().name, s)),
        on_error=lambda e: print(e),
        on_completed=lambda: print("PROCESS 1 Done!")
    )


def process_2():
    rx.range(1, 10).pipe(
        ops.map(lambda s: intense_calculation(s)),
        ops.subscribe_on(pool_scheduler),
    ).subscribe(
        on_next=lambda i: print("PROCESS 2:{0} {1}".format(current_thread().name, i)),
        on_error=lambda e: print(e),
        on_completed=lambda: print("PROCESS 2 Done!")
    )


def process_3():
    rx.interval(1).pipe(
        ops.map(lambda i: i * 100),
        ops.observe_on(pool_scheduler),
        ops.map(lambda s: intense_calculation(s)),
    ).subscribe(
        on_next=lambda i: print("PROCESS 3: {0} {1}".format(current_thread().name, i)),
        on_error=lambda e: print(e),
    )

if __name__ == '__main__':
    process_1()
    process_2()
    process_3()
    input("Press any key to exit\n")

