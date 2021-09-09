from guitar import Guitar
guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another_guitar", 2013, 1)


print(f"{guitar.name} get_age() - Expected 99. Got {guitar.get_age()}")
print(f"{another_guitar.name} get_age() - Expected 8. Got {another_guitar.get_age()}")
print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")
