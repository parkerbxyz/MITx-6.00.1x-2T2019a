def remaining_balance(balance: float,
                      annual_interest_rate: float,
                      monthly_payment_rate: float) -> float:
    """Return the remaining balance after 12 months of minimum payments."""
    monthly_interest_rate = annual_interest_rate / 12.0
    for month in range(12):
        minimum_payment = monthly_payment_rate * balance
        unpaid_balance = balance - minimum_payment
        balance = unpaid_balance + (monthly_interest_rate * unpaid_balance)
    return round(balance, 2)


print("Remaining balance:",
      remaining_balance(balance, annualInterestRate, monthlyPaymentRate))
