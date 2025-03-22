"""MCID查询器的逻辑界面"""
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ui import mcidpage_ui


class McidPage(mcidpage_ui.McidPageUI):
    def __init__(self):
        super().__init__()
