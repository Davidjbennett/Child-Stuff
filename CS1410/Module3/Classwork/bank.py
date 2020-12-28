from savingsaccount import SavingsAccount
import pickle

class Bank():
    def __init__(self):
        self.savings_accounts = {}

    def add(self, account):
        name = account.getName()
        pin = account.getPin()
        
        if self.savings_accounts.get((name,pin), 0) == 0:
            self.savings_accounts[(name, pin)] = account

    def remove(self, name, pin):
        if self.savings_accounts.get((name, pin), 0) != 0:
            self.savings_accounts.pop((name, pin))

    def get(self, name, pin):
        return self.savings_accounts.get((name,pin), None)

    def computerInterest(self):
        totalInterest = 0.0
        for account in self.savings_accounts:
            totalInterest += self.savings_accounts.get(account).computerInterest()
        return totalInterest
    
    def save(self, fileName = None):
        if fileName:
            with open(fileName, "wb") as fileObj:
                pickle.dump(self.savings_accounts, fileObj)

    def read(self, fileName):
        with open(fileName, "rb") as f:
            account = pickle.load(f)
            self.savings_accounts = account

if __name__ == "__main__":
    bank = Bank()
    # account = SavingsAccount("Tim", '24601', 6.50)

    # bank.add(account)
    # bank.add(account)

    # bank.remove(account.getName(), account.getPin())
    
    # print(bank.get(account.getName(), account.getPin()))
    # bank.add(account)
    # print(bank.get(account.getName(), account.getPin()))

    # bank.add(SavingsAccount("Mary", "72837", 2323.32))
    # bank.add(SavingsAccount("Bertha", "86527", 21563212.32))

    # print(bank.computerInterest())

    # bank.save("accounts.txt")

    bank.read("accounts.txt")
    print(bank.get("Tim", "24601"))

    #left off at 19:00 min in video
    
