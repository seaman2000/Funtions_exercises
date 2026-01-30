def is_length_valid(password):
    return 6 <= len(password) <= 10


def has_only_letters_and_digits(password):
    return password.isalnum()


def has_at_least_two_digits(password):
    return sum(char.isdigit() for char in password) >= 2


def is_valid(password):
    valid = True

    if not is_length_valid(password):
        print("Password must be between 6 and 10 characters")
        valid = False

    if not has_only_letters_and_digits(password):
        print("Password must consist only of letters and digits")
        valid = False

    if not has_at_least_two_digits(password):
        print("Password must have at least 2 digits")
        valid = False

    if valid:
        print("Password is valid")


password_input = input()
is_valid(password_input)
