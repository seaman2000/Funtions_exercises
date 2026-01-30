sequence_of_numbers = input().split()

list_of_numbers = []

for number in sequence_of_numbers:
    integer_number = int(number)
    list_of_numbers.append(integer_number)

min_number = min(list_of_numbers)
max_number = max(list_of_numbers)
sum_of_list = sum(list_of_numbers)

print(
    f"The minimum number is {min_number}\n"
    f"The maximum number is {max_number}\n"
    f"The sum number is: {sum_of_list}"
)