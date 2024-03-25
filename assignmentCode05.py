#Jaylin Dinkins
from Assignment05 import *
from PyQt6 import QtCore, QtGui, QtWidgets
import sys

class FirstApp(Ui_assignment05):
    def __init__ (self, window):
        self.setupUi(window)
        #direct signal to a method in the app class
        #self.btnPush.clicked.connect(self.clickMe)
        self.calculateButton.clicked.connect(self.calcBtn)
        self.exitButton.clicked.connect(self.btnE)
        
        

    def calcBtn(self):
         name = (self.nameLine.text())
         numberOne = float(self.numberLineOne.text())
         numberTwo = float(self.numberLineTwo.text())
         numberThree = float(self.numberLineThree.text())

         sum = (numberOne + numberTwo + numberThree)
         sumOutputStr = str(round(sum,2))
         sumOutput = "Sum: " + sumOutputStr 

         product = numberOne * numberTwo * numberThree
         productOutputStr = str(round(product,2))
         productOutput = "Product: " + productOutputStr

         average = sum / 3
         averageOutputStr = str(round(average,2))
         averageOutput = "Average: " + averageOutputStr

         nameOutput = "Name: " + name

         (self.nameLabelTwo.setText(nameOutput))
         (self.averageLabel.setText(averageOutput))
         (self.productLabel.setText(productOutput))
         (self.sumLabel.setText(sumOutput))
         

    def btnE(self):
        print("Exit.")
        sys.exit()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

#Create an instance of our app
ui = FirstApp(MainWindow)

#show the window and start the app
MainWindow.show()
app.exec()