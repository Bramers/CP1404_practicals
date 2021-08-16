import random

out_file = open("temps_input.txt", "w")
for i in range(15):
    temperature_fahrenheit = random.randint(-200, 200)
    print(temperature_fahrenheit, file=out_file)
out_file.close()
