# Momo Shop Profit Calculator

cost_price = float(input("Enter the cost price per plate (NPR): "))
selling_price = float(input("Enter the selling price per plate (NPR): "))
plates_sold = int(input("Enter the number of plates sold: "))

# Calculations
total_revenue = selling_price * plates_sold
total_cost = cost_price * plates_sold
total_profit = total_revenue - total_cost
profit_margin = (total_profit / total_revenue) * 100

# Output
print("\n----- Momo Shop Profit Report -----")
print(f"Total Revenue: NPR {total_revenue:.2f}")
print(f"Total Cost: NPR {total_cost:.2f}")
print(f"Total Profit: NPR {total_profit:.2f}")
print(f"Profit Margin: {profit_margin:.2f}%")