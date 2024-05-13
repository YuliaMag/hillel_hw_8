# import os


def call_counter(path):
    # path = Path("data.txt")
    # path = os.path.join(path)

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


@call_counter("test.txt")
def subtr(a, b):
    return a - b


print(subtr(128, 10))
print(subtr(999, 1))
