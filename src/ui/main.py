"""

  主窗口类

  Project Tongji-AutoGetScore
  Copyright (C) 2022 Cinea Zhan. All rights reserved.
  License: GNU General Public License v3.0

"""
import os

import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import src.ui.source.Ui_main as Ui_main
import easyTongjiapi


# 主窗口类
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_main.Ui_MainWindow()
        self.ui.setupUi(self)

        # 初始化窗口

        self.setFixedSize(1043, 702)
        self.setWindowIcon(QtGui.QIcon(os.path.abspath("static/nmck_bb.ico")))

        # 初始化表格
        self.ui.scoreTable.setColumnCount(6)
        self.ui.scoreTable.setRowCount(0)
        self.ui.scoreTable.verticalHeader().setVisible(False)
        self.ui.scoreTable.setHorizontalHeaderLabels(['课号', '课程名', '学分', '成绩', '是否通过', '更新时间'])
        self.ui.scoreTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.ui.scoreTable.setSelectionMode(QtWidgets.QTableWidget.NoSelection)
        columnWidth = [150, 200, 100, 150, 100, 275]
        for index in range(self.ui.scoreTable.columnCount()):
            self.ui.scoreTable.setColumnWidth(index, columnWidth[index])

        # 连接信号与槽
        self.ui.selectTermComboBox_2.currentIndexChanged.connect(self.selectTerm_InsdexChange)
        self.ui.mailConfirmBtn_2.clicked.connect(self.mailConfirmBtn_Click)
        self.ui.delayTimeOK.clicked.connect(self.delayTimeOK_Click)
        self.ui.startButton.clicked.connect(self.startButton_Click)

        # 登录
        self.session = easyTongjiapi.Session()



    # 工具类函数

    def clearTable(self):
        self.ui.scoreTable.setRowCount(0)

    # 槽函数

    def selectTerm_InsdexChange(self, index):
        print(index)

    def mailConfirmBtn_Click(self):
        print('mailConfirmBtn_Click')

    def delayTimeOK_Click(self):
        print('delayTimeOK_Click')

    def startButton_Click(self):
        print('startButton_Click')
