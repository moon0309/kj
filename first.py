import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from w1 import *
from dialog1 import *
from queren import *
from warner import *
from alarm import *


# 子窗口继承类  登录界面
class childWindow1(QDialog, Ui_Dialog1):
    def __init__(self):
        super(childWindow1, self).__init__()
        # self.setWindowTitle("串口设置")
        self.setWindowFlags(QtCore.Qt.Window)
        self.setupUi(self)

# 子窗口继承类  确认信息界面
class childWindow2(QDialog, Ui_Dialogqueren):
    def __init__(self):
        super(childWindow2, self).__init__()
        # self.setWindowTitle("串口设置")
        self.setWindowFlags(QtCore.Qt.Window)
        self.setupUi(self)

# 子窗口继承类  历史记录界面
class childWindow3(QDialog, Ui_Dialog_warner):
    def __init__(self):
        super(childWindow3, self).__init__()
        # self.setWindowTitle("串口设置")
        self.setWindowFlags(QtCore.Qt.Window)
        self.setupUi(self)

# 子窗口继承类  报警界面
class childWindow4(QDialog,Ui_Dialogalarm):
    def __init__(self):
        super(childWindow4, self).__init__()
        # self.setWindowTitle("串口设置")
        self.setWindowFlags(QtCore.Qt.Window)
        self.setupUi(self)

class mainwindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mainwindow, self).__init__()
        self.setupUi(self)

        #设置窗口标题与初始大小
        self.setWindowTitle(" ")
        # win.resize(350, 250)
        #设置对象名称
        # self.setObjectName("MainWindow")

        # # #todo 1 设置窗口背景图片
        # win.setStyleSheet("#MainWindow{border-image:url(./images/python.jpg);}")

# "background-color: CornflowerBlue"



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./11.png'))
    win = mainwindow()
    # todo 2 设置窗口背景色
    child_window1 = childWindow1()
    child_window2 = childWindow2()
    child_window3 = childWindow3()
    child_window4 = childWindow4()
    child_window4.setWindowIcon(QIcon('./w.png'))
    # win.setStyleSheet("background-color: rgb(167, 182, 191)")
    # win.setStyleSheet("background-color: rgb(255, 255, 255)")
    win.setStyleSheet("border-image:url(./13.png);")
    win.pushButton.clicked.connect(child_window1.show)
    win.pushButton.clicked.connect(child_window2.show)
    win.pushButton.clicked.connect(child_window3.show)
    win.pushButton.clicked.connect(child_window4.show)


    win.show()
    sys.exit(app.exec_())