class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.history = TransactionHistory()

    def check_balance(self):
        return f"Account Balance: ${self.balance:.2f}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.record_transaction("Deposit", amount)
            return f"Deposited ${amount:.2f}. {self.check_balance()}"
        return "Deposit amount must be greater than zero."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.history.record_transaction("Withdrawal", amount)
            return f"Withdrew ${amount:.2f}. {self.check_balance()}"
        return "Insufficient balance or invalid amount."

    def show_history(self):
        return self.history.display()


class SavingsAccount(Account):
    def __init__(self, account_number, name, balance=0, withdraw_limit=1000):
        super().__init__(account_number, name, balance)
        self.withdraw_limit = withdraw_limit

    def withdraw(self, amount):
        if amount > self.withdraw_limit:
            return f"Withdrawal amount exceeds the limit of ${self.withdraw_limit:.2f}."
        return super().withdraw(amount)


class CurrentAccount(Account):
    def __init__(self, account_number, name, balance=0, overdraft_limit=500):
        super().__init__(account_number, name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            return f"Withdrawal exceeds overdraft limit of ${self.overdraft_limit:.2f}."
        self.balance -= amount
        self.history.record_transaction("Withdrawal", amount)
        return f"Withdrew ${amount:.2f}. {self.check_balance()}"


class CheckingAccount(Account):
    def __init__(self, account_number, name, balance=0, daily_limit=2000):
        super().__init__(account_number, name, balance)
        self.daily_limit = daily_limit
        self.daily_withdrawn = 0  # Reset this daily in a real system

    def withdraw(self, amount):
        if self.daily_withdrawn + amount > self.daily_limit:
            return f"Withdrawal exceeds daily limit of ${self.daily_limit:.2f}."
        if amount <= self.balance:
            self.daily_withdrawn += amount
            self.balance -= amount
            self.history.record_transaction("Withdrawal", amount)
            return f"Withdrew ${amount:.2f}. {self.check_balance()}"
        return "Insufficient balance."


class TransactionHistory:
    def __init__(self):
        self.transactions = []

    def record_transaction(self, transaction_type, amount):
        self.transactions.append((transaction_type, amount))

    def display(self):
        if not self.transactions:
            return "No transactions to display."
        history = "Transaction History:\n"
        for i, (trans_type, amount) in enumerate(self.transactions, 1):
            history += f"{i}. {trans_type}: ${amount:.2f}\n"
        return history


# Example Usage
if __name__ == "__main__":
    savings = SavingsAccount("12345", "Alice", 1500, withdraw_limit=500)
    print(savings.deposit(200))
    print(savings.withdraw(400))
    print(savings.withdraw(600))
    print(savings.show_history())

    current = CurrentAccount("67890", "Bob", 1000, overdraft_limit=300)
    print(current.withdraw(1200))
    print(current.withdraw(200))
    print(current.show_history())

    checking = CheckingAccount("11223", "Charlie", 2000, daily_limit=1000)
    print(checking.withdraw(700))
    print(checking.withdraw(500))
    print(checking.show_history())
