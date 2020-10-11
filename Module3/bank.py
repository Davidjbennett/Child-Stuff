from savingsaccount import SavingsAccount

class Bank():
    def __init__(self):
        self.savings_account = {}

    def add(self, account):
        name = account.getName()
        pin = account.getPin()
        
        if self.savings_account.get((name,pin), 0) == 0:
            self.savings_account[(name, pin)] = account

    def remove(self, name, pin):
        if self.savings_account.get((name, pin), 0) != 0:
            self.savings_account.pop(name, pin)
    
if __name__ == "__main__":
    bank = Bank()
    account = SavingsAccount("Tim", 24601, 6.50)

    bank.add(account)
    bank.add(account)

    bank.remove(account.getName(), account.getPin())