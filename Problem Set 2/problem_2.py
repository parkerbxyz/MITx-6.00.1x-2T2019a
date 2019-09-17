def lowest_payment(balance: float, annual_interest_rate: float) -> float:
    """Return the minimum fixed monthly payment that is a multiple
    of $10 needed to pay off a credit card balance within 12 months.
    """
    minimum_payment = 10
    original_balance = balance
    monthly_interest_rate = annual_interest_rate / 12.0
    while balance > 0:
        for month in range(12):
            unpaid_balance = balance - minimum_payment
            balance = unpaid_balance + (monthly_interest_rate * unpaid_balance)
        if balance > 0:
            minimum_payment += 10
            balance = original_balance
    return round(minimum_payment, 2)


print("Loweset Payment:", lowest_payment(balance, annualInterestRate))
