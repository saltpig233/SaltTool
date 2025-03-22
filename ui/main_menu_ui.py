from PyQt5 import QtCore, QtGui, QtWidgets
from .settings import Settings
from .settings import PATH
import sys



class MainUI(QtWidgets.QMainWindow):
    """主界面和索引，菜单栏"""
    def __init__(self):
        super().__init__()
        self.settings = Settings()
        self.screen_width = self.settings.screen_width
        self.screen_height = self.settings.screen_height
        self.setMinimumSize(self.screen_width, self.screen_height)
        self._addmainwindow()  # 主窗口

        # (最外层布局)菜单栏 ， listwidget ， 功能界面        
        self._addfunlist()  # funlist
        
        self._addstackwidget()  # stackwidget

        
        self.windowhbox = QtWidgets.QHBoxLayout()   # 主界面垂直布局内的水平布局(list和功能界面)
        self.windowhbox.setContentsMargins(0, 0, 0, 0)
        wgt1 = QtWidgets.QWidget()
        wgt1.setLayout(self.windowhbox)
        self.windowhbox.addWidget(self.funlist)
        self.windowhbox.addWidget(self.funs)
        self.windowhbox.setStretch(0, 454)
        self.windowhbox.setStretch(1, 1442)
        self._addmenubar()  # menubar
        self.windowvbox.addWidget(self.menubar)
        self.windowvbox.addWidget(wgt1)




        # SaltTool文字和logo


        # self.central_widget.setLayout(self.logobox)


    def resizeEvent(self, event):
        """窗口大小改变事件触发，记录窗口大小"""
        self.screen_width = event.size().width()
        self.screen_height = event.size().height()
        self.logo.setFixedSize(int(self.screen_width * 0.17), int(self.screen_width * 0.17))
        self.logo.setMargin(int(self.logo.width() * 0.05))
        self.logo.setStyleSheet(f"image : url({PATH}pictures/logo.png);font: {int(self.logo.width() * 0.07)}pt \"Arial Rounded MT Bold\";color: rgb(255, 255, 255);")
        self.iconbox.setFixedHeight(int(self.settings.screen_height * 1/25 + self.screen_height * 0.044))
        self.logotext.setStyleSheet(f"font: {13+self.logo.width() * 0.02}pt \"微软雅黑\";color: rgb(255, 255, 255);")

    def _addmainwindow(self):
        """主窗口设置"""
        self.resize(self.settings.screen_width, self.settings.screen_height)  # 窗口大小
        self.setWindowTitle('SaltTool')  # 窗口标题 
        self.central_widget = QtWidgets.QFrame()
        self.central_widget.setObjectName("central_widget")
        self.central_widget.setStyleSheet("""QFrame#central_widget{background-color : rgb(41, 44, 53);}""")
        self.setCentralWidget(self.central_widget)
        self.windowvbox = QtWidgets.QVBoxLayout()   # 主界面内的垂直布局
        self.windowvbox.setContentsMargins(0, 0, 0, 0)
        self.windowvbox.setSpacing(0)
        self.central_widget.setLayout(self.windowvbox)


    def _addmenubar(self):
        """菜单栏设置"""
        self.menubar = QtWidgets.QFrame()
        self.menubar.setFixedHeight(int(self.screen_height * 1/11))
        self.menubar.setObjectName("menubar")
        self.menubar.setStyleSheet("""
QFrame#menubar{
    background-color : rgb(32, 36, 42);
    border-bottom : 2px solid qlineargradient(spread:pad, x1:0, y1:0, x2:0.988636, y2:1, stop:0 rgba(21, 17, 17, 255), stop:1 rgba(96, 96, 102, 255));
}
""")    
        # 菜单栏左侧乌龟和文字logo
        self.turtle = QtWidgets.QLabel()
        self.turtle.setObjectName("turtle")
        self.turtle.setText("")
        self.turtle.setFixedSize(int(self.screen_height * 1/12), int(self.screen_height * 1/12))
        self.turtle.setStyleSheet(f"image : url({PATH}pictures/turtle.jpg);")
        self.text_1 = QtWidgets.QLabel()  # SaltTool标题文字
        self.text_1.setText("SaltTool")
        self.text_1.setObjectName("text_1")
        self.text_1.setStyleSheet("""QLabel#text_1{color: rgb(255, 255, 255);font: 75 13pt \"微软雅黑\";}""")
        self.text_2 = QtWidgets.QLabel()  # 介绍文字
        self.text_2.setText("- Morden GUI / Pyqt")
        self.text_2.setObjectName("text_2")
        self.text_2.setStyleSheet("""color: rgb(149, 136, 180);font: 7pt \"微软雅黑\";""")        
        self.fontbox = QtWidgets.QVBoxLayout()  # 标题文字的垂直布局
        self.fontbox.setContentsMargins(0, 0, 0, 0)
        self.fontbox.setSpacing(0)
        self.fontbox.addStretch()
        self.fontbox.addWidget(self.text_1)
        self.fontbox.addWidget(self.text_2)
        self.fontbox.addStretch()
        self.fontframe = QtWidgets.QFrame()  
        self.fontframe.setLayout(self.fontbox)
        self.logobox = QtWidgets.QHBoxLayout()  # 左侧乌龟和右侧文字的水平布局
        self.logobox.setContentsMargins(7, 0, 0, 0)
        self.logobox.setSpacing(15)
        self.logobox.addWidget(self.turtle,stretch=4)
        self.logobox.addWidget(self.fontframe,stretch=7)
        self.turtleframe = QtWidgets.QFrame()
        self.turtleframe.setLayout(self.logobox)
        self.turtleframe.setFixedWidth(int(self.screen_width * 454/(1442 + 454)))
        menubarhbox = QtWidgets.QHBoxLayout()  # 菜单栏的水平布局
        menubarhbox.setContentsMargins(0, 0, 0, 0)
        menubarhbox.setSpacing(0)
        menubarhbox.addWidget(self.turtleframe,alignment=QtCore.Qt.AlignLeft)
        self.menubar.setLayout(menubarhbox)
        
        


    def _addfunlist(self):
        """功能列表设置"""
        self.funlist = QtWidgets.QListWidget()
        self.funlist.setObjectName("funlist")
        for item_text , icon_path in self.settings.funlist.items():  # 功能列表的列表项
            item = QtWidgets.QListWidgetItem()
            item.setSizeHint(QtCore.QSize(0, self.settings.listitem_height))
            item.setText(item_text)
            icon_path = PATH + icon_path
            item.setIcon(QtGui.QIcon(icon_path))
            item.setFont(self.settings.list_font)
            self.funlist.addItem(item)        
        self.funlist.setStyleSheet("""
QListWidget#funlist{
    background-color : rgb(32, 36, 42);
    border : 0px solid rgb(43, 47, 53);
    color : rgb(255, 255, 255);
}
QListWidget#funlist::item{
    padding-left : 15px;
    border : 0px solid rgb(43, 47, 53);
    color : rgb(255, 255, 255);
}
QListView#funlist::item:selected {
    /*background-color: transparent;*/
    background-color: rgba(255, 255, 255, 50);
    border-left: 2px solid rgb(230, 133, 191);
}
QListWidget#funlist::item:hover{
    background-color: rgba(255, 255, 255, 25);
    padding-left : 20px
}          
""")
        self.funlist.clicked.connect(self._funlist_clicked)
        self.funlist.setCurrentRow(0)


    def _funlist_clicked(self):
        """功能列表点击事件"""
        # print(self.funlist.currentRow())
        pass


    def _addstackwidget(self):
        """功能界面设置"""
        self.funs = QtWidgets.QStackedWidget()
        self.funs.setObjectName("funs")
        self.funs.setStyleSheet("")
        self._mainmenu()
        self.funs.setCurrentIndex(0)


    def _mainmenu(self):
        """主界面"""
        self.mainmenu = QtWidgets.QFrame()
        self.mainmenu.setObjectName("mainmenu")
        self.mainmenu.setStyleSheet("""
QFrame#mainmenu{
    background-color : rgb(41, 44, 53)
}
""")
        # 中心的图标logo
        self.logo = QtWidgets.QLabel(self.mainmenu)
        self.logo.setObjectName("logo")
        self.logo.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        self.logo.setText(f"V {self.settings.version}")
        self.logotext = QtWidgets.QLabel()
        self.logotext.setAlignment(QtCore.Qt.AlignCenter)
        self.logotext.setText("SaltTool | 多功能桌面工具")
        self.logotext.setStyleSheet("font: 13pt \"微软雅黑\";color: rgb(255, 255, 255);")
        self.logovbox = QtWidgets.QVBoxLayout()
        self.logovbox.setContentsMargins(0, 0, 0, 0)
        self.logovbox.setSpacing(20)
        self.logovbox.addWidget(self.logo, alignment=QtCore.Qt.AlignCenter)
        self.logovbox.addWidget(self.logotext)
        self.logoframe = QtWidgets.QFrame()
        self.logoframe.setLayout(self.logovbox)

        self.iconbox = QtWidgets.QFrame()
        self.iconbox.setObjectName("iconbox")
        self.iconbox.setStyleSheet("""QPushButton:hover{background-color : rgba(255,255,255,30);}
QPushButton{
    background-color : rgba(255,255,255,0); 
}
""")
        self.iconbox.setFixedHeight(self.settings.listitem_height)
        self.button_more = QtWidgets.QPushButton()  # 按钮 ： 更多内容
        self.button_more.setText("")
        self.button_more.setFixedSize(self.iconbox.height() - 5, self.iconbox.height() - 5)
        self.button_more.setIcon(QtGui.QIcon(PATH + "icons/more.png"))
        self.button_more.setIconSize(QtCore.QSize(self.button_more.height() - 5, self.button_more.height() - 5))
        self.button_github = QtWidgets.QPushButton()  # 按钮 ： github
        self.button_github.setText("")
        self.button_github.setFixedSize(self.iconbox.height() - 5, self.iconbox.height() - 5)
        self.button_github.setIcon(QtGui.QIcon(PATH + "icons/github.png"))
        self.button_github.setIconSize(QtCore.QSize(self.button_github.height() - 5, self.button_github.height() - 5))
        self.button_qq = QtWidgets.QPushButton()  # 按钮 ： qq
        self.button_qq.setText("")
        self.button_qq.setFixedSize(self.iconbox.height() - 5, self.iconbox.height() - 5)
        self.button_qq.setIcon(QtGui.QIcon(PATH + "icons/qq.png"))
        self.button_qq.setIconSize(QtCore.QSize(self.button_qq.height() - 5, self.button_qq.height() - 5))
        self.button_update = QtWidgets.QPushButton()  # 按钮 ： 检查更新
        self.button_update.setText("")
        self.button_update.setFixedSize(self.iconbox.height() - 5, self.iconbox.height() - 5)
        self.button_update.setIcon(QtGui.QIcon(PATH + "icons/版本更新.png"))
        self.button_update.setIconSize(QtCore.QSize(self.button_update.height() - 5, self.button_update.height() - 5))
        self.iconboxhbox = QtWidgets.QHBoxLayout()
        self.iconboxhbox.setContentsMargins(0, 0, 5, 0)
        self.iconboxhbox.setSpacing(5)
        self.iconboxhbox.addStretch()
        self.iconboxhbox.addWidget(self.button_update)
        self.iconboxhbox.addWidget(self.button_qq)
        self.iconboxhbox.addWidget(self.button_github)
        self.iconboxhbox.addWidget(self.button_more)
        self.iconbox.setLayout(self.iconboxhbox)
        
        self.mainmenuvbox = QtWidgets.QVBoxLayout()
        self.mainmenuvbox.setContentsMargins(0, 0, 0, 0)
        self.mainmenuvbox.setSpacing(0)
        self.mainmenuvbox.addStretch()
        self.mainmenuvbox.addWidget(self.logoframe, alignment=QtCore.Qt.AlignCenter)
        self.mainmenuvbox.addStretch()
        self.mainmenuvbox.addWidget(self.iconbox)
        self.mainmenu.setLayout(self.mainmenuvbox)
        self.funs.addWidget(self.mainmenu)






















if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    sys.exit(app.exec_())
