def palindrome(integers : list):

    for num in integers:
        if num == num[::-1]:
            print("True")
        else:
            print("False")


list_of_numbers = input().split(", ")
palindrome(list_of_numbers)
