from utils.storage import load_transactions, save_transactions
from utils.calculations import calculate_summary
from utils.validators import get_valid_amount


def add_transaction(transactions, transaction_type):
    print("\n-----------------------------")
    print(f"ADD {transaction_type.upper()}")
    print("-----------------------------")

    description = input("Description: ").strip()

    if not description:
        print("Description cannot be empty.")
        return

    amount = get_valid_amount()

    category = input("Category: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    date = input("Date (YYYY-MM-DD): ").strip()

    if not date:
        print("Date cannot be empty.")
        return

    transaction = {
        "description": description,
        "amount": amount,
        "category": category,
        "date": date,
        "type": transaction_type
    }

    transactions.append(transaction)
    save_transactions(transactions)

    print("\nTransaction added successfully!")


def view_transactions(transactions):
    print("\n==============================")
    print("       ALL TRANSACTIONS")
    print("==============================")

    if not transactions:
        print("No transactions found.")
        return

    for index, transaction in enumerate(transactions, start=1):
        print(f"\n{index}. {transaction['description']}")
        print(f"   Amount: ₹{transaction['amount']:.2f}")
        print(f"   Category: {transaction['category']}")
        print(f"   Date: {transaction['date']}")
        print(f"   Type: {transaction['type'].title()}")


def search_transactions(transactions):
    print("\n==============================")
    print("       SEARCH TRANSACTIONS")
    print("==============================")

    if not transactions:
        print("No transactions available.")
        return

    search_term = input(
        "Enter description or category to search: "
    ).strip().lower()

    if not search_term:
        print("Search cannot be empty.")
        return

    results = []

    for transaction in transactions:
        description = str(
            transaction.get("description", "")
        ).lower()

        category = str(
            transaction.get("category", "")
        ).lower()

        if search_term in description or search_term in category:
            results.append(transaction)

    if not results:
        print(f"\nNo transactions found for '{search_term}'.")
        return

    print(f"\nFound {len(results)} transaction(s):")

    for index, transaction in enumerate(results, start=1):
        print(f"\n{index}. {transaction['description']}")
        print(f"   Amount: ₹{transaction['amount']:.2f}")
        print(f"   Category: {transaction['category']}")
        print(f"   Date: {transaction['date']}")
        print(f"   Type: {transaction['type'].title()}")


def filter_transactions(transactions):
    print("\n==============================")
    print("       FILTER TRANSACTIONS")
    print("==============================")

    if not transactions:
        print("No transactions available.")
        return

    print("\n1. Filter by Category")
    print("2. Filter by Type")
    print("3. Back")

    choice = input("\nChoose an option: ").strip()

    results = []

    if choice == "1":
        category = input(
            "Enter category: "
        ).strip().lower()

        if not category:
            print("Category cannot be empty.")
            return

        for transaction in transactions:
            if transaction["category"].lower() == category:
                results.append(transaction)

        if not results:
            print(
                f"\nNo transactions found in category "
                f"'{category}'."
            )
            return

    elif choice == "2":
        print("\n1. Income")
        print("2. Expense")

        type_choice = input(
            "Choose type: "
        ).strip()

        if type_choice == "1":
            transaction_type = "income"

        elif type_choice == "2":
            transaction_type = "expense"

        else:
            print("Invalid option.")
            return

        for transaction in transactions:
            if transaction["type"].lower() == transaction_type:
                results.append(transaction)

        if not results:
            print(
                f"\nNo {transaction_type} transactions found."
            )
            return

    elif choice == "3":
        return

    else:
        print("Invalid option.")
        return

    print("\n==============================")
    print("       FILTERED RESULTS")
    print("==============================")

    print(f"\nFound {len(results)} transaction(s):")

    for index, transaction in enumerate(results, start=1):
        print(f"\n{index}. {transaction['description']}")
        print(f"   Amount: ₹{transaction['amount']:.2f}")
        print(f"   Category: {transaction['category']}")
        print(f"   Date: {transaction['date']}")
        print(f"   Type: {transaction['type'].title()}")


def filter_by_date(transactions):
    print("\n==============================")
    print("        FILTER BY DATE")
    print("==============================")

    if not transactions:
        print("No transactions available.")
        return

    date = input(
        "Enter date (YYYY-MM-DD): "
    ).strip()

    if not date:
        print("Date cannot be empty.")
        return

    results = []

    for transaction in transactions:
        if transaction["date"] == date:
            results.append(transaction)

    if not results:
        print(
            f"\nNo transactions found for {date}."
        )
        return

    print(f"\nTransactions for {date}:")
    print("------------------------------")

    for index, transaction in enumerate(results, start=1):
        print(f"\n{index}. {transaction['description']}")
        print(f"   Amount: ₹{transaction['amount']:.2f}")
        print(f"   Category: {transaction['category']}")
        print(f"   Date: {transaction['date']}")
        print(f"   Type: {transaction['type'].title()}")

    total = sum(
        transaction["amount"]
        for transaction in results
    )

    print("\n------------------------------")
    print(f"Total for {date}: ₹{total:.2f}")


def monthly_analytics(transactions):
    print("\n==============================")
    print("       MONTHLY ANALYTICS")
    print("==============================")

    if not transactions:
        print("No transactions available.")
        return

    month = input(
        "Enter month (YYYY-MM): "
    ).strip()

    if len(month) != 7 or month[4] != "-":
        print("Please use YYYY-MM format.")
        return

    monthly_transactions = []

    for transaction in transactions:
        if transaction["date"].startswith(month):
            monthly_transactions.append(transaction)

    if not monthly_transactions:
        print(
            f"\nNo transactions found for {month}."
        )
        return

    total_income = 0
    total_expenses = 0
    expense_amounts = []

    for transaction in monthly_transactions:
        amount = float(transaction["amount"])

        if transaction["type"] == "income":
            total_income += amount

        elif transaction["type"] == "expense":
            total_expenses += amount
            expense_amounts.append(amount)

    balance = total_income - total_expenses
    transaction_count = len(monthly_transactions)

    if expense_amounts:
        highest_expense = max(expense_amounts)
        average_expense = (
            sum(expense_amounts)
            / len(expense_amounts)
        )
    else:
        highest_expense = 0
        average_expense = 0

    print("\n------------------------------")
    print(f"MONTH: {month}")
    print("------------------------------")

    print(f"Total Income:       ₹{total_income:.2f}")
    print(f"Total Expenses:     ₹{total_expenses:.2f}")
    print(f"Balance:            ₹{balance:.2f}")
    print(f"Transactions:       {transaction_count}")
    print(f"Highest Expense:    ₹{highest_expense:.2f}")
    print(f"Average Expense:    ₹{average_expense:.2f}")


def category_analytics(transactions):
    print("\n==============================")
    print("      CATEGORY ANALYTICS")
    print("==============================")

    if not transactions:
        print("No transactions available.")
        return

    category_totals = {}

    for transaction in transactions:
        if transaction["type"].lower() != "expense":
            continue

        category = transaction["category"].strip()

        if not category:
            category = "Uncategorized"

        category_key = category.lower()

        if category_key not in category_totals:
            category_totals[category_key] = {
                "name": category,
                "amount": 0,
                "count": 0
            }

        category_totals[category_key]["amount"] += float(
            transaction["amount"]
        )

        category_totals[category_key]["count"] += 1

    if not category_totals:
        print("No expense transactions available.")
        return

    total_expenses = sum(
        item["amount"]
        for item in category_totals.values()
    )

    sorted_categories = sorted(
        category_totals.values(),
        key=lambda item: item["amount"],
        reverse=True
    )

    print(
        f"\nTotal Expenses: ₹{total_expenses:.2f}"
    )

    print(
        f"Categories: {len(sorted_categories)}"
    )

    print("\n------------------------------")
    print("SPENDING BY CATEGORY")
    print("------------------------------")

    for index, item in enumerate(
        sorted_categories,
        start=1
    ):
        percentage = (
            item["amount"] / total_expenses * 100
        )

        print(
            f"\n{index}. {item['name']}"
        )

        print(
            f"   Amount: ₹{item['amount']:.2f}"
        )

        print(
            f"   Transactions: {item['count']}"
        )

        print(
            f"   Share: {percentage:.1f}%"
        )

    highest = sorted_categories[0]

    print("\n------------------------------")
    print("HIGHEST SPENDING CATEGORY")
    print("------------------------------")

    print(
        f"Category: {highest['name']}"
    )

    print(
        f"Amount: ₹{highest['amount']:.2f}"
    )

    print(
        f"Share: "
        f"{highest['amount'] / total_expenses * 100:.1f}%"
    )


def edit_transaction(transactions):
    if not transactions:
        print("\nNo transactions to edit.")
        return

    view_transactions(transactions)

    try:
        number = int(
            input("\nEnter transaction number to edit: ")
        )
    except ValueError:
        print("Please enter a valid number.")
        return

    if number < 1 or number > len(transactions):
        print("Invalid transaction number.")
        return

    transaction = transactions[number - 1]

    print("\n-----------------------------")
    print("       EDIT TRANSACTION")
    print("-----------------------------")

    print(
        f"\nCurrent description: "
        f"{transaction['description']}"
    )

    new_description = input(
        "New description (press Enter to keep current): "
    ).strip()

    if new_description:
        transaction["description"] = new_description

    print(
        f"\nCurrent amount: "
        f"₹{transaction['amount']:.2f}"
    )

    new_amount = input(
        "New amount (press Enter to keep current): "
    ).strip()

    if new_amount:
        try:
            new_amount = float(new_amount)

            if new_amount <= 0:
                print("Amount must be greater than zero.")
                return

            transaction["amount"] = new_amount

        except ValueError:
            print("Please enter a valid amount.")
            return

    print(
        f"\nCurrent category: "
        f"{transaction['category']}"
    )

    new_category = input(
        "New category (press Enter to keep current): "
    ).strip()

    if new_category:
        transaction["category"] = new_category

    print(
        f"\nCurrent date: "
        f"{transaction['date']}"
    )

    new_date = input(
        "New date (press Enter to keep current): "
    ).strip()

    if new_date:
        transaction["date"] = new_date

    save_transactions(transactions)

    print("\nTransaction updated successfully!")


def delete_transaction(transactions):
    if not transactions:
        print("\nNo transactions to delete.")
        return

    view_transactions(transactions)

    try:
        number = int(
            input("\nEnter transaction number to delete: ")
        )
    except ValueError:
        print("Please enter a valid number.")
        return

    if number < 1 or number > len(transactions):
        print("Invalid transaction number.")
        return

    deleted = transactions.pop(number - 1)

    save_transactions(transactions)

    print(
        f"\n'{deleted['description']}' "
        "was deleted successfully."
    )


def show_summary(transactions):
    summary = calculate_summary(transactions)

    print("\n==============================")
    print("        FINANCIAL SUMMARY")
    print("==============================")

    print(
        f"Total Income:   "
        f"₹{summary['income']:.2f}"
    )

    print(
        f"Total Expenses: "
        f"₹{summary['expenses']:.2f}"
    )

    print("------------------------------")

    print(
        f"Balance:        "
        f"₹{summary['balance']:.2f}"
    )


def main():
    transactions = load_transactions()

    while True:
        print("\n")
        print("================================")
        print("       PERSONAL EXPENSE TRACKER")
        print("================================")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Financial Summary")
        print("5. Search Transactions")
        print("6. Filter Transactions")
        print("7. Filter by Date")
        print("8. Monthly Analytics")
        print("9. Category Analytics")
        print("10. Edit Transaction")
        print("11. Delete Transaction")
        print("12. Exit")
        print("================================")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_transaction(
                transactions,
                "income"
            )

        elif choice == "2":
            add_transaction(
                transactions,
                "expense"
            )

        elif choice == "3":
            view_transactions(transactions)

        elif choice == "4":
            show_summary(transactions)

        elif choice == "5":
            search_transactions(transactions)

        elif choice == "6":
            filter_transactions(transactions)

        elif choice == "7":
            filter_by_date(transactions)

        elif choice == "8":
            monthly_analytics(transactions)

        elif choice == "9":
            category_analytics(transactions)

        elif choice == "10":
            edit_transaction(transactions)

        elif choice == "11":
            delete_transaction(transactions)

        elif choice == "12":
            print(
                "\nThank you for using "
                "Personal Expense Tracker!"
            )
            break

        else:
            print(
                "\nInvalid option. "
                "Please choose 1-12."
            )


if __name__ == "__main__":
    main()