from breezypythongui import EasyFrame
import tkinter
import tkinter.messagebox

class Module4GuiCode(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, 
                            title="Module 4 Class Code", 
                            width=500, 
                            height=250)

        self.backgroundColor = "blue"
        self.setBackground(self.backgroundColor)
        self.labelColor = "green"
        
        self.lblOne = self.addLabel(text="Green Label", row=0, column=0, sticky='NSEW', background=self.labelColor)
        self.btnChangeColor = self.addButton(text='Click Me', row=0, column=1, columnspan=2, command=self.changeColor)
        
        self.addLabel(text="Background Color", row=1, column=0, background="red")
        self.txtBackgroundColor = self.addTextField(text="blue", row = 1, column = 1, columnspan=2)

        self.addLabel(text="Label Color", row = 2, column=0, background="pink")
        self.txtLabelColor = self.addTextField(text="green", row=2, column=1, columnspan=2)

    def changeColor(self):
        oldBackground = self.backgroundColor
        oldLabel = self.labelColor
        self.backgroundColor = self.txtBackgroundColor.getText()
        self.labelColor = self.txtLabelColor.getText()

        try:
            self.setBackground(self.backgroundColor)
        except:
            self.messageBox(title="Invalid background color", message=self.backgroundColor + " is not a valid color")
            self.backgroundColor = oldBackground

        try:
            self.lblOne["background"] = self.labelColor
            self.lblOne["text"] = self.labelColor.capitalize() + " Label"
        except:
            self.messageBox(title="Invalid label color", message=self.labelColor + " is not a valid color")
            self.labelColor = oldLabel

        response = tkinter.messagebox.askyesno('Do you want to continue changing colors?', "Yes or No?")
        if not response:
            self.txtBackgroundColor["state"] = "readonly"
            self.txtLabelColor["state"] = "readonly"

def main():
    Module4GuiCode().mainloop()

if __name__ == "__main__":
    main()