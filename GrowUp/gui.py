from PyQt5 import QtCore, QtWidgets
import sys
from crawlfn import ALLInfo
from Sendmail import Mail

class Ui_Dialog(object):
    def __init__(self):
        self.taker_Data_Set=[]

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1800, 600)

        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(50, 200, 1700,600 ))
        self.tableWidget.setIconSize(QtCore.QSize(10, 10))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.scrollToBottom()
        self.tableWidget.scrollToTop()

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(740, 150, 131, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.GetterType)

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(940, 150, 151, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.GetterCreate)


        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(700, 30, 700, 800))
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setMouseTracking(True)
        self.label.setTabletTracking(True)
        self.label.setStyleSheet("bold")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(10)
        self.label.setMidLineWidth(10)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "The Internship Monitoring System"))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['College', 'URL', ' Last Date Of Application'])
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)


        self.pushButton_2.setText(_translate("Dialog", "Crawl"))
        self.pushButton_3.setText(_translate("Dialog", "SEND MAIL"))

        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:1000;\"><b>InternSpy:The Internship Monitoring System </b></span></p></body></html>"))



    def GetterType(self):
        r = 0
        taker_Set = ALLInfo()
        print(taker_Set)
        self.tableWidget.insertRow(r)
        self.tableWidget.setItem(r, 0, QtWidgets.QTableWidgetItem(taker_Set[0]))
        self.tableWidget.setItem(r, 1, QtWidgets.QTableWidgetItem(taker_Set[1]))
        self.tableWidget.setItem(r, 2, QtWidgets.QTableWidgetItem(taker_Set[2]))
        r += 1

        self.tableWidget.setVisible(True)



    def GetterCreate(self):
        Mail()


def Caller():
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
	Caller()
