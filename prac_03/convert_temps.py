def main():
    in_file = open("temps_input.txt", "r")
    out_file = open("temp_output.txt", "w")
    for line in in_file:
        temperature_celsius = convert_fahrenheit_to_celsius(float(line))
        print(temperature_celsius, file=out_file)
    in_file.close()
    out_file.close()


def convert_fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
