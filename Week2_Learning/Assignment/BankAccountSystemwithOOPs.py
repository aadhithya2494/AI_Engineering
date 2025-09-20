# Create a Python class named BankAccount to represent and manage basic banking operations.

class BankAccount:
    def __init__(self, account_holder, balance, account_type):
        self.account_holder = account_holder
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New Balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}. New Balance: {self.balance}")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Type: {self.account_type}")
        print(f"Current Balance: {self.balance}")

if __name__ == "__main__":
    account1 = BankAccount("Mohan", 1000.0, "Savings")
    account2 = BankAccount("Tom", 500.0, "Current")

    print("Initial Account Details:")
    account1.display_balance()
    account2.display_balance()
    print()

    print("Depositing Money:")
    account1.deposit(200.0)
    account2.deposit(150.0)
    print()

    print("Withdrawing Money:")
    account1.withdraw(50.0)
    account2.withdraw(700.0) #insucfficient balance
    print()

    print("Final Account Details:")
    account1.display_balance()
    account2.display_balance()