import rx
from rx import of, operators
from rx.core.typing import Observer

source = of('Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon')

def show_subscribe():
    source.subscribe(
        on_next=lambda i: print("Received {0}".format(i)),
        on_error=lambda e: print("Error Occured: {0}".format(e)),
        on_completed=lambda: print("Done!")
    )

    source.subscribe(
        lambda value: print("Received {0}".format(value))
    )


def show_composed():
    composed = source.pipe(
        operators.map(lambda s: len(s)),
        operators.filter(lambda i: i >= 5)
    )
    composed.subscribe(lambda value: print("Received {0}".format(value)))


def show_chain():
    of('Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon').pipe(
        operators.map(lambda s: len(s)),
        operators.filter(lambda i: i <= 5)
    ).subscribe(
        lambda value: print("Received {0}".format(value))
    )


def length_more_than_5():
    return rx.pipe(
        operators.map(lambda s: len(s)),
        operators.filter(lambda i: i <= 5)
    )


def custom_operator():
    source.pipe(length_more_than_5()).subscribe(
        lambda value: print("Received {0}".format(value))
    )


def lowercase():
    def _lowercase(source: rx.Observable):
        def subscribe(observer: Observer, scheduler=None):
            def on_next(value):
                observer.on_next(value.lower())

            return source.subscribe(
                on_next,
                observer.on_error,
                observer.on_completed,
                scheduler
            )

        return rx.create(subscribe)

    return _lowercase


def custom_operator2():
    source.pipe(lowercase()).subscribe(
        lambda value: print("Received {0}".format(value))
    )


def my_test_observable():
    def _my_observalbe(observer, scheduler):
        observer.on_next("Hello")
        observer.on_next("World")
        observer.on_completed()
    return rx.create(_my_observalbe)


def my_test():
    my_test_observable().subscribe(
        on_next=lambda value: print("value:{}".format(value)),
        on_completed=lambda: print("completed")
    )


if __name__ == '__main__':
    # show_subscribe()
    # show_composed()
    # show_chain()
    # custom_operator()
    # custom_operator2()
    my_test()
