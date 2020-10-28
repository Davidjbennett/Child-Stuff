from breezypythongui import EasyFrame

class Module4GuiCode(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, 
                            title="Module 4 Class Code", 
                            width=250, 
                            height=100, 
                            background='blue')

        self.colorCounter = 0
        self.addLabel(text="Green Label", row = 0, column = 0, sticky="NSEW", background="green")
        self.btnChangeColor = self.addButton(text="Click Me", row=0, column=1, columnspan=2, command=self.changeColor)

    def changeColor(self):
        if self.colorCounter == 0:
            self.setBackground("green")
            self.addLabel(text = "Purple Label", row=0, column=0, sticky="NSEW", background="purple")
        elif self.colorCounter == 1:
            self.setBackground("yellow")
            self.addLabel(text = "Orange Label", row=0, column=0, sticky="NSEW", background="orange")
        else:
            self.setBackground('blue')
            self.addLabel(text="Green Label", row=0, column=0, sticky='NSEW', background='green')
        self.colorCounter += 1
        self.colorCounter %= 3
        
def main():
    Module4GuiCode().mainloop()

if __name__ == "__main__":
    main()