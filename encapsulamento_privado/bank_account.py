class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}, New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}, New Balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds")

    def get_balance(self):
        return self.__balance

# Usage
account = BankAccount(100)
account.deposit(50)
account.withdraw(20)
print(f"Final Balance: {account.get_balance()}")
