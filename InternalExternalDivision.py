from cmath import exp
from multiprocessing.sharedctypes import Value
import sys
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

#SpotAx(y), SpotBx(y), BEm(n), Result, ErrerMessage, ResuBu

def CarculDistance(a, b, c, d):
    dis = ((a - c) ** 2 + (b - d) ** 2) **(1/2)
    return dis

def InternalX(a, b, c, d):
    InterX = (c * b + d * a) / (c + d)
    return InterX
def InternalY(a, b, c, d):
    InterY = (c * b + d * a) / (c + d)
    return InterY
def ExternalX(a, b, c, d):
    ExterX = (c * b - d * a) / (c - d)
    return ExterX
def ExternalY(a, b, c, d):
    ExterY = (c * b - d * a) / (c - d)
    return ExterY


form_class = uic.loadUiType('InternalExternalDivisionUI.ui')[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.ResuBu.clicked.connect(self.result)


    def result(self):
        try:
            Ax = float(self.SpotAx.text())
            Ay = float(self.SpotAy.text())
            Bx = float(self.SpotBx.text())
            By = float(self.SpotBy.text())
            m = float(self.BEm.text())
            n = float(self.BEn.text())
            self.ErrorMessage.setText(f"에러 : 없음")
#-------------------------------------------------------------------
            Ix = InternalX(Ax, Bx, m, n)
            Iy = InternalY(Ay, By, m, n)
            Ex = ExternalX(Ax, Bx, m, n)
            Ey = ExternalY(Ay, By, m, n)
#-------------------------------------------------------------------
            CirMidX = (Ix + Ex) / 2
            CirMidY = (Iy + Ey) / 2
#-------------------------------------------------------------------
            Dist = CarculDistance(CirMidX, CirMidY, Ix, Iy)
            self.Result.setText(f"원의 중심좌표 : ({round(CirMidX, 3)}, {round(CirMidY, 3)}) / 반지름 : {round(Dist, 3)}")
        except ValueError:
            self.ErrorMessage.setText(f"에러 : 문자가 입력되어있거나 칸이 비어있음")

    



        


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()