def odd_even_sum(num: str):
    even_sum = 0
    odd_sum = 0

    for digit in num:
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        elif int(digit) % 2 != 0:
            odd_sum += int(digit)

    return even_sum, odd_sum


number = input()
even, odd = odd_even_sum(number)
print(f"Odd sum = {odd}, Even sum = {even}")