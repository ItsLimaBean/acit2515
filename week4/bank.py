from customer import Customer
from account import Account, CreditAccount, SavingsAccount
class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def create_account(self, category, owner, interest_rate = 0):
        if not isinstance(owner, Customer):
            raise TypeError("owner not type Cutomer!")
        
        account = None
        if category == "account":
            account = Account(owner)
        elif category == "credit":
            account = CreditAccount(owner, interest_rate)
        elif category == "savings":
            account = SavingsAccount(owner, interest_rate)

        self.accounts.append(account)
        return account

    def compute_interest(self):
        for account in self.accounts:
            account.compute_interest()
        
    def find_accounts(self, name):
        accounts = []
        for account in self.accounts:
            if account.owner.name == name:
                accounts.append(account)

        return accounts