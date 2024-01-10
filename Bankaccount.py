class BankAccount:
    def __init__(self, account_holder_name, account_number, balance):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds. Please try again."
        else:
            self.balance -= amount
            return self.balance

    def display_balance(self):
        return self.balance

    def get_account_details(self):
        return {
            "Account Holder Name": self.account_holder_name,
            "Account Number": self.account_number,
            "Current Balance": self.display_balance()
        }

#Here is how you can use the class:

# Create a new bank account
account1 = BankAccount("John Doe", "123456789", 500)

# Deposit money into the account
account1.deposit(100)

# Withdraw money from the account
account1.withdraw(50)

# Display the current balance
print(account1.display_balance())

# Get the account details
print(account1.get_account_details())
