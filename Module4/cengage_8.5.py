import random
from breezypythongui import EasyFrame

class GuessingGame(EasyFrame):
    """Plays a guessing game with the user."""

    def __init__(self):
        """Sets up the window,widgets, and data."""
        EasyFrame.__init__(self, title = "Guessing Game")

        self.lowerBound = random.randint(0,50)
        self.upperBound = random.randint(0,50)
        self.count = 0

        self.myNumber = (self.lowerBound + self.upperBound) // 2
        guess = "Is the number " + str(self.myNumber) + "?"
        self.myLabel = self.addLabel(text = guess,
                                       row = 0, column = 0,
                                       sticky = "NSEW",
                                       columnspan = 4)
        self.small = self.addButton(text = "Too small", row = 1,
                                    column = 0, command = self.goLarge)
        self.large = self.addButton(text = "Too large", row = 1,
                                        column = 1,
                                        command = self.goSmall)
        self.correct = self.addButton(text = "Correct", row = 1,
                                        column = 2,
                                        command = self.goCorrect)
        self.newButton = self.addButton(text = "New game", row = 1,
                                        column = 3,
                                        command = self.newGame)

    def goLarge(self):
        """Guess was too small, so move guess to the right of the number."""
        self.lowerBound = self.myNumber
        
    def goSmall(self):
        """Guess was too large, so move guess to the left of the number."""
        self.upperBound = self.myNumber

    def goCorrect(self):
        """Guess was too correct, so announce and wait."""
        return False


    def newGame(self):
        """Resets the GUI to its original state."""
        # Write code here

def main():
    """Instantiate and pop up the window."""
    GuessingGame().mainloop()

if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("\nProgram closed.")