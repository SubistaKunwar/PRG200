# Inventory Restock Alert Program

inventory = [
    {"item": "Rice", "stock": 5, "threshold": 10},
    {"item": "Eggs", "stock": 24, "threshold": 12},
    {"item": "Milk", "stock": 3, "threshold": 6},
    {"item": "Bread", "stock": 8, "threshold": 5},
    {"item": "Chicken", "stock": 0, "threshold": 4},
    {"item": "Cooking Oil", "stock": 2, "threshold": 3},
]

# Variable to count the number of items that need restocking
restock_count = 0

print("=== Inventory Restock Report ===\n")

# Loop through each item in the inventory
for item in inventory:

    # Check if the stock is below the threshold
    if item["stock"] < item["threshold"]:
        print(f"Restock Alert: {item['item']}")
        print(f"Current Stock : {item['stock']}")
        print(f"Threshold     : {item['threshold']}")
        print("-" * 30)

        # Increase the restock counter
        restock_count += 1

# Display the total number of items that need restocking
print(f"\nTotal items that need restocking: {restock_count}")