# Form implementation generated from reading ui file 'Calculator.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(708, 573)
        self.count = 0
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 120, 113, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 120, 113, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 120, 113, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 180, 113, 71))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(110, 180, 113, 71))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(210, 180, 113, 71))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 240, 113, 71))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(110, 240, 113, 71))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(210, 240, 113, 71))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 300, 113, 71))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(110, 300, 113, 71))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(210, 300, 113, 71))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(10, 360, 113, 71))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(110, 360, 113, 71))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(210, 360, 113, 71))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(330, 120, 113, 71))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(330, 180, 113, 71))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(330, 240, 113, 71))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(330, 300, 113, 71))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(330, 360, 113, 71))
        self.pushButton_20.setObjectName("pushButton_20")
        self.radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(450, 30, 100, 20))
        self.radioButton.setObjectName("radioButton")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(450, 50, 100, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonGroup.addButton(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(550, 30, 100, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.buttonGroup.addButton(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(550, 50, 100, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.buttonGroup.addButton(self.radioButton_4)
        self.pushButton_21 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(550, 80, 113, 32))
        self.pushButton_21.setObjectName("pushButton_21")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 100, 60, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(460, 120, 201, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 190, 60, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(460, 210, 201, 51))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_22 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(550, 180, 113, 32))
        self.pushButton_22.setObjectName("pushButton_22")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 30, 431, 81))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 708, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Clear"))
        self.pushButton_2.setText(_translate("MainWindow", "Mode"))
        self.pushButton_3.setText(_translate("MainWindow", "Del"))
        self.pushButton_4.setText(_translate("MainWindow", "7"))
        self.pushButton_5.setText(_translate("MainWindow", "8"))
        self.pushButton_6.setText(_translate("MainWindow", "9"))
        self.pushButton_7.setText(_translate("MainWindow", "4"))
        self.pushButton_8.setText(_translate("MainWindow", "5"))
        self.pushButton_9.setText(_translate("MainWindow", "6"))
        self.pushButton_10.setText(_translate("MainWindow", "1"))
        self.pushButton_11.setText(_translate("MainWindow", "2"))
        self.pushButton_12.setText(_translate("MainWindow", "3"))
        self.pushButton_13.setText(_translate("MainWindow", "+/-"))
        self.pushButton_14.setText(_translate("MainWindow", "0"))
        self.pushButton_15.setText(_translate("MainWindow", "."))
        self.pushButton_16.setText(_translate("MainWindow", "/"))
        self.pushButton_17.setText(_translate("MainWindow", "*"))
        self.pushButton_18.setText(_translate("MainWindow", "-"))
        self.pushButton_19.setText(_translate("MainWindow", "+"))
        self.pushButton_20.setText(_translate("MainWindow", "="))
        self.radioButton.setText(_translate("MainWindow", "Circle"))
        self.radioButton_2.setText(_translate("MainWindow", "Rectangle"))
        self.radioButton_3.setText(_translate("MainWindow", "Square"))
        self.radioButton_4.setText(_translate("MainWindow", "Triangle"))
        self.radioButton_2.setChecked(True)
        self.pushButton_21.setText(_translate("MainWindow", "Submit"))
        self.label.setText(_translate("MainWindow", "Base"))
        self.label_2.setText(_translate("MainWindow", "Height"))
        self.pushButton_22.setText(_translate("MainWindow", "Submit"))
        self.radioButton.hide()
        self.radioButton_2.hide()
        self.radioButton_3.hide()
        self.radioButton_4.hide()
        self.label.hide()
        self.label_2.hide()
        self.pushButton_21.hide()
        self.pushButton_22.hide()
        self.lineEdit_2.hide()
        self.lineEdit.hide()
        self.radioButton.toggled.connect(lambda: self.button_state(self.radioButton))
        self.radioButton_2.toggled.connect(lambda: self.button_state(self.radioButton_2))
        self.radioButton_3.toggled.connect(lambda: self.button_state(self.radioButton_3))
        self.radioButton_4.toggled.connect(lambda: self.button_state(self.radioButton_4))

        self.pushButton_2.clicked.connect(lambda: self.mode())
        self.pushButton_14.clicked.connect(self.action_0)
        self.pushButton_10.clicked.connect(self.action_1)
        self.pushButton_11.clicked.connect(self.action_2)
        self.pushButton_12.clicked.connect(self.action_3)
        self.pushButton_7.clicked.connect(self.action_4)
        self.pushButton_8.clicked.connect(self.action_5)
        self.pushButton_9.clicked.connect(self.action_6)
        self.pushButton_4.clicked.connect(self.action_7)
        self.pushButton_5.clicked.connect(self.action_8)
        self.pushButton_6.clicked.connect(self.action_9)
        self.pushButton_20.clicked.connect(self.action_equal)
        self.pushButton_19.clicked.connect(self.action_plus)
        self.pushButton_18.clicked.connect(self.action_minus)
        self.pushButton_17.clicked.connect(self.action_mult)
        self.pushButton_16.clicked.connect(self.action_div)
        self.pushButton_3.clicked.connect(self.action_delete)
        self.pushButton_15.clicked.connect(self.action_point)
        self.pushButton.clicked.connect(self.action_clear)



    def button_state(self, b):
        if b.isChecked():
            if b.text() == 'Circle':
                self.label.setText('Radius')
                self.lineEdit_2.hide()
                self.label_2.hide()
                self.pushButton_22.hide()
            if b.text() == 'Square':
                self.label.setText('Side')
                self.lineEdit_2.hide()
                self.label_2.hide()
                self.pushButton_22.hide()
            if b.text() == 'Rectangle':
                self.label_2.show()
                self.label.setText('Base')
                self.label_2.setText('Height')
                self.lineEdit_2.show()
                self.pushButton_22.show()
            if b.text() == 'Triangle':
                self.label_2.show()
                self.label.setText('Base')
                self.label_2.setText('Height')
                self.lineEdit_2.show()
                self.pushButton_22.show()

    def mode(self):
        self.count += 1
        if self.count % 2 == 1:
            self.radioButton.show()
            self.radioButton_2.show()
            self.radioButton_3.show()
            self.radioButton_4.show()
            self.label.show()
            self.label_2.show()
            self.lineEdit_2.show()
            self.lineEdit.show()
            self.pushButton_21.show()
            self.pushButton_22.show()

        else:
            self.radioButton.hide()
            self.radioButton_2.hide()
            self.radioButton_3.hide()
            self.radioButton_4.hide()
            self.label.hide()
            self.label_2.hide()
            self.pushButton_21.hide()
            self.pushButton_22.hide()
            self.lineEdit_2.hide()
            self.lineEdit.hide()



    def action_equal(self):
        equation = self.textBrowser.text()

        try:
            ans = eval(equation)
            self.textBrowser.setText(str(ans))
        except:
            self.textBrowser.setText("Wrong Input")

    def action_plus(self):
        text = self.textBrowser.text()
        self.textBroswer.setText(text + ' + ')

    def action_minus(self):
        text = self.textBrowser.text()
        self.textBrowser.setText(text + ' - ')

    def action_div(self):
        text = self.textBrowser.text()
        self.textBrowser.setText(text + ' / ')

    def action_mult(self):
        text = self.textBrowser.text()
        self.textBrowser.setText(text + ' * ')

    def action_point(self):
        text = self.textBrowser.text()
        self.textBrowser.setText(text + '.')

    def action_1(self):
        text = self.textBrowser.text()
        self.textBrowser.setText(text + '1')

    def action_2(self):
        text = self.textBrowser.text()
        self.textBrowser.setText(text + '2')

    def action_3(self):
        text = self.textBrowser.text()
        self.textBrowser.setText(text + '3')

    def action_4(self):
        text = self.textBrowser.text()
        self.textBrowser.setText(text + '4')

    def action_5(self):
        text = self.textBrowser.text()
        self.textBrowser.setText(text + '5')

    def action_6(self):
        text = self.textBrowser.text()
        self.textBrowser.setText(text + '6')

    def action_7(self):
        text = self.textBrowser.text()
        self.textBrowser.setText(text + '7')

    def action_8(self):
        text = self.textBrowser.text()
        self.textBrowser.setText(text + '8')

    def action_9(self):
        text = self.textBrowser.text()
        self.textBrowser.setText(text + '9')

    def action_0(self):
        text = self.textBrowser.text()
        self.textBrower.setText(text + '0')

    def action_clear(self):
        self.textBrowser.clear()

    def action_delete(self):
        text = self.textBrowser.text()
        self.textBrowser.setText(text[:len(text)-1])







if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
