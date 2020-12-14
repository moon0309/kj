import sys
from PyQt5.QtWidgets import *
from mainw import *  # mainwindow为子窗口py文件名
from dialog import *  # childwindow为子窗口py文件名
import numpy as np
from PyQt5.QtGui import QIcon

# 子窗口继承类
class childWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super(childWindow, self).__init__()
        # self.setWindowTitle("串口设置")
        self.setWindowFlags(QtCore.Qt.Window)
        self.setupUi(self)

# 主窗口继承类
class mainwindow(QtWidgets.QMainWindow, Ui_mywindow):
    def __init__(self):
        super(mainwindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("空间伺服机构测试系统")
        self.tabWidget3.setTabText(0, "归零")
        self.tabWidget3.setTabText(1, "角度跟踪")
        self.tabWidget3.setTabText(2, "多种速度跟踪")
        self.tabWidget3.setTabText(3, "定步驱动")
        self.tabWidget3.setTabText(4, "保持")
        self.tabWidget3.setTabText(5, "角度限位")

        self.tabWidget.setTabText(0, "数值显示")
        self.tabWidget.setTabText(1, "实时曲线")
        self.tabWidget.setTabText(2, "备用测试曲线")

        self.data1 = np.random.normal(size=100)
        self.data2 = np.random.normal(size=100)
        self.data3 = np.random.normal(size=100)
        self.data4 = np.random.normal(size=100)
        self.data5 = np.random.normal(size=100)
        self.data6 = np.random.normal(size=100)
        self.data7 = np.random.normal(size=100)

        self.data21 = np.random.normal(size=100)
        self.data22 = np.random.normal(size=100)
        self.data23 = np.random.normal(size=100)
        self.data24 = np.random.normal(size=100)

        self.data31 = np.random.normal(size=100)
        self.data32 = np.random.normal(size=100)
        self.data33 = np.random.normal(size=100)
        self.data34 = np.random.normal(size=100)
        self.data35 = np.random.normal(size=100)
        self.data36 = np.random.normal(size=100)
        self.data37 = np.random.normal(size=100)
        self.data38 = np.random.normal(size=100)

        self.data41 = np.random.normal(size=100)
        self.data42 = np.random.normal(size=100)
        self.data43 = np.random.normal(size=100)
        self.data44 = np.random.normal(size=100)
        self.data45 = np.random.normal(size=100)
        self.data46 = np.random.normal(size=100)
        self.data47 = np.random.normal(size=100)
        self.data48 = np.random.normal(size=100)

        self.curve1 = self.p1.plot(self.data1, pen='b', name="mode1")
        self.curve2 = self.p1.plot(self.data2, pen='r', name="mode2")
        self.curve3 = self.p2.plot(self.data3, pen='b', name="mode1")
        self.curve4 = self.p2.plot(self.data4, pen='r', name="mode2")
        self.curve5 = self.p3.plot(self.data5, pen='r', name="mode2")
        self.curve6 = self.p3.plot(self.data6, pen='b', name="mode1")
        self.curve7 = self.p4.plot(self.data7, pen='b', name="mode2")

        self.curve21 = self.p5.plot(self.data21, pen='b', name="mode1")
        self.curve22 = self.p5.plot(self.data22, pen='r', name="mode2")
        self.curve23 = self.p5.plot(self.data23, pen='w', name="mode1")
        self.curve24 = self.p5.plot(self.data24, pen='g', name="mode2")

        self.curve31 = self.p6.plot(self.data31, pen='b', name="mode1")
        self.curve32 = self.p6.plot(self.data32, pen='r', name="mode2")
        self.curve33 = self.p6.plot(self.data33, pen='w', name="mode1")
        # self.curve34 = self.p6.plot(self.data34, pen='g', name="mode2")
        # self.curve35 = self.p6.plot(self.data35, pen='y', name="mode1")
        # self.curve36 = self.p6.plot(self.data36, pen='b', name="mode2")
        # self.curve37 = self.p6.plot(self.data37, pen='r', name="mode1")
        # self.curve38 = self.p6.plot(self.data38, pen='#FF0500', name="mode2")

        self.curve41 = self.p7.plot(self.data41, pen='b', name="mode1")
        self.curve42 = self.p7.plot(self.data42, pen='r', name="mode2")
        self.curve43 = self.p7.plot(self.data43, pen='w', name="mode1")
        # self.curve44 = self.p7.plot(self.data44, pen='g', name="mode2")
        # self.curve45 = self.p7.plot(self.data45, pen='y', name="mode1")
        # self.curve46 = self.p7.plot(self.data46, pen='b', name="mode2")
        # self.curve47 = self.p7.plot(self.data47, pen='r', name="mode1")
        # self.curve48 = self.p7.plot(self.data48, pen='#FF0500', name="mode2")

        self.l1.setEnabled(False)
        self.l2.setEnabled(False)
        self.l3.setEnabled(False)
        self.l4.setEnabled(False)
        # self.l12.setEnabled(False)
        # self.l13.setEnabled(False)
        # self.l14.setEnabled(False)
        # self.l15.setEnabled(False)
        # self.l16.setEnabled(False)
        # self.l17.setEnabled(False)
        # self.l18.setEnabled(False)
        # self.l19.setEnabled(False)
        # self.l20.setEnabled(False)
        # self.l21.setEnabled(False)
        self.textEdit111.setPlainText('串口打开成功！\n设备连接成功！')







# 可在继承类中定义其他绑定事件及其对应的函数

# 主窗口通过按钮显示子窗口
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('./11.png'))
    main_window = mainwindow()
    child_window = childWindow()
    main_window.pushButton_177.clicked.connect(child_window.show)  # 绑定主窗口的按钮事件为显示子窗口
    main_window.show()
    sys.exit(app.exec())