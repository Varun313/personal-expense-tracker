def get_valid_amount():
    while True:

        amount = input("Amount: ").strip()

        try:
            amount = float(amount)

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            return amount

        except ValueError:
            print("Please enter a valid number.")