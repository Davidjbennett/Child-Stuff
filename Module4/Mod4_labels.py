#from Module4.breezypythongui import EasyFrame
from breezypythongui import EasyFrame

class Mod4GuiLbls(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,
                            title='Mod 4 Class Code', 
                            width=650, 
                            height=400, 
                            background='blue')
        #a label is usually just text
        self.addLabel(text="(0,0)", row=0, column=0, sticky='NSEW', background='green')
        self.addLabel(text="(1,0)", row=1, column=0, sticky='SEW', background='aquamarine')
        self.addLabel(text="(0,1)", row=0, column=1, sticky='N', background='yellow')
        self.addLabel(text="(1,1)", row=1, column=1, sticky='SE', background='orange')

def main():
    Mod4GuiLbls().mainloop()

if __name__ == "__main__":
    main()