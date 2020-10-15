from breezypythongui import EasyFrame
#from Module4.breezypythongui import EasyFrame
import Proj4

class BookRecsGui(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Book Recommendations")
        
        self.btnFriends = self.addButton(text='Freinds',row=0,column=0, command=self.getFriends)

    def getFriends(self):
        name = self.prompterBox("Friends", "Enter Readers Name")
        friends = Proj4.friends(name)
        self.messageBox("Friends of", name.capitalize(), friends)


def main():
    BookRecsGui().mainloop()

if __name__ == "__main__":
    main()
