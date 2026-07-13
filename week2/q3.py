# Trekking Cost Calculator

# Input
trekkers = int(input("Enter the number of trekkers: "))
fee_per_person = float(input("Enter TIMS + ACAP fee per person (NPR): "))

total_fee = trekkers * fee_per_person

service_charge = total_fee * 0.05

final_cost = total_fee + service_charge

average_cost = final_cost / trekkers

# Output
print("\n----- Trekking Cost Summary -----")
print(f"Total Cost: NPR {final_cost:.2f}")
print(f"Average Cost Per Person: NPR {average_cost:.2f}")