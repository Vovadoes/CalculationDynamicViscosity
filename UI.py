import json
import math

from PyQt5 import QtWidgets, QtGui
from files.CalculationDynamicViscosity import Ui_MainWindow
from files.Window import Ui_Dialog
import sys


class Window(QtWidgets.QDialog):
    def __init__(self, parent, nl: str, Ee: str):
        super(Window, self).__init__()
        self.ui = Ui_Dialog()
        self.parent = parent
        self.ui.setupUi(self)
        self.ui.label.setText(nl)
        self.ui.label_2.setText(Ee)


# System consts

path_to_A = "files/student_coefficient.json"

# Consts
G = 9.81
A = None
dG = 0.006
Nmax = 5


class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.click_plus)
        self.ui.pushButton_3.clicked.connect(self.click_minus)
        self.ui.pushButton.clicked.connect(self.calculate)
        # self.ui.tableWidget.itemSelectionChanged.connect(self.on_selection)

        # self.p = 0.0
        # self.dp = 0.0
        # self.p0 = 0.0
        # self.dp0 = 0.0
        # self.l = 0.0
        # self.dl = 0.0
        # self.t = 0.0
        # self.dt = 0.0
        # self.ddnp = 0.0
        # self.run()

    def click_plus(self):
        row = self.ui.tableWidget.rowCount() + 1
        self.ui.tableWidget.setRowCount(row)
        self.ui.tableWidget.setVerticalHeaderLabels([f"d{i + 1}" for i in range(row)])
        # print(self.ui.tableWidget.item(0, 0).text())

    def click_minus(self):
        indexes = []
        for selectionRange in self.ui.tableWidget.selectedRanges():
            indexes.append(selectionRange.topRow())
        indexes.sort()
        j = 0
        for i in indexes:
            # print(f"{i=}", f"{j=}", f"{i-j=}")
            self.ui.tableWidget.removeRow(i - j)
            j += 1
        # print("click -")

    def calculate(self):
        p = self.is_float(self.ui.doubleSpinBox)
        dp = self.is_float(self.ui.doubleSpinBox_2)
        p0 = self.is_float(self.ui.doubleSpinBox_11)
        dp0 = self.is_float(self.ui.doubleSpinBox_12)
        l = self.is_float(self.ui.doubleSpinBox_13)
        dl = self.is_float(self.ui.doubleSpinBox_14)
        t = self.is_float(self.ui.doubleSpinBox_15)
        dt = self.is_float(self.ui.doubleSpinBox_16)
        ddnp = self.is_float(self.ui.doubleSpinBox_17)
        n = self.ui.tableWidget.rowCount()
        # print(n)

        measurements = []
        flag = False
        for i in range(n):
            lst = []
            for j in self.ui.tableWidget.item(i, 0), self.ui.tableWidget.item(i, 1):
                try:
                    lst.append(float(j.text()))
                    j.setBackground(QtGui.QColor(255, 255, 255))
                except:
                    j.setBackground(QtGui.QColor(255, 0, 0))
                    flag = True
                    lst.append(0.0)
            measurements.append({"d": lst[0], "dd": lst[1]})
        del lst
        if flag:
            print("error")
            return None

        # Change A to n
        with open(path_to_A, "r", encoding="UTF-8") as f:
            A = round(json.loads(f.read())[str(n)]["0.95"], 2)

        ddcn = A * math.sqrt(sum([i["dd"] ** 2 for i in measurements]) / (n * (n - 1)))

        dcp = sum([i["d"] for i in measurements]) / n

        dd = ddcn + ddnp

        E = (dG / G) + ((dp + dp0) / (p - p0)) + 2 * (dd / dcp) + (dl / l) + (dt / t)

        nl = (G / 18) * ((p - p0) / (l / 100)) * ((dcp / 1000) ** 2) * t

        dnl = nl * E

        print(f"nl = {round(nl, 10)} +- {round(dnl, 10)} Па*с")
        print(f"Ee = {round(E * 100, 2)} %")

        window = Window(
            self,
            nl=f"nl = {round(nl, 10)} +- {round(dnl, 10)} Па*с",
            Ee=f"Ee = {round(E * 100, 2)} %"
        )
        window.exec_()

    def is_float(self, value: QtWidgets.QDoubleSpinBox):
        try:
            a = float(value.value())
            value.setStyleSheet("QDoubleSpinBox {}")
            return a
        except:
            value.setStyleSheet("QDoubleSpinBox { background-color: red; }")
            raise ValueError()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
