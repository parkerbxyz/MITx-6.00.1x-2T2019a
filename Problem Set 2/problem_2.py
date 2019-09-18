def remaining_balance(balance: float,
                      annual_interest_rate: float,
                      monthly_payment: float) -> float:
    """Return the remaining balance after 12 months of monthly payments."""
    monthly_interest_rate = annual_interest_rate / 12.0
    for month in range(12):
        unpaid_balance = balance - monthly_payment
        balance = unpaid_balance + (monthly_interest_rate * unpaid_balance)
    return round(balance, 2)


def lowest_payment(balance: float, annual_interest_rate: float) -> float:
    """Return the minimum fixed monthly payment that is a multiple
    of $10 needed to pay off a credit card balance within 12 months.
    """
    starting_balance = balance
    minimum_payment = 10
    while balance > 0:
        balance = remaining_balance(
            balance, annual_interest_rate, minimum_payment)
        if balance > 0:
            minimum_payment += 10
            balance = starting_balance
    return round(minimum_payment, 2)


print("Loweset Payment:", lowest_payment(balance, annualInterestRate))
