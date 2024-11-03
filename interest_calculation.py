investment_amount = float(input("Enter the investement amount(greater than 0 and less than 50000): "))
while investment_amount <= 0 or investment_amount > 50000:
    investment_amount = float(input("Invalid amount. Please try again: "))

interest_rate = float(input("Enter the interest rate(greater than 0 and less than 15): "))
while interest_rate <= 0 or interest_rate > 15:
    interest_rate = float(input("Invalid amount. Please try again: "))

investment_duration = int(input("Enter the investment duration in years: "))
while investment_duration <= 0:
    investment_duration = int(input("Invalid amount. Please try again: "))

months = investment_duration * 12
monthly_interest_rate = interest_rate / 12 / 100

future_total = 0
for i in range(1, months +1):
    future_total += investment_amount
    interest_amount = future_total * monthly_interest_rate
    future_total += interest_amount
    
    if i % 12 == 0:
        print(f"Year {i // 12}: ${round(future_total, 2)}")
print()

print(f"Investment Duration: {investment_duration}")
print(f"Yearly Interest Rate: {interest_rate}%")
print(f"Monthly Investment Amount: ${investment_amount}")
print(f"Total Amount of Investment After Compounding: ${round(future_total, 2)}")
print("Completed by, Cade Armstrong")