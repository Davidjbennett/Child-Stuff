class SavingsAccount:
    '''Defines a savings account'''

    #static variables
    RATE = 0.02
    MIN_BALANCE = 25

    def __init__(self, name, pin, balance = 0.0):
        self.name = name
        self.pin = pin 
        self.balance = balance
    
    def __str__(self):
        result = "Name: " + self.name + "\n"
        result += "PIN: " + self.pin + "\n"
        result += "Balance: " + str(self.balance)
        return result
    
    def getBalance(self):
        return self.balance
    
    def getName(self):
        return self.name
    
    def getPin(self):
        return self.pin

    def deposit(self, amount):
        '''deposits the amount into our balance'''
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            return "Amount must be >= 0"
        if self.balance < amount:
            return "Insufficient Funds"
        self.balance -= amount
        return None

    def computeInterest(self):
        interest = self.balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest



class RestrictedSavingsAccount(SavingsAccount):
    def __init__(self, name, pin, balance = 0.0, no_withdrawls_per_month = 5):
        SavingsAccount.__init__(self, name, pin, balance)
        self.max_number_of_withdrawls = no_withdrawls_per_month
        self.withdraw_count = 1

    def withdraw(self, amount):
        if self.withdraw_count > self.max_number_of_withdrawls:
            print("Youve reached monthly withdrawl limit")
        SavingsAccount.withdraw(self,amount)
        self.withdraw_count += 1
        print("Your Balance:", SavingsAccount.getBalance(self))
        

            
 
if __name__ == "__main__":
    sa = RestrictedSavingsAccount("David", 12345, 6.50)
    sa.deposit(399)
    for i in range(6):
        sa.withdraw(i)
    print(sa.computeInterest())
    print(sa.getBalance())