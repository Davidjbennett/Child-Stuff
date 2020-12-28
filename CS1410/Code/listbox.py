''' listbox.py: Shows a listbox inside a dialog '''

from breezypythongui import *

class MyDialog(EasyDialog):
    def __init__(self,parent,title):
        self.index = -1
        super().__init__(parent,title)

    def body(self,parent):
        ''' 
            This method is automaticaly called by Dialog.__init__ 
        '''
        self.addLabel(parent,text="Select Item:",row=0,column=0)
        self.items = self.addListbox(parent,row=1,column=0,width=10,height=5,listItemSelected=self.itemSelected)
        self.addLabel(parent,text="Your Selection:",row=0,column=1,sticky="W")
        self.choice = self.addIntegerField(parent,-1,row=1,column=1,sticky="N")
        self.itemlist = ["how","now","brown","cow"]
        self.itemlist.sort()
        self.items.insert(0,*self.itemlist)

    def itemSelected(self,index):
        ''' 
            This method is called whenever a listbox selection occurs. 
        '''
        self.index = index
        self.choice.setNumber(index)

    def validate(self):
        ''' This method is called when OK is pressed.
            If it returns True, then apply is called.
            If it returns False, apply is not called, 
            and the dialog remains active.
        '''
        if self.index == -1:
            self.messageBox('Error','No selection.')
            return False
        else:
            return True

    def apply(self):
        '''
            Called whenever validate returns True (the default).
            The dialog is destroyed when this function terminates.
        '''
        self.messageBox('Selection','You selected ' + self.itemlist[self.index] + '.')
        self.setModified()  # Must be set explicitly

class MyFrame(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="Listbox in a Dialog")
        self.addButton(text="Click",row=0,column=0,command = self.process)

    def process(self):
        if MyDialog(self,'Make a Selection').modified():
            self.messageBox('Done','Good hands!')
        else:
            self.messageBox('Huh?','You clicked Cancel :-(')

MyFrame().mainloop()
