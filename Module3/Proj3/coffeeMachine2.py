
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
    credit = 0
    totalRecieved = 0

    def __init__(self):
        pass

    def deposit(self, amount):
        self.credit += amount
    
    def returnCoins(self):
        returnTotal = 0
        returnTotal += self.credit
        self.credit -= self.credit
        return returnTotal

    def haveYou(self, amount):
        return amount <= self.credit
        

    def deduct(self, amount):
        if self.haveYou(amount):
            self.credit -= amount
            self.totalRecieved += amount
            print("Returning change "+ str(self.credit))

    def total(self):
        return self.totalRecieved



class Selector:
    def __init__(self, cashbox, products):
        self.cashBox = cashbox
        self.products = Product
    
    def select(self, choiceIndex):
        if choiceIndex < 1 or choiceIndex > 5:
            print("Invalid Choice")

        choice = self.products[choiceIndex-1]    
        if not self.cashBox.haveYou(choice.get_price()):
            print("Not enough money")
            return
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
            if self.cashBox.credit != 0:
                returned = self.cashBox.returnCoins()
                print("Returning", returned, "cents")
                print()
            return False
        if resp[0] == "cancel":
            returned = self.cashBox.returnCoins()
            print("Returning", returned, "cents")
            print()
            return True
        elif resp[0] == "insert":
            if resp[1] == "5" or resp[1] == "10" or resp[1] == "25" or resp[1] == "50":
                self.cashBox.deposit(int(resp[1]))
                print("- Depositing ", resp[1], "cents. You have ", self.cashBox.credit, "cents credit")
                print()
            else:
                print("- INVALID AMOUNT >>>")
                print("- We only take half-dollars, quarters, dimes, and nickels.")
                print()
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
    