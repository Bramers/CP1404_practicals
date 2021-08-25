COLOUR_CODE_TO_NAMES = {"beige": "#f5f5dc", "black": "	#000000", "coral": "#ff7f50", "cornflowerblue": "#6495ed",
                        "darkkhaki": "#bdb76b", "darkorchid": "#9932cc", "firebrick": "#b22222", "gold1": "#ffd700",
                        "gray": "#bebebe", "hotpink": "#ff69b4"}

colour = input("Colour: ").lower()
while colour != "":
    if colour in COLOUR_CODE_TO_NAMES:
        print(f"The {colour} colour code is {COLOUR_CODE_TO_NAMES[colour]}")
    else:
        print("Invalid colour")
    colour = input("Colour: ").lower()

