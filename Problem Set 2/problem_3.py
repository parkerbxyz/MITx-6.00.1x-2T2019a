def remaining_balance(balance: float, annual_interest_rate: float,
                      monthly_payment: float) -> float:
    """Return the remaining balance after 12 months of monthly payments."""
    monthly_interest_rate = annual_interest_rate / 12.0
    for month in range(12):
        unpaid_balance = balance - monthly_payment
        balance = unpaid_balance + (monthly_interest_rate * unpaid_balance)
    return round(balance, 2)


def lowest_payment(balance: float, annual_interest_rate: float) -> float:
    """Return the minimum fixed monthly payment needed
    to pay off a credit card balance within 12 months.
    """
    starting_balance = balance
    monthly_interest_rate = annual_interest_rate / 12.0
    min_payment = balance / 12
    max_payment = (balance * (1 + monthly_interest_rate)**12) / 12
    monthly_payment = (min_payment + max_payment) / 2
    while balance != 0:
        balance = remaining_balance(
            balance, annual_interest_rate, monthly_payment)
        if balance > 0:
            min_payment = monthly_payment
            balance = starting_balance
        if balance < 0:
            max_payment = monthly_payment
            balance = starting_balance
        monthly_payment = (min_payment + max_payment) / 2
    return round(monthly_payment, 2)


print("Loweset Payment:", lowest_payment(balance, annualInterestRate))
