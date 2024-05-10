from PyQt6 import QtWidgets
from calc_gui import Ui_MainWindow
from logic import CalculatorLogic

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    logic = CalculatorLogic(ui)
    MainWindow.show()
    sys.exit(app.exec())
