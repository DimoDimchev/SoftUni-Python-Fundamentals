def validate(password, numbers):
    for character in password:
        if character.isdigit():
            numbers += 1
    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
    if not password.isalnum():
        print("Password must consist only of letters and digits")
    if not numbers >= 2:
        print("Password must have at least 2 digits")
    if numbers >= 2 and 6 <= len(password) <= 10 and password.isalnum():
        print("Password is valid")


password_input = input()
number_counter = 0

validate(password_input, number_counter)
