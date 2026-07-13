# Money Transfer Calculator

usd_amount = float(input("Enter the USD amount sent: "))
exchange_rate = float(input("Enter the current exchange rate (1 USD to NPR): "))
service_fee = float(input("Enter the service fee percentage: "))

converted_npr = usd_amount * exchange_rate

fee = converted_npr * (service_fee / 100)


final_amount = converted_npr - fee

# Output
print("\n----- Money Transfer Summary -----")
print(f"Converted Amount: NPR {converted_npr:.2f}")
print(f"Service Fee: NPR {fee:.2f}")
print(f"Final Amount Received: NPR {final_amount:.2f}")