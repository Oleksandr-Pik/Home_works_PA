# Напишіть декоратор, який буде заміряти час виконання для наданої функції.

import time


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(time.time() - start)
        return result

    return wrapper


@time_decorator
def hello_by_name(name):
    return f"Hello, {name}! " * 1000


print(hello_by_name("Alex"))