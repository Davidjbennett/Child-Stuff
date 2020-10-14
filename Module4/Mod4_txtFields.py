#from Module4.breezypythongui import EasyFrame
from breezypythongui import EasyFrame

#easyframe in the brackets is inheritance
class Mod4GuiCode(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,
                           title='Mod 4 CC', 
                           width=250, 
                           height=100, 
                           background='blue',
                           resizable=True)

        self.lblOne = self.addLabel(text="green lbl", row=0,column=0,sticky='NSEW',background='white')
        self.btnChangeColor = self.addButton(text='Click me',row=0,column=1, columnspan=2,rowspan=1)

        self.addLabel(text='Background Color', row=1,column=0,background='red')
        self.txtLabelColor = self.addTextField(text='blue',row=1,column=1,columnspan=2)
        def changeColor(self):
            # newBackGroundColor = self.txtBackGroundColor.getText()
            # newLblColor = self.txtLblColor.getText()
            # self.setBackground(newBackGroundColor)
            self.lblOne = self.addLabel(text=(newLblColor.capitalize() + "Label"),row=0,column=4)
    
#!UNDERSTAND self. before variables
