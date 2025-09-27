import time
from functools import lru_cache

def execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f"\n Час виконання: {duration} секунд")
        return result
    return wrapper


def fib_no_cache(n):
    if n <= 1:
        return n
    return fib_no_cache(n - 1) + fib_no_cache(n - 2)


fib_cache = {}
def fib_custom_cache(n):
    if n in fib_cache:
        return fib_cache[n]
    if n <= 1:
        fib_cache[n] = n
    else:
        fib_cache[n] = fib_custom_cache(n - 1) + fib_custom_cache(n - 2)
    return fib_cache[n]


@lru_cache(maxsize=10)
def fib_lru_10(n):
    if n <= 1:
        return n
    return fib_lru_10(n - 1) + fib_lru_10(n - 2)


@lru_cache(maxsize=16)
def fib_lru_16(n):
    if n <= 1:
        return n
    return fib_lru_16(n - 1) + fib_lru_16(n - 2)


@execution_time
def run_fib_sequence(fib_func, label):
    print(f"\n {label}")
    for i in range(25):
        print(fib_func(i), end=' ')


run_fib_sequence(fib_no_cache, "Без кешу")
run_fib_sequence(fib_custom_cache, "З кешем довільної довжини")
run_fib_sequence(fib_lru_10, "З functools кешем (maxsize=10)")
run_fib_sequence(fib_lru_16, "З functools кешем (maxsize=16)")
