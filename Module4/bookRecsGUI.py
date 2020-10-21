from breezypythongui import EasyFrame
#from Module4.breezypythongui import EasyFrame
#from Module4 import Proj4
import bookrecs

class BookRecsGui(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Book Recommendations",width=300, height=60,background='powderblue')
        
        self.btnFriends = self.addButton(text='Friends',row=0,column=0, command=self.getFriends)
        self.btnRecommend = self.addButton(text='Recommend',row=0,column=1, command=self.getRecommendations)
        self.btnRecommend = self.addButton(text='Report',row=0,column=2, command=self.getReport)

    def getFriends(self):
        try:
            name = self.prompterBox("Friends", "Enter Reader Name")
            friends = bookrecs.friends(name)
            self.messageBox("Friends of " + name.capitalize(), friends, width=40, height=10)
        except KeyError:
            self.messageBox(title="Error", message="No such reader")
    
    def getRecommendations(self):
        try:
            name = self.prompterBox("Friends", "Enter Reader Name")
            bookRecs = bookrecs.recommend(name)
            brStr = ""
            for book in bookRecs:
                brStr += "Author: " + book[0] + ", " + "Book Title: " + book[1] + "\n"
            self.messageBox("Recommendations for " + name.capitalize(), brStr, width=80, height=20)
        except KeyError:
            self.messageBox(title="Error", message="No such reader")
    
    def getReport(self):
        reportList = bookrecs.report()
        self.messageBox("Report", reportList, width=80, height=30)


def main():
    BookRecsGui().mainloop()

if __name__ == "__main__":
    main()
