from view import View
from model import Model
from controller import Controller
from PySide6 import QtWidgets
import sys

if __name__ == "__main__":
    # as much as I'd love to move this to view.py, it doesn't seem to work then
    app = QtWidgets.QApplication()
    main_window = QtWidgets.QMainWindow()

    # init view, model and controller, starting the event loop and connecting
    # all of the pieces
    view = View(main_window)
    model = Model()
    controller = Controller(model, view)  # type: ignore
    # show main window
    main_window.show()
    # exit script if app.exec returns
    sys.exit(app.exec())
