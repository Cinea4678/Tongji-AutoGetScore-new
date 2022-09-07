"""

  主窗口类

  Project Tongji-AutoGetScore
  Copyright (C) 2022 Cinea Zhan. All rights reserved.
  License: GNU General Public License v3.0

"""

import os
import time
import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
from loguru import logger
import easyTongjiapi
import src.ui.src.Ui_main as Ui_main
import src.ui.login as Ui_login
import src.sources.static_rc

currentDir = os.path.dirname(os.path.abspath(__file__))


# 日志窗口类
class LogOutput:
    def __init__(self, updateSignal):
        self.updateSignal = updateSignal

    def info(self, name: str):
        logger.info(name)
        self.updateSignal.emit(f'{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())} | {name}')

    def warning(self, name: str):
        logger.warning(name)
        self.updateSignal.emit(
            f'{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())} | <span style="color:#ff0000;">{name}</span>')

    def error(self, name: str):
        logger.error(name)
        self.updateSignal.emit(
            f'{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())} | <span style="font-weight:600; color:#ff0000;">{name}</span>')


# 主窗口类
class MainWindow(QtWidgets.QMainWindow):
    loggerSubmitSignal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_main.Ui_MainWindow()
        self.ui.setupUi(self)

        # 初始化窗口

        self.setFixedSize(1043, 702)
        self.setWindowIcon(QtGui.QIcon(os.path.abspath(os.path.join(currentDir, "../sources/nmck_bb.ico"))))

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
        self.ui.selectTermComboBox_2.currentIndexChanged.connect(self.selectTerm_IndexChange)
        self.ui.mailConfirmBtn_2.clicked.connect(self.mailConfirmBtn_Click)
        self.ui.delayTimeOK.clicked.connect(self.delayTimeOK_Click)
        self.ui.startButton.clicked.connect(self.startButton_Click)

        # 注册信号
        self.loggerSubmitSignal.connect(self.updateLog)
        self.logger = LogOutput(self.loggerSubmitSignal)

        # 初始化其他变量
        self.term = 0

        # 登录
        self.session = easyTongjiapi.Session()
        loginDialog = Ui_login.LoginDialog(self.session)
        if loginDialog.exec() != 1:
            logger.info("用户取消登录")
            exit(0)

        # 加载学生数据
        selfData: easyTongjiapi.Student = self.session.studentData
        if not selfData:
            self.logger.error("获取学生数据失败！")
            QtWidgets.QMessageBox.critical(self, "连接出错", "连接到一系统时出错，为了保证您的体验，程序即将自动退出。")
            exit(0)
        self.ui.nameLabel.setText(selfData.name)
        self.ui.fLabel.setText(selfData.facultyName)
        self.ui.gradeLabel.setText(selfData.grade)

        # 加载学期数据
        self.ui.label.setText("1系统已登录")
        scoreData: easyTongjiapi.Scores = self.session.getScore()
        if not scoreData:
            self.logger.error("获取学期数据失败！")
            QtWidgets.QMessageBox.critical(self, "连接出错", "连接到一系统时出错，为了保证您的体验，程序即将自动退出。")
            exit(0)
        self.ui.selectTermComboBox_2.removeItem(0)
        if scoreData.termNum == 0:
            self.ui.selectTermComboBox_2.addItem("第一学年 上学期")
            QtWidgets.QMessageBox.warning(self, "您是新生吗", "您在1系统中目前没有成绩信息，若启动查询，将默认查询您的第一个学期。\n\
            请放心，出现这种情况是正常的。")
        else:
            for term in scoreData.data['term']:
                self.ui.selectTermComboBox_2.addItem(term['termName'])
        self.ui.mailLineEdt.setReadOnly(False)
        self.ui.mailLineEdt.setText("")
        self.ui.statusbar.showMessage("就绪")

    # 工具类函数

    def clearTable(self):
        self.ui.scoreTable.setRowCount(0)

    def updateLog(self, message: str):
        self.ui.outputWindow.append(message)

    # 槽函数

    def selectTerm_IndexChange(self, index):
        if index < 0:
            return
        self.logger.info(f"设置了第{index+1}个学期")

    def mailConfirmBtn_Click(self):
        print('mailConfirmBtn_Click')

    def delayTimeOK_Click(self):
        print('delayTimeOK_Click')

    def startButton_Click(self):
        print('startButton_Click')
