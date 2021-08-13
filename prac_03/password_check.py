PASSWORD_MINIMUM_LENGTH = 5

password = input("Enter password: ")
while len(password) < PASSWORD_MINIMUM_LENGTH:
    print(f"Password must be {PASSWORD_MINIMUM_LENGTH} characters long.")
    password = input("Enter password: ")
print("*" * len(password))
