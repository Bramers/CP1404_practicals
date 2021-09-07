# print("Electricity bill estimator")
# cents_per_kwh = int(input("Enter cents per kwh: ")) * .01
# daily_use_in_kwh = float(input("Enter daily use in kwh: "))
# number_of_billing_days = int(input("Enter number of billing days: "))
# bill_estimate = (cents_per_kwh * daily_use_in_kwh) * number_of_billing_days
# print(f"Estimated bill: ${bill_estimate:.2f}")

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
tariff = input("Which tariff? 11 or 31: ")
if tariff == "11":
    tariff = TARIFF_11
else:
    tariff = TARIFF_31
daily_use_in_kwh = float(input("Enter daily use in kwh: "))
number_of_billing_days = int(input("Enter number of billing days: "))
bill_estimate = (tariff * daily_use_in_kwh) * number_of_billing_days
print(f"Estimated bill: ${bill_estimate:.2f}")
