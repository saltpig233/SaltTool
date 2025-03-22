from ui import main_menu_ui
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import webbrowser

class MainMenu(main_menu_ui.MainUI):
    def __init__(self):
        super().__init__()
        self.button_github.clicked.connect(lambda : webbrowser.open("https://github.com/saltpig233"))
        self.button_qq.clicked.connect(lambda : webbrowser.open("https://qm.qq.com/q/zIZYuzQkL0"))

class MoreMenu(QtWidgets.QMainWindow):
    pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = MainMenu()
    ui.show()
    sys.exit(app.exec_())
