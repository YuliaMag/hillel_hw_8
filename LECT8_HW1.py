def skip_if(condition, reason):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not condition:
                return func(*args, **kwargs)
            else:
                print(reason)

        return wrapper

    return decorator


@skip_if(True, "Some reason...")
def test_one():
    assert 2 + 2 == 4
    print("Test one.")


test_one()
print("\n")

@skip_if(False, "Some reason...")
def test_two():
    assert 2 - 2 == 5
    # print("Test two.")


test_two()
