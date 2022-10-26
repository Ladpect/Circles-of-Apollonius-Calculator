from cmath import exp
import sys
from PyQt5 import uic, QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import *

def CarculDistance(a, b, c, d):    #두 점 사이 거리 구하는 함수
    dis = ((a - c) ** 2 + (b - d) ** 2) **(1/2)
    return dis

def InternalX(a, b, c, d): #내분점 X 구하는 함수
    InterX = (c * b + d * a) / (c + d) 
    return InterX
def InternalY(a, b, c, d): #내분점 Y 구하는 함수
    InterY = (c * b + d * a) / (c + d)
    return InterY
def ExternalX(a, b, c, d): #외분점 X 구하는 함수
    ExterX = (c * b - d * a) / (c - d)
    return ExterX
def ExternalY(a, b, c, d): #외분점 Y 구하는 함수
    ExterY = (c * b - d * a) / (c - d)
    return ExterY


form_class = uic.loadUiType('InternalExternalDivisionUI.ui')[0] #UI load

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.ResuBu.clicked.connect(self.result) #'계산' 버튼 누르면
                                                 #       
                                                 #       
    def result(self):                            #여기에서 실행
        try:
            Ax = float(self.SpotAx.text()) #입력란에 입력된 점 A의 x좌표 
            Ay = float(self.SpotAy.text()) #입력란에 입력된 점 A의 y좌표
            Bx = float(self.SpotBx.text()) #입력란에 입력된 점 B의 x좌표
            By = float(self.SpotBy.text()) #입력란에 입력된 점 B의 y좌표
            m = float(self.BEm.text()) #입력란에 입력된 두 점 사이 거리의 비 m
            n = float(self.BEn.text()) #입력란에 입력된 두 점 사이 거리의 비 n
            self.ErrorMessage.setText(f"에러 : 없음") #에러 메세지 초기화
#-------------------------------------------------------------------
            Ix = InternalX(Ax, Bx, m, n) #내분점 x 연산
            Iy = InternalY(Ay, By, m, n) #내분점 y 연산
            Ex = ExternalX(Ax, Bx, m, n) #외분점 x 연산
            Ey = ExternalY(Ay, By, m, n) #외분점 y 연산
#-------------------------------------------------------------------
            #내분점과 외분점의 중심을 계산. 아폴로니우스의 원 중심이 됨.
            CirMidX = (Ix + Ex) / 2 #중심 x 좌표
            CirMidY = (Iy + Ey) / 2 #중심 y 좌표
#-------------------------------------------------------------------
            Dist = CarculDistance(CirMidX, CirMidY, Ix, Iy)
            self.Result.setText(f"원의 중심좌표 : ({round(CirMidX, 3)}, {round(CirMidY, 3)}) / 반지름 : {round(Dist, 3)}")
        except ValueError:
            self.ErrorMessage.setText(f"에러 : 문자가 입력되어있거나 칸이 비어있음") #점 좌표 혹은 거리의 비 입력칸에 문자가 들어간 경우 발생할 오류 예외처리
        except ZeroDivisionError:
            self.ErrorMessage.setText(f"에러 : 거리의 비가 서로 같음.") #거리의 비가 서로 같을 때 발생하는 오류 처리

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
