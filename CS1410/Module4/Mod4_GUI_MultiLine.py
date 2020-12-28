from breezypythongui import EasyFrame
import bookrecs as br

class MultiLineExample(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="MultiLine Example")
        self.outputArea = self.addTextArea(text="", row=0, column=0, columnspan=2, width=50, height=15)

        self.btnGetReport = self.addButton(text="open", row=1, column=0, columnspan=2, command=self.getReport)

    def getReport(self):
        self.outputArea.setText(br.report())

def main():
    MultiLineExample().mainloop()

if __name__ == "__main__":
    main()
