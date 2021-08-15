# PASSWORD_MINIMUM_LENGTH = 5
#
#
# function main()
#     password = get_password()
#     print_asterisks(password)
#
#
# function get_password()
#     get password
#     while length of password < PASSWORD_MINIMUM_LENGTH
#         display invalid password message
#         get password
#     return password
#
#
# function print_asterisks(password)
#     display "*" for each character in password
#
#
# main()


PASSWORD_MINIMUM_LENGTH = 5


def main():
    """Print asterisks based on its length of password"""
    password = get_password()
    print_asterisks(password)


def get_password():
    """Get a password of valid length"""
    password = input("Enter password: ")
    while len(password) < PASSWORD_MINIMUM_LENGTH:
        print(f"Password must be {PASSWORD_MINIMUM_LENGTH} characters long.")
        password = input("Enter password: ")
    return password


def print_asterisks(password):
    """Print * for password length"""
    print("*" * len(password))


main()
