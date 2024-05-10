import math


class CalculatorLogic:
    def __init__(self, ui):
        self.ui = ui
        self.setup_buttons()

    def setup_buttons(self):
        """Setup button connections"""
        self.ui.pushButton_2.clicked.connect(lambda: self.mode())
        self.ui.pushButton_14.clicked.connect(self.action_0)
        self.ui.pushButton_10.clicked.connect(self.action_1)
        self.ui.pushButton_11.clicked.connect(self.action_2)
        self.ui.pushButton_12.clicked.connect(self.action_3)
        self.ui.pushButton_7.clicked.connect(self.action_4)
        self.ui.pushButton_8.clicked.connect(self.action_5)
        self.ui.pushButton_9.clicked.connect(self.action_6)
        self.ui.pushButton_4.clicked.connect(self.action_7)
        self.ui.pushButton_5.clicked.connect(self.action_8)
        self.ui.pushButton_6.clicked.connect(self.action_9)
        self.ui.pushButton_20.clicked.connect(self.action_equal)
        self.ui.pushButton_19.clicked.connect(self.action_plus)
        self.ui.pushButton_18.clicked.connect(self.action_minus)
        self.ui.pushButton_17.clicked.connect(self.action_mult)
        self.ui.pushButton_16.clicked.connect(self.action_div)
        self.ui.pushButton_3.clicked.connect(self.action_delete)
        self.ui.pushButton_15.clicked.connect(self.action_point)
        self.ui.pushButton.clicked.connect(self.action_clear)
        self.ui.pushButton_21.clicked.connect(self.area_func)

        self.ui.radioButton.toggled.connect(lambda: self.button_state(self.ui.radioButton))
        self.ui.radioButton_2.toggled.connect(lambda: self.button_state(self.ui.radioButton_2))
        self.ui.radioButton_3.toggled.connect(lambda: self.button_state(self.ui.radioButton_3))
        self.ui.radioButton_4.toggled.connect(lambda: self.button_state(self.ui.radioButton_4))

    def button_state(self, b):

        """Handling radio button states/changes"""

        if b.isChecked():
            if b.text() == 'Circle':
                self.ui.label.setText('Radius')
                self.ui.lineEdit_2.hide()
                self.ui.label_2.hide()
                # self.pushButton_22.hide()

            if b.text() == 'Square':
                self.ui.label.setText('Side')
                self.ui.lineEdit_2.hide()
                self.ui.label_2.hide()
                # self.pushButton_22.hide()
            if b.text() == 'Rectangle':
                self.ui.label_2.show()
                self.ui.label.setText('Length')
                self.ui.label_2.setText('Width')
                self.ui.lineEdit_2.show()
                # self.pushButton_22.show()
            if b.text() == 'Triangle':
                self.ui.label_2.show()
                self.ui.label.setText('Base')
                self.ui.label_2.setText('Height')
                self.ui.lineEdit_2.show()
                # self.pushButton_22.show()

    def mode(self):
        """Toggle mode on/off"""
        self.ui.count += 1
        if self.ui.count % 2 == 1:
            self.ui.radioButton.show()
            self.ui.radioButton_2.show()
            self.ui.radioButton_3.show()
            self.ui.radioButton_4.show()
            self.ui.label.show()
            self.ui.label_2.show()
            self.ui.lineEdit_2.show()
            self.ui.lineEdit.show()
            self.ui.pushButton_21.show()
        else:
            self.ui.radioButton.hide()
            self.ui.radioButton_2.hide()
            self.ui.radioButton_3.hide()
            self.ui.radioButton_4.hide()
            self.ui.label.hide()
            self.ui.label_2.hide()
            self.ui.pushButton_21.hide()
            self.ui.lineEdit_2.hide()
            self.ui.lineEdit.hide()

    def action_equal(self):
        """Performs the calculation input into the textBrowser box"""
        equation = self.ui.textBrowser.toPlainText()
        try:
            ans = eval(equation)
            formatted_results = "{:.3f}".format(ans)
            self.ui.textBrowser.setText(formatted_results)
        except:
            self.ui.textBrowser.setText("No input")

    def action_plus(self):
        """Allows for addition of numbers put into the textBrowser box"""
        text = self.ui.textBrowser.toPlainText()
        self.ui.textBrowser.setText(text + ' + ')

    def action_minus(self):
        """Allows for subtraction of numbers put into the textBrowser box"""
        text = self.ui.textBrowser.toPlainText()
        self.ui.textBrowser.setText(text + ' - ')

    def action_div(self):
        """Allows for division of numbers put into the textBrowser box"""
        text = self.ui.textBrowser.toPlainText()
        self.ui.textBrowser.setText(text + ' / ')

    def action_mult(self):
        """Allows for multiplication of numbers put into the textBrowser box"""
        text = self.ui.textBrowser.toPlainText()
        self.ui.textBrowser.setText(text + ' * ')

    def action_point(self):
        """Appends a decimal point to the current input"""
        text = self.ui.textBrowser.toPlainText()
        self.ui.textBrowser.setText(text + '.')

    def action_1(self):
        """Appends number 1 to current input"""
        text = self.ui.textBrowser.toPlainText()
        self.ui.textBrowser.setText(text + '1')

    def action_2(self):
        """Appends number 2 to current input"""
        text = self.ui.textBrowser.toPlainText()
        self.ui.textBrowser.setText(text + '2')

    def action_3(self):
        """Appends number 3 to current input"""
        text = self.ui.textBrowser.toPlainText()
        self.ui.textBrowser.setText(text + '3')

    def action_4(self):
        """Appends number 4 to current input"""
        text = self.ui.textBrowser.toPlainText()
        self.ui.textBrowser.setText(text + '4')

    def action_5(self):
        """Appends number 5 to current input"""
        text = self.ui.textBrowser.toPlainText()
        self.ui.textBrowser.setText(text + '5')

    def action_6(self):
        """Appends number 6 to current input"""
        text = self.ui.textBrowser.toPlainText()
        self.ui.textBrowser.setText(text + '6')

    def action_7(self):
        """Appends number 7 to current input"""
        text = self.ui.textBrowser.toPlainText()
        self.ui.textBrowser.setText(text + '7')

    def action_8(self):
        """Appends number 8 to current input"""
        text = self.ui.textBrowser.toPlainText()
        self.ui.textBrowser.setText(text + '8')

    def action_9(self):
        """Appends number 9 to current input"""
        text = self.ui.textBrowser.toPlainText()
        self.ui.textBrowser.setText(text + '9')

    def action_0(self):
        """Appends number 0 to current input"""
        text = self.ui.textBrowser.toPlainText()
        self.ui.textBrowser.setText(text + '0')

    def action_clear(self):
        """Clears the textBrowser box from all input"""
        self.ui.textBrowser.clear()

    def action_delete(self):
        """Deletes last input that was inputted into textBrowser box"""
        text = self.ui.textBrowser.toPlainText()
        self.ui.textBrowser.setText(text[:len(text) - 1])

    def area_func(self):
        """Allows for the calculation of area for circle, triangle, square, and rectangle"""
        try:
            if self.ui.radioButton.isChecked():
                radius_text = self.ui.lineEdit.text()
                if not radius_text:
                    raise ValueError("Radius cannot be empty.")
                if not radius_text.replace('.', '', 1).lstrip('-').isdigit():
                    raise ValueError("Radius must be a number.")
                radius = float(radius_text)
                if radius <= 0:
                    raise ValueError("Radius must be a positive number.")
                self.ui.area = math.pi * radius ** 2
            elif self.ui.radioButton_2.isChecked():
                if self.ui.lineEdit.text() and self.ui.lineEdit_2.text():
                    length_text = self.ui.lineEdit.text()
                    width_text = self.ui.lineEdit_2.text()
                    if not (length_text.replace('.', '', 1).lstrip('-').isdigit() and width_text.replace('.', '',
                                                                                                         1).lstrip(
                            '-').isdigit()):
                        raise ValueError("Both length and width must be numbers for rectangle calculation.")
                    length = float(length_text)
                    width = float(width_text)
                    if length <= 0 or width <= 0:
                        raise ValueError("Both length and width must be positive numbers for rectangle calculation.")
                    self.ui.area = length * width
                else:
                    raise ValueError("Both length and width are required for rectangle calculation.")
            elif self.ui.radioButton_3.isChecked():
                if self.ui.lineEdit.text():
                    side_text = self.ui.lineEdit.text()
                    if not side_text.replace('.', '', 1).lstrip('-').isdigit():
                        raise ValueError("Side length must be a number for square calculation.")
                    side = float(side_text)
                    if side <= 0:
                        raise ValueError("Side length must be a positive number for square calculation.")
                    self.ui.area = side ** 2
                else:
                    raise ValueError("Side length is required for square calculation.")
            elif self.ui.radioButton_4.isChecked():
                if self.ui.lineEdit.text() and self.ui.lineEdit_2.text():
                    base_text = self.ui.lineEdit.text()
                    height_text = self.ui.lineEdit_2.text()
                    if not (base_text.replace('.', '', 1).lstrip('-').isdigit() and height_text.replace('.', '',
                                                                                                        1).lstrip(
                            '-').isdigit()):
                        raise ValueError("Both base and height must be numbers for triangle calculation.")
                    base = float(base_text)
                    height = float(height_text)
                    if base <= 0 or height <= 0:
                        raise ValueError("Both base and height must be positive numbers for triangle calculation.")
                    self.ui.area = 0.5 * base * height
                else:
                    raise ValueError("Both base and height are required for triangle calculation.")
            else:
                raise ValueError("Please select a shape.")

            formatted_area = "{:.5g}".format(self.ui.area)
            self.ui.textBrowser.setText(f'Area: {formatted_area}')
        except ValueError as ve:
            self.ui.textBrowser.setText(str(ve))
        except Exception as e:
            self.ui.textBrowser.setText("An error occurred: " + str(e))