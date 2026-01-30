list_of_numbers = input().split()

list_of_integers = []

for number in list_of_numbers:
    integer_number = int(number)
    list_of_integers.append(integer_number)

print(sorted(list_of_integers))