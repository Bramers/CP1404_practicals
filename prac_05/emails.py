def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        full_name = get_name_from_email(email)
        print(f"Is your name {full_name}")
        correct_name = input("(Y/n) ").upper()
        if correct_name != "Y":
            full_name = input("Name: ").title()
        email_to_name[email] = full_name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name}({email})")


def get_name_from_email(email):
    full_name = ""
    names = email.split("@")[0].split(".")
    for name in names:
        part = name.capitalize()
        full_name += part + " "
    return full_name


main()
