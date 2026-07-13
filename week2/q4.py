# Dashain Bonus Calculator

# Input
salary = float(input("Enter monthly basic salary (NPR): "))
deduction_percent = float(input("Enter deduction percentage: "))

bonus = salary

deduction = bonus * (deduction_percent / 100)

final_bonus = bonus - deduction

# Output
print("\n----- Dashain Bonus -----")
print(f"Bonus Amount: NPR {bonus:.2f}")
print(f"Deduction: NPR {deduction:.2f}")
print(f"Final Take-home Bonus: NPR {final_bonus:.2f}")
