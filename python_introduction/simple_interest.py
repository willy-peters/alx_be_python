
def main():
    """Main function to run the finance calculator."""
    
    # Get user input for financial details
    monthly_income = float(input("Enter your monthly income: "))
    monthly_expenses = float(input("Enter your total monthly expenses: "))
    
    # Calculate monthly savings
    monthly_savings = monthly_income - monthly_expenses
    
    # Check if savings are positive, then project annual savings
    if monthly_savings >= 0:
        # Project annual savings with 5% interest
        annual_interest_rate = 0.05
        total_annual_savings = monthly_savings * 12
        interest_earned = total_annual_savings * annual_interest_rate
        projected_savings = total_annual_savings + interest_earned
        
        # Display results
        print(f"Your monthly savings are ${monthly_savings:.0f}.")
        print(f"Projected savings after one year, with interest, is: ${projected_savings:.0f}.")
    else:
        print(f"Warning: You have a monthly deficit of ${abs(monthly_savings):.2f}")
        print("Consider reducing expenses or increasing income.")

if __name__ == "__main__":
    main()
