import csv

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
    
    def transfer(self, amount, target_account):
        if 0 < amount <= self.balance:
            self.withdraw(amount)
            target_account.deposit(amount)

    def __str__(self):
        return f"{self.name}: ${self.balance:.2f}"

class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, balance=0):
        if name not in self.accounts:
            self.accounts[name] = BankAccount(name, balance)

    def get_account(self, name):
        return self.accounts.get(name)

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for account in self.accounts.values():
                writer.writerow([account.name, account.balance])
    
    def load_from_csv(self, filename):
        self.accounts.clear()
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, balance = row
                self.create_account(name, float(balance))

# Example usage
if __name__ == "__main__":
    bank = BankSystem()
    
    # Create accounts
    bank.create_account('Alice', 1000)
    bank.create_account('Bob', 500)
    
    # Deposit money
    alice = bank.get_account('Alice')
    alice.deposit(200)
    
    # Withdraw money
    alice.withdraw(100)
    
    # Transfer money
    bob = bank.get_account('Bob')
    alice.transfer(150, bob)
    
    # Print account balances
    print(alice)
    print(bob)
    
    # Save state to CSV
    bank.save_to_csv('bank_state.csv')
    
    # Load state from CSV
    new_bank = BankSystem()
    new_bank.load_from_csv('bank_state.csv')
    print(new_bank.get_account('Alice'))
    print(new_bank.get_account('Bob'))
