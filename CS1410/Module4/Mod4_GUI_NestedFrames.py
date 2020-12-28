from breezypythongui import EasyFrame

class PanelDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Panel Demo - v2",width=300, height=175)

        dataPanel = self.addPanel(row=0, column=0, background='lightgray')
        dataPanel.addLabel(text="Label 1", row=0, column=0, background='gray')
        dataPanel.addTextField(text="Text 1", row=0, column=1)
        dataPanel.addLabel(text="Label 2", row=1, column=0, background='darkgray')
        dataPanel.addTextField(text="Text 2", row=1, column=1)

        buttonPanel = self.addPanel(row=0, column=1, background='black')
        buttonPanel.addButton(text="B1", row=0, column=0)
        buttonPanel.addButton(text="B1", row=0, column=1)
        buttonPanel.addButton(text="B1", row=0, column=2)
        

def main():
    PanelDemo().mainloop()

if __name__ == "__main__":
    main()