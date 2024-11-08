class BankAccount:
	def _init_(self,customer_id,name,staring_balance=0):
		self.customer_id = customer_id
		self.name = name
		self.balance = staring_balance
		self.transactions = {}

	def _str_(self):
		return f"Customer ID: {self.customerclass BankAccount:
    def __init__(self, customer_id, name, starting_balance=0):
        self.customer_id = customer_id
        self.name = name
        self.balance = starting_balance
        self.transactions = {} 

    def __str__(self):
        return f"Customer ID: {self.customer_id}\nName: {self.name}\nBalance: ${self.balance:.2f}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions['deposit'] = self.transactions.get('deposit', 0) + amount
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.transactions['withdrawal'] = self.transactions.get('withdrawal', 0) + amount
            else:
                print("Insufficient funds!")
        else:
            print("Withdrawal amount must be greater than zero.")

    def print_transactions(self):
        print("Transaction History:")
        for trans_type, amount in self.transactions.items():
            print(f"{trans_type.capitalize()}: ${amount:.2f}")

account = BankAccount(12345, "John Doe", 1000)

# Print customer info
print(account)

# Deposit and withdraw money
account.deposit(500)
account.withdraw(200)

# Print customer info again after transactions
print("\nAfter transactions:")
print(account)

# Print transaction history
account.print_transactions()
