def perfect_dividers(integer_num: int):
    list_of_dividers = []
    for num in range(1, integer_num):
        if integer_num % num == 0:
            list_of_dividers.append(num)
    return list_of_dividers


def perfect_number(integer_num: int):
    sum_of_numbers = sum(perfect_dividers(integer_num))
    if sum_of_numbers == integer_num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number = int(input())
perfect_number(number)