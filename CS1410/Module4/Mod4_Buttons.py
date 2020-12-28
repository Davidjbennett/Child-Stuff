#from Module4.breezypythongui import EasyFrame
from breezypythongui import EasyFrame

class Mod4GuiBtn(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,
                            title='Mod 4 Class Code', 
                            width=650, 
                            height=400, 
                            background='blue')
        self.colorCounter = 0
        self.lblOne = self.addLabel(text="Green Lbl", row=0, column=0, sticky="NSEW", background='green')
        self.btnChangeColor = self.addButton(text="Change Color", row=0, column=1, columnspan=2, command=self.changeColor)
    
    def changeColor(self):
        if self.colorCounter == 0:
            self.setBackground('green')
            self.addLabel(text='Purple Label',row=0,column=0,sticky='NSEW', background='purple')
        elif self.colorCounter == 1:
            self.setBackground('yellow')
            self.addLabel(text='Orange Label',row=0,column=0,sticky='NSEW', background='orange')
        else:
            self.setBackground('blue')
            self.addLabel(text='Green Label',row=0,column=0,sticky='NSEW', background='green')
        self.colorCounter +=1
        self.colorCounter %=3

def main():
    Mod4GuiBtn().mainloop()

if __name__ == "__main__":
    main()