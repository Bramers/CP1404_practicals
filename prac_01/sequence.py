low_number = 0
high_number = 0

MENU = f"""i. Show the even numbers from {low_number} to {high_number}
ii. Show the odd numbers from {low_number} to {high_number}
iii. Show the squares from {low_number} to {high_number}
iv. Exit the program"""

low_number = int(input("Enter a low number: "))
high_number = int(input("Enter a high number: "))
print(MENU)
choice = input(">>> ")
while choice != "iv":
    if choice == "i":
        if low_number % 2 == 1:
            for i in range(low_number + 1, high_number, 2):
                print(i)
        else:
            for i in range(low_number, high_number, 2):
                print(i)
    elif choice == "ii":
        if low_number % 2 == 0:
            for i in range(low_number + 1, high_number, 2):
                print(i)
        else:
            for i in range(low_number, high_number, 2):
                print(i)
    elif choice == "iii":
        for i in range(low_number, high_number):
            print(i ** 2)
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ")
print("Goodbye")
