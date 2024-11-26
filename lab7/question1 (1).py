class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Your current balance is: ₹{self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
            self.check_balance()
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance! Transaction failed.")
        elif amount <= 0:
            print("Invalid withdraw amount. Please enter a positive value.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
            self.check_balance()

    def exit(self):
        print("Thank you for using the ATM. Goodbye!")

# Example usage:
atm = ATM(5000)  # Starting balance is ₹5000

while True:
    print("\nWelcome to the ATM")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")
    
    if choice == '1':
        atm.check_balance()
    elif choice == '2':
        amount = float(input("Enter amount to deposit: "))
        atm.deposit(amount)
    elif choice == '3':
        amount = float(input("Enter amount to withdraw: "))
        atm.withdraw(amount)
    elif choice == '4':
        atm.exit()
        break
    else:
        print("Invalid choice. Please select a valid option.")