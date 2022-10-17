# .isalnum - check for letters and digits
# .isdigit - check for digits

password = input()
password_is_valid = True
if not 6 <= len(password) <= 10:
    password_is_valid = False
    print("Password must be between 6 and 10 characters")
if not password.isalnum():
    password_is_valid = False
    print("Password must consist only of letters and digits")
counter_digits = 0
for digit in password:
    if digit.isdigit():
        counter_digits += 1
if counter_digits < 2:
    password_is_valid = False
    print("Password must have at least 2 digits")
if password_is_valid:
    print("Password is valid")