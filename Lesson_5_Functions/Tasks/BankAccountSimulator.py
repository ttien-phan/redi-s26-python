balance = 0
transaction_history = []


def deposit(balance, num):
    if num <= 0:
        print("Deposit not possible")
    else:
        balance += num
        transaction_history.append(("deposit", num))
        print(f"Deposit: {num}. Balance: {balance}")

    return balance


def withdraw(balance, num):
    if num > balance:
        print("Not enough money")
    elif num <= 0:
        print("Amount not correct")

    else:
        balance -= num
        transaction_history.append(("withdraw", num))
        print(f"Withdraw: {num}. Balance: {balance}")

    return balance


def check_balance(balance):
    print(f"Your current balance: {balance}")


def show_transactional_history(x):
    for trans_type, amount in x:
        print(f"{trans_type}: {amount}")


while True:
    print("\n=== BANK ACCOUNT ===")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Transaction history")
    print("5. Exit")
    choice = input("Choose your option: ")

    if choice == "1":
        amount = float(input("Amount: "))
        balance = deposit(balance, amount)
    elif choice == "2":
        amount = float(input("Amount: "))
        balance = withdraw(balance, amount)
    elif choice == "3":
        check_balance(balance)
    elif choice == "4":
        show_transactional_history(transaction_history)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option")
