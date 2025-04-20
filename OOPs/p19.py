# Program 19 : Write an object oriented menu driven program to perform banking operations (New account, Deposit, Withdraw, Balance, Show all, Exit).
class BankAccount:
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance!")

    def show_balance(self):
        print(f"Current Balance for {self.name}: ₹{self.balance}")

    def display_details(self):
        print(f"\nAccount No: {self.acc_no}")
        print(f"Name: {self.name}")
        print(f"Balance: ₹{self.balance}\n")


# Dictionary to store account objects
accounts = {}

def main():
    while True:
        print("\n====== BANKING MENU ======")
        print("1. New Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Balance Enquiry")
        print("5. Show All Accounts")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            acc_no = input("Enter Account Number: ")
            if acc_no in accounts:
                print("Account already exists.")
            else:
                name = input("Enter Account Holder Name: ")
                initial = float(input("Enter Initial Deposit: "))
                accounts[acc_no] = BankAccount(acc_no, name, initial)
                print("Account created successfully!")

        elif choice == '2':
            acc_no = input("Enter Account Number: ")
            if acc_no in accounts:
                amount = float(input("Enter amount to deposit: "))
                accounts[acc_no].deposit(amount)
            else:
                print("Account not found.")

        elif choice == '3':
            acc_no = input("Enter Account Number: ")
            if acc_no in accounts:
                amount = float(input("Enter amount to withdraw: "))
                accounts[acc_no].withdraw(amount)
            else:
                print("Account not found.")

        elif choice == '4':
            acc_no = input("Enter Account Number: ")
            if acc_no in accounts:
                accounts[acc_no].show_balance()
            else:
                print("Account not found.")

        elif choice == '5':
            if accounts:
                for acc in accounts.values():
                    acc.display_details()
            else:
                print("No accounts available.")

        elif choice == '6':
            print("Exiting... Thank you for using our banking system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
