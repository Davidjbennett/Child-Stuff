from breezypythongui import EasyFrame
#from Module4.breezypythongui import EasyFrame
#from Module4 import Proj4
import bookrecs

class BookRecsGui(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Book Recommendations",width=450, height=250)
        
        self.btnFriends = self.addButton(text='Friends',row=0,column=0, command=self.getFriends)
        self.btnRecommend = self.addButton(text='Recommend',row=0,column=1, command=self.getRecommendations)

    def getFriends(self):
        name = self.prompterBox("Friends", "Enter Reader Name")
        friends = bookrecs.friends(name)
        self.messageBox("Friends of", name.capitalize(), friends)
    
    def getRecommendations(self):
        name = self.prompterBox("Friends", "Enter Reader Name")
        bookRecs = bookrecs.recommend(name)
        brStr = ""
        for book in bookRecs:
            brStr += book[0] + ", " + book[1] + "\n"
        self.messageBox("Recommendations for " + name.capitalize(), brStr)


def main():
    BookRecsGui().mainloop()

if __name__ == "__main__":
    main()
