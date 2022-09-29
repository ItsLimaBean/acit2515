from customer import Customer

class Account:
    def __init__(self, customer):
        if not isinstance(customer, Customer):
            raise AttributeError("not type Customer")
        self.owner = customer
        self.amount = 0.0

    def deposit(self, amount):
        if amount < 0:
            raise AttributeError("Amount is < 0")
        self.amount += amount
    
    def withdraw(self, amount):
        if amount < 0:
            raise AttributeError("Amount is < 0")
        self.amount -= amount

    def transfer(self, account, amount):
        if not isinstance(account, Account):
            raise TypeError("account is not type Account")
        self.withdraw(amount)
        account.deposit(amount)

    def compute_interest(self):
        pass

class CreditAccount(Account):
    def __init__(self, interest_rate):
        super().__init__()
        self.interest = interest_rate

    def compute_interest(self):
        if self.amount < 0:
            self.amount = self.amount * (100 + self.interest) / 100
            self.withdraw(10)

class SavingsAccount(Account):
    def __init__(self, interest_rate):
        super().__init__()
        self.interest = interest_rate

    def withdraw(self, amount):
        if amount > self.amount:
            raise UserWarning("Cannot withdraw more money than in account.")
        super().withdraw(amount)

    def compute_interest(self):
        self.amount = self.amount * (100 + self.interest) / 100
    