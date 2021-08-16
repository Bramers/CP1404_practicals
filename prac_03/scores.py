import random


def main():
    out_file = open("results.txt", "w")
    number_of_scores = int(input("Number of scores? "))
    for i in range(number_of_scores):
        score = random.randint(0, 100)
        result = determine_score_status(score)
        print(f"{score:2} is {result}", file=out_file)
    out_file.close()


def determine_score_status(score):
    if score < 50:
        result = "Bad"
    elif score < 90:
        result = "Passable"
    else:
        result = "Excellent"
    return result


main()
