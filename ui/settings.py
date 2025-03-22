from PyQt5 import QtGui
# 从上级目录读取json
import json
import os
# 获取当前文件所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取上级目录
parent_dir = os.path.dirname(current_dir)
with open(parent_dir + '\\config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

if config["use_path"]:
    PATH = config['test_path']
else:
    PATH = "ui/"

class Settings:
    def __init__(self):
        self.version = config['version']

        self.screen_width = 1300
        self.screen_height = 800
        self.listitem_height = 60
        self.list_font = QtGui.QFont()
        self.list_font.setFamily("微软雅黑")
        self.list_font.setPointSize(14)

        self.funlist = {
    "    Home" : "icons\\主页.png",
    "    MCID" : "icons\\查询.png",
}