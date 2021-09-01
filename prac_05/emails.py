def main():
    """Store email and name in a dictionary"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        full_name = get_name_from_email(email)
        print(f"Is your name {full_name}")
        verification = input("(Y/n) ").upper()
        if verification != "Y" and verification != "":
            full_name = input("Name: ").title()
        email_to_name[email] = full_name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name}({email})")


def get_name_from_email(email):
    """Get name from email"""
    full_name = ""
    names = email.split("@")[0].split(".")
    for name in names:
        part = name.capitalize()
        full_name += part + " "
    return full_name


main()
