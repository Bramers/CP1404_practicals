out_file = open("name.txt", "w")
name = input("Name: ")
print(name, file=out_file)
out_file.close()

in_file = open("name.txt", "r")
text = in_file.read().strip()
in_file.close()
print(f"Your name is {text}")

in_file = open("numbers.txt", "r")
number_1 = int(in_file.readline())
number_2 = int(in_file.readline())
in_file.close()
result = number_1 + number_2
print(result)

in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    total += int(line)
in_file.close()
print(f"The total is {total}")
