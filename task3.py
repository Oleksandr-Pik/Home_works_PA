# Напишіть програму яка буде виводити 25 перших чисел Фібоначі,
# використовуючи для цього три наведені в тексті заняття функції:
# без кешу,
# з кешем довільної довжини,
# з кешем з модулю functools з максимальною кількістю 10 елементів
# та з кешем з модулю functools з максимальною кількістю 16 елементів.


from functools import lru_cache


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


print(" Без кешу:")
for i in range(25):
    print(fib_no_cache(i), end=' ')

print("\n\n З кешем довільної довжини:")
for i in range(25):
    print(fib_custom_cache(i), end=' ')

print("\n\n З functools кешем (maxsize=10):")
for i in range(25):
    print(fib_lru_10(i), end=' ')

print("\n\n З functools кешем (maxsize=16):")
for i in range(25):
    print(fib_lru_16(i), end=' ')
