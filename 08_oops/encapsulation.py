class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # __balance - __ means make the variable private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount(10000)
account.deposit(5000)
print(f"Balance = {account.get_balance()}")