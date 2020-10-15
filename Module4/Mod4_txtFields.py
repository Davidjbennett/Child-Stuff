#from Module4.breezypythongui import EasyFrame
from breezypythongui import EasyFrame
import tkinter
import tkinter.messagebox

#easyframe in the brackets is inheritance
class Mod4GuiCode(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,
                           title='Mod 4 CC', 
                           width=250, 
                           height=100)
        
        self.backgroundColor = "blue"
        self.setBackground(self.backgroundColor)
        self.lblColor = "green"


        self.lblOne = self.addLabel(text="Green Label", row=0,column=0,sticky='NSEW',background=self.lblColor)
        self.btnChangeColor = self.addButton(text="Click me", row=0, column=1, columnspan=2, command=self.changeColor)

        self.addLabel(text='Background Color', row=1,column=0,background='red')
        self.txtBackgroundColor = self.addTextField(text='blue',row=1,column=1,columnspan=2)

        self.addLabel(text="Label Color",row=2,column=0,background='pink')
        self.txtLabelColor = self.addTextField(text="green", row=2,column=1,columnspan=2)

    def changeColor(self):
        oldBackground = self.backgroundColor
        oldLbl = self.lblColor
        self.backgroundColor = self.txtBackgroundColor.getText()
        self.lblColor = self.txtLabelColor.getText()

        try:
            self.setBackground(self.backgroundColor)
        except:
            self.messageBox(title="Invalid Background color", message=self.backgroundColor + "!")
            self.backgroundColor = oldBackground

        try:
            self.lblOne["background"] = self.lblColor
            self.lblOne["text"] = self.lblColor.capitalize() + "label"
        except:
            self.messageBox(title="Invalid lbl color", message = self.lblColor + "is not a valid")
            self.lblColor = oldLbl

        response = tkinter.messagebox.askyesno("Continue Changing Colors?", 'Yes or No?')
        if not response:
            self.txtBackgroundColor["state"] = "readonly"
            self.txtLabelColor["state"] = "readonly"

#!UNDERSTAND self. before variables
def main():
    Mod4GuiCode().mainloop()

if __name__ == "__main__":
    main()