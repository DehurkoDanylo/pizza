# -*- coding: utf-8 -*-



from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1031, 600)
        MainWindow.setStyleSheet("background-color: rgb(254, 255, 242);    ")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 220, 271, 291))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("2.png"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(700, 510, 113, 32))
        self.pushButton.setStyleSheet("background-color: rgb(246, 106, 0);\n"
"font: 18pt \"Georgia\";")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, -20, 1031, 221))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("124.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 520, 91, 21))
        self.label_3.setStyleSheet("font: 18pt \"Georgia\";")
        self.label_3.setObjectName("label_3")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(690, 230, 48, 24))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(10)
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(690, 260, 48, 24))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(10)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(690, 290, 48, 24))
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(10)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_4 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_4.setGeometry(QtCore.QRect(690, 320, 48, 24))
        self.spinBox_4.setMinimum(1)
        self.spinBox_4.setMaximum(10)
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_5 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_5.setGeometry(QtCore.QRect(690, 350, 48, 24))
        self.spinBox_5.setMinimum(1)
        self.spinBox_5.setMaximum(10)
        self.spinBox_5.setObjectName("spinBox_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(500, 230, 61, 21))
        self.label_4.setStyleSheet("font: 18pt \"Georgia\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(500, 260, 121, 21))
        self.label_5.setStyleSheet("font: 18pt \"Georgia\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(500, 290, 121, 21))
        self.label_6.setStyleSheet("font: 18pt \"Georgia\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(500, 320, 121, 21))
        self.label_7.setStyleSheet("font: 18pt \"Georgia\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(500, 350, 181, 21))
        self.label_8.setStyleSheet("font: 18pt \"Georgia\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(340, 180, 571, 41))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("142.png"))
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1031, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Замовити"))
        self.label_3.setText(_translate("MainWindow", "200 грн"))
        self.label_4.setText(_translate("MainWindow", "Сир"))
        self.label_5.setText(_translate("MainWindow", "Черный перец"))
        self.label_6.setText(_translate("MainWindow", "Сливки"))
        self.label_7.setText(_translate("MainWindow", "Груша"))
        self.label_8.setText(_translate("MainWindow", "Миндальные хлопья"))


if __name__ == "__main__":
    import sys
    import datetime
    print(datetime.datetime.today())
    print(datetime.datetime.today().weekday())
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    if datetime.datetime.today().weekday()==0:
        ui.label.setPixmap(QtGui.QPixmap("2.png"))
        _translate = QtCore.QCoreApplication.translate
        ui.label_3.setText(_translate("MainWindow", "100 грн"))
    elif datetime.datetime.today().weekday()==1:
        ui.label.setPixmap(QtGui.QPixmap("3.png"))
        _translate = QtCore.QCoreApplication.translate
        ui.label_3.setText(_translate("MainWindow", "200 грн"))
    elif datetime.datetime.today().weekday()==2:
        ui.label.setPixmap(QtGui.QPixmap("4.png"))
        _translate = QtCore.QCoreApplication.translate
        ui.label_3.setText(_translate("MainWindow", "100 грн"))
    elif datetime.datetime.today().weekday()==3:
        ui.label.setPixmap(QtGui.QPixmap("5.png"))
        _translate = QtCore.QCoreApplication.translate
        ui.label_3.setText(_translate("MainWindow", "200 грн"))
    elif datetime.datetime.today().weekday()==4:
        ui.label.setPixmap(QtGui.QPixmap("6.png"))
        _translate = QtCore.QCoreApplication.translate
        ui.label_3.setText(_translate("MainWindow", "100 грн"))
    elif datetime.datetime.today().weekday()==5:
        ui.label.setPixmap(QtGui.QPixmap("7.png"))
        _translate = QtCore.QCoreApplication.translate
        ui.label_3.setText(_translate("MainWindow", "200 грн"))
    elif datetime.datetime.today().weekday()==6:
        ui.label.setPixmap(QtGui.QPixmap("8.png"))
        _translate = QtCore.QCoreApplication.translate
        ui.label_3.setText(_translate("MainWindow", "100 грн"))
    elif datetime.datetime.today().weekday()==7:
        ui.label.setPixmap(QtGui.QPixmap("2.png"))
        _translate = QtCore.QCoreApplication.translate
        ui.label_3.setText(_translate("MainWindow", "200 грн"))
    MainWindow.show()
    sys.exit(app.exec_())
