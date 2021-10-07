from prac_08.silverservicetaxi import SilverServiceTaxi
from prac_08.taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
current_taxi = None
bill_to_date = 0
print("Let's drive!")
print(MENU)
choice = input(">>>").lower()
while choice != "q":
    if choice == "c":
        print("Taxis available:")
        for i, taxi in enumerate(taxis):
            print(f"{i} - {taxi}")
        try:
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
        except IndexError:
            print("Invalid choice")
    elif choice == "d":
        if current_taxi is None:
            print("You need to choose a taxi before you can drive")
        else:
            distance = int(input("Drive how far? "))
            current_taxi.start_fare()
            current_taxi.drive(distance)
            bill_to_date += current_taxi.get_fare()
            print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}")
    else:
        print("Invalid option")
    print(f"Bill to date: ${bill_to_date:.2f}")
    print(MENU)
    choice = input(">>>").lower()
print(f"Total trip cost: {bill_to_date:.2f}")
print("Taxis are now:")
for i, taxi in enumerate(taxis):
    print(f"{i} - {taxi}")
