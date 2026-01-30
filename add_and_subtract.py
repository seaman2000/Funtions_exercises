def sum_numbers(a, b) -> int:
    return a + b


def subtract_numbers(sum_of_num, c ) -> int:
    return sum_of_num - c


def add_and_subtract():
    sum_of_numbers = sum_numbers(first_number, second_number)
    add_and_subtract_result = subtract_numbers(sum_of_numbers, third_number)
    return add_and_subtract_result


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract())