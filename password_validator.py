def password_is_valid(password: str):
    digits_counter = 0
    has_only_letters_and_digits = True
    is_length_valid = 6 <= len(password) <= 10

    if not is_length_valid:
        print("Password must be between 6 and 10 characters")

    for char in password:
        if not char.isalpha() and not char.isdigit():
            print("Password must consist only of letters and digits")
            has_only_letters_and_digits = False
            break
        if char.isdigit():
            digits_counter += 1

    if digits_counter < 2:
        print("Password must have at least 2 digits")

    if (is_length_valid and
            digits_counter >= 2 and
            has_only_letters_and_digits):
        print("Password is valid")


password_input = input()
password_is_valid(password_input)