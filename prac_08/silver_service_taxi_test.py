from prac_08.silverservicetaxi import SilverServiceTaxi

taxi = SilverServiceTaxi("Hummer", 200, 2)
taxi.drive(18)
print(taxi)
print(f"${taxi.get_fare()}")
