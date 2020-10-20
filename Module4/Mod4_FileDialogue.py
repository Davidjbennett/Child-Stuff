from breezypythongui import EasyFrame
import tkinter, tkinter.filedialog

class FileDialogueExample(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="File Dialogue Example")
        self.outputArea = self.addTextArea("", row=0, column=0, columnspan=2, width=50, height=15)

        self.btnFile = self.addButton(text="Open File", row=1, column=0, columnspan=2, command=self.openFileDialogue)

    def openFileDialogue(self):
        fList = [("Python Files", "*.py"), ("Text Files", "*.txt")]
        fileName = tkinter.filedialog.askopenfilename(parent=self, filetypes=fList)

        with open(fileName, 'r') as fileReader:
            self.outputArea.setText(fileReader.read())

def main():
    FileDialogueExample().mainloop()

if __name__ == "__main__":
    main()