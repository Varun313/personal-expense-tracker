def calculate_summary(transactions):
    income = 0
    expenses = 0

    for transaction in transactions:

        if transaction["type"] == "income":
            income += transaction["amount"]

        elif transaction["type"] == "expense":
            expenses += transaction["amount"]

    balance = income - expenses

    return {
        "income": income,
        "expenses": expenses,
        "balance": balance
    }