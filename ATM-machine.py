balance = 1000

while True:
    print("""
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
""")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Your balance is:", balance)

    elif choice == "2":
        amount = int(input("Enter deposit amount: "))
        balance += amount
        print("Deposited successfully. New balance:", balance)

    elif choice == "3":
        amount = int(input("Enter withdrawal amount: "))

        if amount > balance:
            print("Insufficient funds!")
        else:
            balance -= amount
            print("Withdrawal successful. New balance:", balance)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option")