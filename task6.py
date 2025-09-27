# Створіть функцію-генератор чисел Фібоначчі.
# Застосуйте до неї декоратор, який залишатиме в послідовності лише парні числа.


def filter_even(generator_func):
    def wrapper(*args, **kwargs):
        for number in generator_func(*args, **kwargs):
            if number % 2 == 0:
                yield number

    return wrapper


@filter_even
def fibonacci_generator(limit):
    a, b = 0, 1
    for i in range(limit):
        yield a
        a, b = b, a + b


n = int(input("Введіть натуральне число: "))

print("Парні числа Фібоначчі:")
for num in fibonacci_generator(n):
    print(num, end=' ')
