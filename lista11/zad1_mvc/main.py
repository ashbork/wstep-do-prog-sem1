from view import View
from model import Model
from controller import Controller
from PySide6 import QtWidgets
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication()
    main_window = QtWidgets.QMainWindow()

    view = View(main_window)
    model = Model()
    controller = Controller(model, view)

    main_window.show()
    sys.exit(app.exec())
