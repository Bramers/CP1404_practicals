"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


# score = float(input("Enter score: "))
# if score < 0:
#     print("Invalid score")
# else:
#     if score > 100:
#         print("Invalid score")
#     if score > 50:
#         print("Passable")
#     if score > 90:
#     print("Excellent")
# if score < 50:
#     print("Bad")

import random


def main():
    """Get a score and print the status"""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    result = determine_score_status(score)
    print(result)

    random_score = random.randint(0, 100)
    result = determine_score_status(random_score)
    print(f"{random_score} is {result}")


def determine_score_status(score):
    """Determine the status of score"""
    if score < 50:
        result = "Bad"
    elif score < 90:
        result = "Passable"
    else:
        result = "Excellent"
    return result


main()
