# Створіть звичайну функцію множення двох чисел.
# Створіть карированну функцію множення двох чисел.
# Частково застосуйте її до одного аргументу, до двох аргументiв.

def mult(num1, num2):
    return num1 * num2

def curried_mult(num1):
    def do_mult(num2):
        return num1 * num2

    return do_mult

print(mult(3, 6))
print()

print(curried_mult(3)(6))
print()

mult_to_five = curried_mult(5)
print(mult_to_five(2))
print(mult_to_five(3))
