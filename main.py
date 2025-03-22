"""主程序"""
from ui import main_menu_ui
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import webbrowser
import os
import json
import config
from PyQt5.QtWebEngineWidgets import QWebEngineView
from mcidpage import McidPage
import requests

class MainMenu(main_menu_ui.MainUI):
    def __init__(self):
        super().__init__()
        self.button_github.clicked.connect(lambda : webbrowser.open("https://github.com/saltpig233"))
        self.button_qq.clicked.connect(lambda : webbrowser.open("https://qm.qq.com/q/zIZYuzQkL0"))
        self.button_update.clicked.connect(self.update_)
        self.button_more.clicked.connect(self._moremenu)
        self.can_moremenu = True
        self.moremenu = None

        self.funlist.itemClicked.connect(self._open)
        self.addfuns()


    def addfuns(self):
        """添加功能页面"""
        self.mcidpage = McidPage()
        self.funs.addWidget(self.mcidpage)

    def _open(self):
        """打开对应的页面"""
        # 获取self.funlist所有列表项,并获取当前选中的列表项的文本
        item_texts = []
        for i in range(self.funlist.count()):
            item = self.funlist.item(i)
            item_texts.append(item.text())
        current_item = self.funlist.currentItem().text()
        current_index = item_texts.index(current_item)
        # 打开对应的页面
        self.funs.setCurrentIndex(current_index)

    
    def update_(self):
        """更新程序"""
        currentjson = requests.get(url="https://salttool.oss-cn-shanghai.aliyuncs.com/config.json").json()
        verson = currentjson["version"]
        if verson == config.VERSON:
            QtWidgets.QMessageBox.information(self, "提示", f"当前已是最新版本(V{config.VERSON})")
        else:
            choice = QtWidgets.QMessageBox.question(self, "提示", f"发现新版本(V{verson}),是否更新?")
            if choice == QtWidgets.QMessageBox.Yes:
                # 让用户选择下载路径
                path = QtWidgets.QFileDialog.getExistingDirectory(self, "选择下载路径", config.PATH)
                if path:
                    # 下载最新版本
                    try:
                        newfile = requests.get(url="https://salttool.oss-cn-shanghai.aliyuncs.com/SaltTool.zip")
                        with open(path + f"\\SaltTool(V{verson}).zip", "wb") as f:
                            f.write(newfile.content)
                        with open(config.PATH + "\\config.json", "w", encoding="utf-8") as f:
                            f.write(json.dumps(currentjson, indent=4, ensure_ascii=False))
                        config.VERSON = verson
                        choice2 = QtWidgets.QMessageBox.question(self, "提示", f"更新成功,请解压后运行\n是否打开下载目录?")
                        if choice2 == QtWidgets.QMessageBox.Yes:
                            os.startfile(path)
                    except:
                        QtWidgets.QMessageBox.information(self, "提示", "更新失败,请检查网络连接")
                else:
                    QtWidgets.QMessageBox.information(self, "提示", "取消更新")
            else:
                QtWidgets.QMessageBox.information(self, "提示", "取消更新")
                            
                    

    def _moremenu(self):
        if self.can_moremenu:
            self.moremenu = MoreMenu()
            self.moremenu.show()
            self.can_moremenu = False

    
    def closeEvent(self, event):
        """重写关闭事件"""
        if self.moremenu:
            self.moremenu.close()
        event.accept()


html = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>更新日志</title>
    <style>
        body {{
            font-family: 'Segoe UI', Arial, sans-serif;
            line-height: 1.6;
            margin: 2rem;
            background-color: #f5f5f5;
        }}

        .update-container {{
            max-width: 800px;
            margin: 0 auto;
            background: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}

        .header {{
            border-bottom: 2px solid #eee;
            padding-bottom: 1rem;
            margin-bottom: 1.5rem;
        }}

        .version {{
            color: #2c3e50;
            font-size: 1.8rem;
            font-weight: bold;
        }}

        .author {{
            color: #7f8c8d;
            font-size: 1.1rem;
        }}

        .update-time {{
            color: #95a5a6;
            font-size: 0.9rem;
            margin-top: 0.5rem;
        }}

        .update-content {{
            padding-left: 1.5rem;
        }}

        .update-content li {{
            margin: 0.8rem 0;
            color: #34495e;
            position: relative;
            padding-left: 1.2rem;
        }}

        .update-content li:before {{
            content: "•";
            color: #3498db;
            position: absolute;
            left: 0;
        }}
    </style>
</head>
<body>
    <div class="update-container">
        <div class="header">
            <div class="version">版本 V{config.VERSON}</div>
            <div class="author">作者：路小雨</div>
            <div class="update-time">上次更新时间：{config.UPDATE_TIME}</div>
        </div>
        
        <ul class="update-content">
            {config.LAST_UPDATE}
        </ul>
    </div>
</body>
</html>
"""


class MoreMenu(QtWidgets.QMainWindow):
    """打开更多时，弹出一个弹窗显示信息"""
    def __init__(self):
        super().__init__()
        self.resize(int(ui.screen_width / 1.5), int(ui.screen_height / 1.5))
        # 设置无边框，窗口透明
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowTitle("More")
        # 设置背景透明
        self.central_widget = QtWidgets.QFrame()
        self.central_widget.setObjectName("central_widget")
        self.central_widget.setStyleSheet("""QFrame#central_widget{background-color : rgba(41, 44, 53,150);border : 1px solid rgba(255, 255, 255,255);}""")
        self.setCentralWidget(self.central_widget)
        # menubar
        self.setmenubar()
        # HTML文本框
        self.html = QWebEngineView()
        self.html.setStyleSheet("""QTextBrowser{background-color : rgba(41, 44, 53,0);border : 1px solid rgb(25,25,25);color: rgb(255,255,255);font-size : 14px;font-family : "微软雅黑";}""")
        self.html.setHtml(html)
        
        self.windowvbox = QtWidgets.QVBoxLayout(self.central_widget)
        self.windowvbox.setContentsMargins(0, 0, 0, 0)
        self.windowvbox.setSpacing(0)
        self.windowvbox.addWidget(self.menubar)
        self.windowvbox.addWidget(self.html)


    def close_Event(self, event):
        ui.can_moremenu = True
        self.close()




    def showEvent(self, event):
        """重写showEvent事件"""
        self.elastic_animation = QtCore.QPropertyAnimation(self, b"geometry")
        self.elastic_animation.setDuration(1000)  # 动画持续时间，可按需调整
        start_rect = QtCore.QRect(self.x(), self.y(), 0, 0)
        end_rect = QtCore.QRect(self.x(), self.y(), self.width(), self.height())
        self.elastic_animation.setStartValue(start_rect)
        self.elastic_animation.setEndValue(end_rect)
        self.elastic_animation.setEasingCurve(QtCore.QEasingCurve.OutElastic)  # 弹性缓动曲线
        self.elastic_animation.start()
        super().showEvent(event)    

        
    def setmenubar(self):
        """设置菜单栏"""
        self.menubar = QtWidgets.QFrame()
        self.menubar.setObjectName("menubar")
        self.menubar.setStyleSheet("""QFrame#menubar{background-color : rgb(41, 44, 53);border : 0px solid rgb(255,255,255);}""")
        self.title = QtWidgets.QLabel()
        self.title.setStyleSheet("""QLabel{color : rgb(255,255,255);font-size : 18px;font-family : "黑体";}""")
        self.title.setText("更多信息 > > >")
        self.exitbutton = QtWidgets.QPushButton()
        self.exitbutton.setStyleSheet("""QPushButton{background-color : rgba(255,255,255,0);}QPushButton:hover{background-color : rgba(255,255,255,100);}""")
        self.exitbutton.setIcon(QtGui.QIcon(f"{config.PATH}ui/icons/关闭.png"))
        self.exitbutton.setIconSize(QtCore.QSize(20, 20))
        self.exitbutton.clicked.connect(self.close_Event)
        self.menubarhbox = QtWidgets.QHBoxLayout(self.menubar)
        self.menubarhbox.setContentsMargins(15, 0, 0, 0)
        self.menubarhbox.setSpacing(0)
        self.menubarhbox.addWidget(self.title)
        self.menubarhbox.addStretch(1)
        self.menubarhbox.addWidget(self.exitbutton)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = MainMenu()
    ui.show()
    sys.exit(app.exec_())
