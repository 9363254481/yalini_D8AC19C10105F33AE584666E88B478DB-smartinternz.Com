def display_balance(self): print(f"Account (self._account_number} balance: ${self._account_balance:.2f}")

# Testing the BankAccount class

if_name_ == "__main___":

# Create a BankAccount instance account1 = BankAccount("123456", "John Doe", 1000.0)

# Deposit money account1.deposit(500.0)

#Withdraw money account1.withdraw(200.0)

# Display balance

account1.display_balance()def deposit(self, amount):

if amount > 0: self._account_balance += amount print(f"Deposited ${amount:.2f} into account {self._account_number}") else:

print("Invalid deposit amount. Please deposit a positive amount.")

def withdraw(self, amount):

if amount > 0: if self._account_balance >= amount: self._account_balance-= amount print(f"Withdrew ${amount:.2f) from account {self._account_number}") else: print("Insufficient balance. Cannot withdraw.") print("Invalid withdrawal amount.