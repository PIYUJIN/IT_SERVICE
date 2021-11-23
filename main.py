import sys
import os
import csv
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from IT_2021 import *
from PyQt5.QtCore import Qt

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.

form_class = uic.loadUiType("test.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.path=('','')

        self.pushButton.clicked.connect(self.loadImageFromFile)
        self.excelBtn.clicked.connect(self.loadExcelFromFile)
        self.showBtn.clicked.connect(self.showReceiptData)

    def loadImageFromFile(self):
        fileName=QFileDialog.getOpenFileName(self,"Open Image", './', "Image Files (*.png *.jpg *.bmp *.jpeg)")
        if fileName:
            print(fileName)
            self.qPixmapFileVar=QPixmap()
            self.qPixmapFileVar.load(fileName[0])
            self.qPixmapFileVar=self.qPixmapFileVar.scaledToWidth(400)
            self.label.setPixmap(self.qPixmapFileVar)
        result=main(fileName[0])
        self.label_3.setText(result)

    def loadExcelFromFile(self):
        self.path=QFileDialog.getOpenFileName(self,"Open Csv", './', "Csv Files (*.csv)")
        self.all_data=pd.read_csv(self.path[0],encoding='euc-kr')
        self.all_data=self.all_data[['날짜', '영수증번호', ' 상세내용 ', ' 지출 ']]
        self.tableWidget.setColumnCount(len(self.all_data.columns))
        self.tableWidget.setRowCount(len(self.all_data))
        self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)
        for i in range(len(self.all_data)):
            for j in range(len(self.all_data.columns)):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))
        self.tableWidget.resizeColumnsToContents()
    def showReceiptData(self):
        if os.path.isfile(self.path[0])=='':
            return print('없음')
        receiptNum=self.spinBox.value()
        print(receiptNum)
        if receiptNum==0:
            self.tableWidget.setColumnCount(len(self.all_data.columns))
            self.tableWidget.setRowCount(len(self.all_data))
            self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)
            for i in range(len(self.all_data)):
                for j in range(len(self.all_data.columns)):
                    self.tableWidget.setItem(i,j,QTableWidgetItem(str(self.all_data.iat[i,j])))
            self.tableWidget.resizeColumnsToContents()
        else:
            self.tableWidget.setColumnCount(len(self.all_data.columns))
            self.tableWidget.setRowCount(len(self.all_data))
            self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)
            for i in range(len(self.all_data)):
                for j in range(len(self.all_data.columns)):
                    if str(self.all_data.iat[i, j])==str(receiptNum):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))
            self.tableWidget.resizeColumnsToContents()



if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
'''
AttributeError: 'WindowClass' object has no attribute 'accept'
이 오류가 뜬다면 아마도 Qt Designer 등의 프로그램에서 예시로 만든 폼 템플릿이 'Main Window'가 아니어서 그럴겁니다.

예를 들어 템플릿 폼을 Dialog with Buttons 등으로 만들면 클래스 이름이 'QDialog'가 됩니다.
그리고 ui를 연결할 때 사용하는 클래스의 인자도 수정해야 합니다.
위 소스에서 class WindowClass(QMainWindow, form_class): 인 부분에서 QMainWindow를 QDialog로 바꿔주면 이상 없이 실행될겁니다.

다른 폼 템플릿을 사용했다면, 폼 생성 후 ui 파일 열어서 <class></class> 바로 아래 있는 <widget> 태그의 class 속성 값으로 넣어주면 됩니다
'''
