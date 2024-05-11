def call_counter(func):
    def counter(*args, **kwargs):
        counter.calls += 1
        with open("data.txt", "a") as f:
            f.write(f"Function '{func.__name__}' was called {counter.calls} times.\n")
        return func(*args, **kwargs)
    counter.calls = 0
    return counter


@call_counter
def add(a, b):
    return a + b


print(add(128, 10))


@call_counter
def subtr(a, b):
    return a - b


print(subtr(128, 10))
print(subtr(12, 4))
print(subtr(999, 1))
