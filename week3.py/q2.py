# Online Store Discount System

purchase = float(input("Enter total purchase amount (NPR): "))
member = input("Are you a loyalty member? (yes/no): ")

discount = 0

if purchase < 1000:
    discount = 0
elif purchase < 5000:
    discount = 5
elif purchase < 15000:
    discount = 10
else:
    discount = 20

discounted_price = purchase - (purchase * discount / 100)

if member.lower() == "yes":
    discounted_price = discounted_price - (discounted_price * 5 / 100)

print("Final payable amount: NPR", round(discounted_price, 2))