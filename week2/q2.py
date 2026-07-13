# NEA Electricity Bill Calculator

# Input
previous_reading = float(input("Enter the previous meter reading: "))
current_reading = float(input("Enter the current meter reading: "))
rate_per_unit = float(input("Enter the rate per unit (NPR): "))
service_charge = float(input("Enter the monthly service charge (NPR): "))

units = current_reading - previous_reading

electricity_charge = units * rate_per_unit

total_bill = electricity_charge + service_charge

# Output
print("\n----- Electricity Bill -----")
print(f"Units Consumed: {units:.2f} kWh")
print(f"Electricity Charge: NPR {electricity_charge:.2f}")
print(f"Service Charge: NPR {service_charge:.2f}")
print(f"Total Bill: NPR {total_bill:.2f}")