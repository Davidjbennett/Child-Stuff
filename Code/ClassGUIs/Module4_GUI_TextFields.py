from breezypythongui import EasyFrame

class Module4GuiCode(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, 
                            title="Module 4 Class Code", 
                            width=500, 
                            height=250, 
                            background='blue')

        self.lblOne = self.addLabel(text="Green Label", row=0, column=0, sticky='NSEW', background='green')
        self.btnChangeColor = self.addButton(text='Click Me', row=0, column=1, columnspan=2, command=self.changeColor)
        
        self.addLabel(text="Background Color", row=1, column=0, background="red")
        self.txtBackgroundColor = self.addTextField(text="blue", row = 1, column = 1, columnspan=2)

        self.addLabel(text="Label Color", row = 2, column=0, background="pink")
        self.txtLabelColor = self.addTextField(text="green", row=2, column=1, columnspan=2)

    def changeColor(self):
        newBackgroundColor = self.txtBackgroundColor.getText()
        newLabelColor = self.txtLabelColor.getText()
        self.setBackground(newBackgroundColor)
        self.lblOne = self.addLabel(text=(newLabelColor.capitalize() + " Label"), row=0, column=0, background=newLabelColor, sticky='NSEW')

def main():
    Module4GuiCode().mainloop()

if __name__ == "__main__":
    main()