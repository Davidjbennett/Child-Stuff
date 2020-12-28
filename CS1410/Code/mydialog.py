from breezypythongui import *

class MyEasyFrame(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="My Easy Frame",width=200,height=50)
        self.addButton(text="Click",row=0,column=0,command=self.respond)

    def respond(self):
    	RespondDialog(self,'Enter Your Name')

class RespondDialog(EasyDialog):
    def __init__(self,parent,title):
        super().__init__(parent,title)

    def body(self,parent):
        self.addLabel(parent,text="First:",row=0,column=0)
        self.addLabel(parent,text="Last:",row=1,column=0)
        self.first = self.addTextField(parent,"",row=0,column=1)
        self.last = self.addTextField(parent,"",row=1,column=1)

    def apply(self):
    	self.messageBox('Thank You!','Your name is ' + self.first.get() + ' ' + self.last.get())

MyEasyFrame().mainloop()