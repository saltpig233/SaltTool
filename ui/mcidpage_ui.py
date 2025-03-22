"""MCID查询器的UI界面"""
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class McidPageUI(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""QWidget{background-color : rgb(255,255,255);}""")
        self.hbox = QtWidgets.QHBoxLayout()
        self.label = QtWidgets.QLabel()
        self.clicktime = 0
        self.label.setText(f"MCID查询器(尚未开发)\n这只是一个测试页面\n可扩展ui功能通过了此次测试\n你点击了按钮{self.clicktime}次")
        self.button = QtWidgets.QPushButton()
        self.button.setText("点我")
        self.button.clicked.connect(self._push)
        self.hbox.addWidget(self.label)
        self.hbox.addWidget(self.button)
        self.setLayout(self.hbox)


    def _push(self):
        self.clicktime += 1
        self.label.setText(f"MCID查询器(尚未开发)\n这只是一个测试页面\n可扩展ui功能通过了此次测试\n你点击了按钮{self.clicktime}次")


        