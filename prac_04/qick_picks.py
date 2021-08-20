import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(number_of_quick_picks):
        random_numbers = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in random_numbers:
                number = random.randint(MINIMUM, MAXIMUM)
            random_numbers.append(number)
        random_numbers.sort()
        print(" ".join("{:2}".format(number) for number in random_numbers))


main()
