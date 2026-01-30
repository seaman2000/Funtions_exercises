list_of_numbers = input().split()
list_of_nums = []

for digit in list_of_numbers:
    digit_integer = int(digit)
    list_of_nums.append(digit_integer)

even_numbers = filter(lambda num: num % 2 == 0, list_of_nums)
print(list(even_numbers))