def factorial_number(number: int):
    result = 1
    for digit in range(1, number + 1):
        result *= digit
    return result


def factorial_division(a: int, b: int):
    return factorial_number(a) / factorial_number(b)


def main_input():
    first_num = int(input())
    second_num = int(input())
    result = factorial_division(first_num, second_num)
    print(f"{result:.2f}")

main_input()