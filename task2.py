# Напишіть декоратор, який буде заміряти час виконання для наданої функції.

import time


def execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f"Час виконання: {duration} секунд")
        return result
    return wrapper


@execution_time
def hello_by_name(name):
    return f"Hello, {name}! " * 1000


print(hello_by_name("Alex"))