from auth import authenticate
from operations import check_balance, withdraw, deposit
from database import init_db, create_user

# Initialize database and create a test user
init_db()
create_user("123456", "1234", 5000.0)  # For testing

def main():
    print("Welcome to ATM")
    account_number = input("Enter account number: ")
    pin = input("Enter PIN: ")

    user = authenticate(account_number, pin)
    if not user:
        print("Invalid credentials. Try again.")
        return

    while True:
        print("\n1. Check Balance\n2. Withdraw\n3. Deposit\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            print(f"Your balance: ₹{check_balance(account_number)}")

        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            new_balance = withdraw(account_number, amount)
            if new_balance is not None:
                print(f"Withdrawal successful! New balance: ₹{new_balance}")
            else:
                print("Insufficient balance or invalid amount.")

        elif choice == "3":
            amount = float(input("Enter amount to deposit: "))
            new_balance = deposit(account_number, amount)
            if new_balance is not None:
                print(f"Deposit successful! New balance: ₹{new_balance}")
            else:
                print("Invalid deposit amount.")

        elif choice == "4":
            print("Thank you for using the ATM!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
