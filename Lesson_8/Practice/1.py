class BankAccount:
    def __init__(self: BankAccount, balance = 0):
        self.__balance = balance

    def __check_amount(self: BankAccount, amount):
        try:
            amount = float(amount)
        except (ValueError, TypeError):
            raise ValueError("Amount must ba a number")

        if amount <= 0:
            raise ValueError("Amount must be positive.")

        return amount

    def deposit(self: BankAccount, amount: float):
        amount = self.__check_amount(amount)
        self.__balance += amount 
        print(f"Balance: {self.__balance}, deposit: {amount}")

    def withdraw(self: BankAccount, amount: float):
        amount = self.__check_amount(amount)
        if amount > self.__balance:
            raise OverflowError("Not enough balance")
        self.__balance -= amount 
        print(f"Balance: {self.__balance}, withdraw: {amount}")

my_acc = BankAccount()
print(isinstance(my_acc, BankAccount))
try:
    my_acc.deposit(203.43)
    my_acc.withdraw(20.79)
    my_acc.deposit("333")
    my_acc.withdraw(300)
except ValueError as error:
    print(f"ValueError: {error}")
except OverflowError as error:
    print(f"OverflowError: {error}")