
class Product:
    def __init__(self, name, price, recipe):
        self.name = name
        self.price = price
        self.recipe = recipe
    
    def get_price(self):
        return self.price

    def make(self):
        print(self.recipe)

class CashBox:
    def __init__(self):
        self.credit = 0 #why do i implement this in the init vs above it?
        self.totalRecieved = 0

    def deposit(self, amount):
        if amount not in (5,10,25,50):
            print("- INVALID AMOUNT >>>")
            return
        self.credit += amount
        print("Depositing", amount, "cents you have", self.credit, "cents credit.\n")
    
    def returnCoins(self):
        print("Returning", self.credit, "cents.\n")

    def haveYou(self, amount):
        return amount <= self.credit
        

    def deduct(self, amount):
        if self.haveYou(amount):
            self.credit -= amount
            self.totalRecieved += amount
            print("Returning", self.credit, "cents.\n")
            self.credit = 0
            
    def total(self):
        return self.totalRecieved



class Selector:
    def __init__(self, cashbox, products):
        self.cashBox = cashbox
        self.products = products
    
    def select(self, choiceIndex):
        if choiceIndex < 1 or choiceIndex > 5:
            print("- Invalid Choice >>>")

        choice = self.products[choiceIndex-1]    
        if not self.cashBox.haveYou(choice.get_price()):
            print("- Not enough money\n")
            return
        else:
            choice.make()
            self.cashBox.deduct(choice.get_price())

class CoffeeMachine:
    def __init__(self):
        self.cashBox = CashBox()
        products = []
        products.append(Product("Black", 35, "Making Black:\n\tDispensing cup\n\tDispensing coffee\n"+
                                     "\tDispensing water"))
        products.append(Product("White", 35, "Making White:\n\tDispensing cup\n\tDispensing coffee\n"+
                                     "\tDispensing creamer\n\tDispensing water"))
        products.append(Product("Sweet", 35, "Making Sweet:\n\tDispensing cup\n\tDispensing coffee\n"+
                                     "Dispensing sugar\n\tDispensing water"))
        products.append(Product("White and Sweet", 35, "Making White & Sweet:\n\tDispensing cup\n"
                                     "\tDispensing coffee\n\tDispensing creamer\n\tDispensing sugar\n"
                                     "\tDispensing water"))
        products.append(Product("Bouillon", 25, "Making Bouillon:\n\tDispensing cup\n"
                                     "\tDispensing Bouillon Powder\n\t Dispensing water\n"))
        self.selector = Selector(self.cashBox, products)

        

    def one_action(self):
        print("PRODUCT LIST: all 35 cents, except bouillon (25 cents)\n" + 
              "1=black, 2=white, 3=sweet, 4= white & sweet, 5=bouillon\n"+
              "Sample commands: insert 25, select 1\n")

        resp = input("- Your Command: ")

        resp = resp.split()
        
        if resp[0] == "quit":
            print(self.cashBox.totalRecieved)
            return False

        if resp[0] == "cancel":
            self.cashBox.returnCoins()
            return True

        elif resp[0] == "insert":
            self.cashBox.deposit(int(resp[1]))
            return True

        elif resp[0] == "select":
            self.selector.select(int(resp[1]))
            
        else:
            print("- Invalid entry")
            return True


    def totalCash(self):
        return self.cashBox.total()

def main():
    m = CoffeeMachine()
    while m.one_action():
        pass
    total = m.totalCash()
    print(f"Total cash: ${total/100:.2f}")

if __name__ == "__main__":
    main()
    