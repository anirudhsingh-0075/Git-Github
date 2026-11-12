import os

File_name = "bank.txt"
Min_balance = 500


def load_accounts():
    # Loads the account records from bank.txt into a dictionary
    accounts = {}
    if os.path.exists(File_name):
        with open(File_name, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    if len(parts) == 3:
                        acc_no = int(parts[0])
                        name = parts[1]
                        # Convert to int if whole number, else float for clean formatting
                        balance = float(parts[2])
                        if balance.is_integer():
                            balance = int(balance)
                        accounts[acc_no] = {"name": name, "balance": balance}
    return accounts


def save_accounts(accounts):
    # Saves all the account records from the dictionary back into bank.txt
    with open(File_name, "w") as file:
        for acc_no, data in accounts.items():
            file.write(f"{acc_no},{data['name']},{data['balance']}\n")


def format_amount(val):
    # Formats numeric balance to show int instead of float
    return int(val) if float(val).is_integer() else val


def get_valid_amount(prompt):
    # Prompts for and validates a positive numerical amount
    try:
        amount = float(input(prompt))
        if amount <= 0:
            print("Invalid amount. Value must be greater than 0.")
            return None
        return format_amount(amount)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None


def get_valid_acc_no(prompt):
    # Prompts for and validates an integer account number
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid account number. Please enter numbers only.")
        return None


def create_account(accounts):
    # Create a new bank account starting from 1001
    name = input("Enter customer name: ").strip()
    if not name or "," in name:
        print("Invalid name. Name cannot be empty or contain commas.")
        return

    deposit = get_valid_amount("Enter opening deposit: ")
    if deposit is None:
        return

    if deposit < Min_balance:
        print(f"Account not created. Minimum opening balance of Rs.{Min_balance} is required.")
        return

    # Generate unique account number starting from 1001
    next_acc_no = max(accounts.keys(), default=1000) + 1
    accounts[next_acc_no] = {"name": name, "balance": deposit}
    save_accounts(accounts)

    print(f"Account created. A/C No: {next_acc_no} | Balance: {accounts[next_acc_no]['balance']}")


def deposit_money(accounts):
    # Deposit money into an existing account
    acc_no = get_valid_acc_no("Enter account number: ")
    if acc_no is None:
        return

    if acc_no not in accounts:
        print(f"Account {acc_no} not found.")
        return

    amount = get_valid_amount("Enter deposit amount: ")
    if amount is None:
        return

    accounts[acc_no]["balance"] = format_amount(accounts[acc_no]["balance"] + amount)
    save_accounts(accounts)
    print(f"Deposit successful. Balance: {accounts[acc_no]['balance']}")


def withdraw_money(accounts):
    # Withdraw money while enforcing the Rs.500 minimum balance rule
    acc_no = get_valid_acc_no("Enter account number: ")
    if acc_no is None:
        return

    if acc_no not in accounts:
        print(f"Account {acc_no} not found.")
        return

    amount = get_valid_amount("Enter withdrawal amount: ")
    if amount is None:
        return

    if accounts[acc_no]["balance"] - amount < Min_balance:
        print(f"Withdrawal failed. A minimum balance of Rs.{Min_balance} must always remain in the account.")
        return

    accounts[acc_no]["balance"] = format_amount(accounts[acc_no]["balance"] - amount)
    save_accounts(accounts)
    print(f"Withdrawal successful. Balance remaining: {accounts[acc_no]['balance']}")


def transfer_money(accounts):
    # Transfer money between two accounts while checking validity and minimum balance
    from_acc = get_valid_acc_no("Enter sender account number: ")
    if from_acc is None:
        return
    if from_acc not in accounts:
        print(f"Account {from_acc} not found. Transfer cancelled.")
        return

    to_acc = get_valid_acc_no("Enter receiver account number: ")
    if to_acc is None:
        return
    if to_acc not in accounts:
        print(f"Account {to_acc} not found. Transfer cancelled.")
        return

    if from_acc == to_acc:
        print("Cannot transfer to the same account. Transfer cancelled.")
        return

    amount = get_valid_amount("Enter transfer amount: ")
    if amount is None:
        return

    if accounts[from_acc]["balance"] - amount < Min_balance:
        print(f"Transfer cancelled. Sender must maintain a minimum balance of Rs.{Min_balance}.")
        return

    accounts[from_acc]["balance"] = format_amount(accounts[from_acc]["balance"] - amount)
    accounts[to_acc]["balance"] = format_amount(accounts[to_acc]["balance"] + amount)
    save_accounts(accounts)

    print("Transfer successful.")
    print(f"{from_acc} balance: {accounts[from_acc]['balance']} | {to_acc} balance: {accounts[to_acc]['balance']}")


def check_balance(accounts):
    # Enquire account details and balance
    acc_no = get_valid_acc_no("Enter account number: ")
    if acc_no is None:
        return

    if acc_no not in accounts:
        print(f"Account {acc_no} not found.")
        return

    acc = accounts[acc_no]
    print(f"A/C No: {acc_no} | Name: {acc['name']} | Balance: {acc['balance']}")


def main():
    # Main console menu loop
    while True:
        accounts = load_accounts()
        print("\n--- Simple Banking System ---")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Balance Enquiry")
        print("6. Exit")

        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            deposit_money(accounts)
        elif choice == "3":
            withdraw_money(accounts)
        elif choice == "4":
            transfer_money(accounts)
        elif choice == "5":
            check_balance(accounts)
        elif choice == "6":
            print("Thank you for using the Simple Banking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main() 
    