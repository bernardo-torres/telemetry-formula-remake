import numpy as np

a = np.arange(12)
b = a = np.arange(12)
p = np.zeros((2,12))
p[0] = a
p[1] = b
p.astype(int)
print(str(p[0].astype(int)))
c = '\n'
a_str = c.join(str(x) for x in p)
print(a_str)

for i in range(0,7):
    print(i)


class Data:
    def __init__(self):
        self.test = []
        self.test.append(26)
        self.dic = {'p1': self.test}
        self.dic2 = {'p1': self.dic['p1']}

    def testfunctioin(self, lala):
        print(lala)


j = Data()
s = "j.testfunctioin"
a = eval(s)
j.testfunctioin("dka")
a("dd")

list = [a, b]
print(list[0])

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 table - pythonspot.com'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable()

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        # Show widget
        self.show()

    def createTable(self):
       # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setItem(0,0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setItem(1,0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget.setItem(1,1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget.setItem(2,0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget.setItem(2,1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget.setItem(3,0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget.setItem(3,1, QTableWidgetItem("Cell (4,2)"))
        self.tableWidget.move(0,0)

        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

    print(j.test, j.dic, j.dic['p1'], j.dic2['p1'])

    j.test[0] = 2
    print(j.test, j.dic, j.dic['p1'], j.dic2['p1'])

    j.dic['p1'][0] = 26

    print(j.test, j.dic, j.dic['p1'], j.dic2['p1'])

    k = [1,2,3,4,5,6]
    k = k[-1:] + k[:5]
    print(k[:-1], k)
