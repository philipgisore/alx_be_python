class BankAccount:
    def __init__(self, balance=0):
        self.account_balance = balance

    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited ${amount}. New balance: ${self.account_balance}")

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.account_balance}")
            return True
        else:
            print("Insufficient funds")
            return False

    def display_balance(self):
        print(f"Current balance: ${self.account_balance}")
        return self.account_balance
