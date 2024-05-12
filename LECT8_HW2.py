from pathlib import Path


def call_counter(path):
    path = Path("data.txt")

    def wrapper(func):
        def counter(*args, **kwargs):
            counter.calls += 1
            with open(path, "a") as f:
                f.write(f"Function '{func.__name__}' was called {counter.calls} times.\n")
            return func(*args, **kwargs)
        counter.calls = 0
        return counter

    return wrapper


@call_counter("data.txt")
def add(a, b):
    return a + b


print(add(128, 10))


@call_counter("data.txt")
def subtr(a, b):
    return a - b


print(subtr(128, 10))
print(subtr(999, 1))
