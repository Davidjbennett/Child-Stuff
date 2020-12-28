from breezypythongui import EasyFrame

class Module4GuiCode(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, 
                            title="Module 4 Class Code", 
                            width=500, 
                            height=250, 
                            background="blue")
        self.addLabel(text="(0,0)", row=0, column=0, sticky="NSEW", background="green")
        self.addLabel(text="(1,0)", row=1, column=0, sticky='SEW', background='aquamarine')
        self.addLabel(text="(0,1)", row=0, column=1, sticky="NSE", background="yellow")
        self.addLabel(text="(1,1)", row=1, column=1, sticky="SE", background="red")

def main():
    Module4GuiCode().mainloop()

if __name__ == "__main__":
    main()
