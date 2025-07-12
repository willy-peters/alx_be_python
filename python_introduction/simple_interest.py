monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = float(monthly_income) - float(monthly_expenses)

annual_interest_rate = 0.05
total_annual_savings = monthly_savings * 12
interest_earned = total_annual_savings * annual_interest_rate
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${monthly_savings:.0f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.0f}.")
