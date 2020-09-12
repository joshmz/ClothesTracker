#Imports
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from productTrack import *

class Ui_MainWindow(object):

        #Setting Window Data
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 480) #Width x Height
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Setting Title Data
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(60, 20, 231, 41)) #Xpos, YPos, W, H
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setFrameShape(QtWidgets.QFrame.Box)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")

        #Setting Product Input Data
        self.ProductInput = QtWidgets.QLineEdit(self.centralwidget)
        self.ProductInput.setGeometry(QtCore.QRect(50, 180, 113, 32))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.ProductInput.setFont(font)
        self.ProductInput.setAlignment(QtCore.Qt.AlignCenter)
        self.ProductInput.setObjectName("ProductInput")

        #Setting Retail Input Data
        self.RetailInput = QtWidgets.QLineEdit(self.centralwidget)
        self.RetailInput.setGeometry(QtCore.QRect(50, 260, 113, 32))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.RetailInput.setFont(font)
        self.RetailInput.setAlignment(QtCore.Qt.AlignCenter)
        self.RetailInput.setObjectName("RetailInput")

        #Setting Resale Data
        self.ResaleInput = QtWidgets.QLineEdit(self.centralwidget)
        self.ResaleInput.setGeometry(QtCore.QRect(50, 340, 113, 32))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.ResaleInput.setFont(font)
        self.ResaleInput.setAlignment(QtCore.Qt.AlignCenter)
        self.ResaleInput.setObjectName("ResaleInput")

        #Setting Choice Data
        self.Choice = QtWidgets.QComboBox(self.centralwidget)
        self.Choice.setGeometry(QtCore.QRect(120, 100, 113, 32))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Choice.setFont(font)
        self.Choice.setObjectName("Choice")
        self.Choice.addItem("")
        self.Choice.addItem("")

        #Setting Shoe Size Data
        self.ShoeSize = QtWidgets.QLineEdit(self.centralwidget)
        self.ShoeSize.setGeometry(QtCore.QRect(190, 260, 113, 32))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.ShoeSize.setFont(font)
        self.ShoeSize.setAlignment(QtCore.Qt.AlignCenter)
        self.ShoeSize.setObjectName("ShoeSize")

        #Setting ComboBox Data
        self.Confirm = QtWidgets.QPushButton(self.centralwidget)
        self.Confirm.setGeometry(QtCore.QRect(190, 178, 113, 32))
        self.Confirm.clicked.connect(clicked)
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Confirm.setFont(font)
        self.Confirm.setObjectName("Confirm")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Setting Placeholder Text In Input Boxes
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Clothes Tracker"))
        self.Title.setText(_translate("MainWindow", "Clothes Tracker"))
        self.ProductInput.setPlaceholderText(_translate("MainWindow", "Product Name"))
        self.RetailInput.setPlaceholderText(_translate("MainWindow", "Retail Price"))
        self.ResaleInput.setPlaceholderText(_translate("MainWindow", "Resale Price"))
        self.ShoeSize.setPlaceholderText(_translate("MainWindow", "Shoe Size"))
        self.Choice.setItemText(0, _translate("MainWindow", "Clothing"))
        self.Choice.setItemText(1, _translate("MainWindow", "Shoes"))
        self.Confirm.setText(_translate("MainWindow", "Confirm Entry"))

#When User Clicks 'Confirm Entry'
def clicked():
    #Grabs User Entries
    prodName = (ui.ProductInput.text())
    retailPrice = (ui.RetailInput.text())
    resalePrice = (ui.ResaleInput.text())
    #Check For Item Type
    if ui.Choice.currentText() == "Clothing":
        #Use productTrack.py Class setups
        newProd = Apparel(prodName,retailPrice,resalePrice)
        newProd.addApparel() #Add To Database
    else:
        shoeSize = (ui.ShoeSize.text())
        newProd = Sneakers(prodName,retailPrice,resalePrice,shoeSize)
        newProd.addSneaker()
    #Close Current Instance Of Program And Restart
    os.execv(sys.executable,['python'] + sys.argv)
    sys.exit(app.exec_())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_()) #Clean Exit
