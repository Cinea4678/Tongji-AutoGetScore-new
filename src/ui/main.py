"""

  主窗口类

  Project Tongji-AutoGetScore
  Copyright (C) 2022 Cinea Zhan. All rights reserved.
  License: GNU General Public License v3.0

"""

import os
import platform
import re
import threading
import time
import json

import PyQt6.QtWidgets as QtWidgets
import PyQt6.QtCore as QtCore
import PyQt6.QtGui as QtGui

import easyTongjiapi

try:
    import src.ui.src.Ui_main as Ui_main
    import src.ui.login as Ui_login
    import src.ui.verifyMail as Ui_ve
    import src.ui.about as Ui_about
    import src.sources.static_rc
    import src.mail as mailTools
except ImportError:
    from .src import Ui_main as Ui_main
    import login as Ui_login
    import verifyMail as Ui_ve
    from .. import mail as mailTools

from loguru import logger
import requests

currentDir = os.path.dirname(os.path.abspath(__file__))

veLastSendTime = 0  # 验证邮件最后发送时间
veLastSendAddr = ''

stop_flag = False


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
    processBarUpdateSignal = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_main.Ui_MainWindow()
        self.ui.setupUi(self)

        # 初始化窗口
        self.setFixedSize(1043, 702)
        self.setWindowIcon(QtGui.QIcon(os.path.abspath(os.path.join(currentDir, "../sources/nmck_bb.ico"))))
        self.ui.queryTimeEdit.setValue(30.0)

        # 初始化表格
        self.ui.scoreTable.setColumnCount(6)
        self.ui.scoreTable.setRowCount(0)
        self.ui.scoreTable.verticalHeader().setVisible(False)
        self.ui.scoreTable.setHorizontalHeaderLabels(['课号', '课程名', '学分', '成绩', '是否通过', '更新时间'])
        self.ui.scoreTable.setEditTriggers(QtWidgets.QTableWidget.EditTrigger.NoEditTriggers)
        self.ui.scoreTable.setSelectionMode(QtWidgets.QTableWidget.SelectionMode.NoSelection)
        columnWidth = [150, 200, 100, 150, 100, 275]
        for index in range(self.ui.scoreTable.columnCount()):
            self.ui.scoreTable.setColumnWidth(index, columnWidth[index])

        # 连接信号与槽
        self.ui.selectTermComboBox_2.currentIndexChanged.connect(self.selectTerm_IndexChange)
        self.ui.mailConfirmBtn_2.clicked.connect(self.mailConfirmBtn_Click)
        self.ui.delayTimeOK.clicked.connect(self.delayTimeOK_Click)
        self.ui.startButton.clicked.connect(self.startButton_Click)
        self.ui.aboutBtn.clicked.connect(self.showAboutDialog)

        # 注册信号
        self.loggerSubmitSignal.connect(self.updateLog)
        self.logger = LogOutput(self.loggerSubmitSignal)
        self.processBarUpdateSignal.connect(self.updateProcessBar)

        # 初始化其他变量
        self.term = 0
        self.mail = ""
        self.delay = 30.0
        self.running = False
        self.queryThread = None

        # 登录
        self.session = easyTongjiapi.Session()
        loginDialog = Ui_login.LoginDialog(self.session)
        if loginDialog.exec() != 1:
            logger.info("用户取消登录")
            os._exit(0)

        # 加载学生数据
        selfData: easyTongjiapi.Student = self.session.studentData
        if not selfData:
            self.logger.error("获取学生数据失败！")
            QtWidgets.QMessageBox.critical(self, "连接出错", "连接到一系统时出错，为了保证您的体验，程序即将自动退出。")
            os._exit(0)
        self.ui.nameLabel.setText(selfData.name)
        self.ui.fLabel.setText(selfData.facultyName)
        self.ui.gradeLabel.setText(selfData.grade)

        # 加载学期数据
        self.ui.label.setText("1系统已登录")
        scoreData: easyTongjiapi.Scores = self.session.getScore()
        self.scores = scoreData
        if not scoreData:
            self.logger.error("获取学期数据失败！")
            QtWidgets.QMessageBox.critical(self, "连接出错", "连接到一系统时出错，为了保证您的体验，程序即将自动退出。")
            os._exit(0)
        self.ui.selectTermComboBox_2.removeItem(0)
        if scoreData.termNum == 0:
            self.ui.selectTermComboBox_2.addItem("第一学年 上学期")
            QtWidgets.QMessageBox.warning(self, "您是新生吗", "您在1系统中目前没有成绩信息，若启动查询，将默认查询您的第一个学期。\n\
            请放心，出现这种情况是正常的。")
        else:
            for term in scoreData.data['term']:
                self.ui.selectTermComboBox_2.addItem(term['termName'])
            self.updateScoreTable(0)
        self.ui.mailLineEdt.setReadOnly(False)
        self.ui.mailLineEdt.setText("")
        self.ui.statusbar.showMessage("就绪  |  关闭程序前，最好先停止查询，不然mac系统会弹窗")

    def __del__(self):
        logger.info("程序即将退出")
        os._exit(0)

    # 工具类函数

    def clearScoreTable(self):
        for _ in range(self.ui.scoreTable.rowCount()):
            self.ui.scoreTable.removeRow(0)

    def updateScoreTable(self, term: int):
        scores = self.scores
        self.clearScoreTable()
        tb = self.ui.scoreTable
        cl = scores.data['term'][term]['creditInfo']
        # '课号', '课程名', '学分', '成绩', '是否通过', '更新时间'
        for c in cl:
            rowCount = tb.rowCount()
            tb.insertRow(rowCount)
            tb.setItem(rowCount, 0, QtWidgets.QTableWidgetItem(str(c['courseNum'])))
            tb.setItem(rowCount, 1, QtWidgets.QTableWidgetItem(str(c['courseName'])))
            tb.setItem(rowCount, 2, QtWidgets.QTableWidgetItem(str(c['credit'])))
            tb.setItem(rowCount, 3, QtWidgets.QTableWidgetItem(str(c['score'])))
            tb.setItem(rowCount, 4, QtWidgets.QTableWidgetItem(str(c['isPassName'])))
            tb.setItem(rowCount, 5, QtWidgets.QTableWidgetItem(str(c['updateTime'])))

    def updateLog(self, message: str):
        self.ui.outputWindow.append(message)

    # 槽函数

    def updateProcessBar(self, value):
        self.ui.progressBar.setValue(value)

    def selectTerm_IndexChange(self, index):
        if index < 0:
            return
        if index != self.term:
            self.updateScoreTable(index)
        self.term = index
        self.logger.info(f"设置了第{index + 1}个学期")

    def mailConfirmBtn_Click(self):
        mail = self.ui.mailLineEdt.text().encode("utf-8").decode("latin1")
        # noinspection RegExpRedundantEscape
        if re.match(r"^\w+@\w+\.[\w\.]+$", mail):
            # 使用作者提供的api
            global veLastSendAddr, veLastSendTime
            if veLastSendTime > 0 and veLastSendAddr == mail:
                # 已经发送过邮件，不用再联网验证
                mdlg = Ui_ve.verifyMailDialog(mail, veLastSendTime, self)
                mdlg.exec()
                return
            # noinspection SpellCheckingInspection
            res = requests.get(f"https://www.cinea.com.cn/api/sqp/check?mail={mail}", params={'code': 'ccczzz'}).json()
            if res["needVerify"]:
                veLastSendTime = res["lastSendTime"]
                veLastSendAddr = mail
                mdlg = Ui_ve.verifyMailDialog(mail, veLastSendTime, self)
                mdlg.exec()
                return
            elif not res["valid"]:
                QtWidgets.QMessageBox.warning(self, "错误", "此邮箱已被投诉禁用，请更换重试")
            else:
                veLastSendAddr = mail
                self.verifiedMail(True)
        else:
            QtWidgets.QMessageBox.warning(self, "错误", "您输入的邮箱不正确")

    def verifiedMail(self, ok: bool):
        if ok:
            mail = veLastSendAddr
            self.logger.info(f"设置了mail: {mail}")
            self.mail = mail

    def delayTimeOK_Click(self):
        delayTime = self.ui.queryTimeEdit.value()
        self.delay = delayTime
        if delayTime <= 10.0:
            QtWidgets.QMessageBox.warning(self, "高频查询警告",
                                          "您正在尝试进行高频率查询，请您务必明确以下几点内容：\n    1.成绩可能每天只出一科，高频查询没有必要；\n    2.高频查询会无意义地增加1系统负担；\n    3.高频查询可能会使您被指控破坏1系统，由此产生的后果将由且仅由您自己承担。作者本人在开发程序过程中也因大量测试被封禁过账号；\n    4.（最重要）您的高频查询可能会使网络中心升级验证系统登录复杂度，这样大家都没有办法再使用本程序了\n\n因此，本程序暂不允许进行高频查询。将为您调整频率至10秒每次。（说实话10秒每次挂一天也有八千六百多次了，不要挂太久哦）")
            delayTime = 10.0
            self.ui.queryTimeEdit.setValue(10.0)
        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setMaximum(int(delayTime))
        self.logger.info(f"设置了查询间隔：{delayTime}")

    def startButton_Click(self):
        global stop_flag
        if not self.running:
            if self.mail == '':
                QtWidgets.QMessageBox.warning(self, "错误", "您还未设置邮箱")
                return
            if platform.system() == 'Darwin':
                QtWidgets.QMessageBox.information(self, "提示", "您使用的是Apple macOS操作系统，由于苹果对后台、省电管理严格，请务必前往“系统偏好设置”—“节能”勾选“当显示器关闭时，防止Mac自动进入睡眠”并接入电源使用本程序。\n\n作者使用的是m1版mbp，不同机型可能表现不同，敬请谅。")
            elif platform.system() == 'Windows':
                QtWidgets.QMessageBox.information(self, "提示", "您使用的是Windows操作系统，为防止程序意外停止，请务必右键点击“开始菜单”，选择“电源选项”，将“接通电源后，系统将进入睡眠状态”设为“永不”并将设备接入电源。")
            else:
                # 你已经是一个成熟的linux用户了，应该学会自己为运维负责了
                pass
            self.ui.startButton.setText("停止查询")
            stop_flag = False
            self.queryThread = queryThreadClass(self, self.processBarUpdateSignal)
            self.queryThread.start()
            self.running = True
        else:
            self.ui.startButton.setText("开始查询")
            stop_flag = True
            self.running = False
            self.logger.info("查询线程即将结束...")
            self.ui.progressBar.reset()

    @staticmethod
    def showAboutDialog():
        dialog = Ui_about.aboutDialog()
        dialog.exec()


# 查询线程类
class queryThreadClass(threading.Thread):
    def __init__(self, parent: MainWindow, updateProcessBarSignal: QtCore.pyqtBoundSignal):
        super(queryThreadClass, self).__init__()
        self.parent = parent
        self.updateProcessBarSignal = updateProcessBarSignal

    def run(self) -> None:
        self.parent.logger.info("查询已开始，正在初始化...")
        grades = []
        for courses in self.parent.scores.data['term'][self.parent.term]['creditInfo']:
            grades.append(courses['id'])
        self.parent.logger.info(f"查询已开始，当前已出{len(grades)}门成绩（如果是新学期则为0门，本数量不影响查询过程）")
        totalChecked = 0
        errors = 0

        def query_once():
            newScores = self.parent.session.getScore()
            if not newScores:
                return False
            if self.parent.scores.courseNum != newScores.courseNum:
                self.parent.scores = newScores
                newGrades = []
                for course in newScores.data['term'][self.parent.term]['creditInfo']:
                    if course['id'] not in grades:
                        newGrades.append(course)
                    if len(newGrades) == 0:
                        return True
                    else:
                        message = "<h2>新出成绩提醒</h2><p>新出" + str(len(newGrades)) + "门成绩</p><hr>"
                        for newCourse in newGrades:
                            submsg = f"<p>{newCourse['publicCoursesName']}课程<b>{newCourse['courseName']}</b>，\
                            成绩为<b>{newCourse['score']}</b>。</p>"
                            message += submsg
                            grades.append(newCourse['id'])
                        message += f"<hr>当前本学期绩点<b>{newScores.data['term'][self.parent.term]['averagePoint']}</b>，总绩点<b>{newScores.gradePoint}</b><br>已修学分<b>{newScores.earnedCredits}</b>，挂科学分<b>{newScores.failedCredits}</b>。</p><p>本邮件由成绩查询服务自动发送，若您被骚扰可以将本地址添加黑名单。</p>"
                        mailTools.sendMail("新出成绩提醒", self.parent.mail, message)
                        return True
            else:
                return True

        start_time = time.time()
        while not stop_flag:
            self.updateProcessBarSignal.emit(int(time.time()-start_time))
            if time.time() - start_time < self.parent.delay:
                time.sleep(1)
                continue
            else:
                self.updateProcessBarSignal.emit(int(time.time()-start_time))
                start_time = time.time()
            totalChecked += 1
            if not query_once():
                self.parent.logger.warning(f"已完成第{totalChecked}次查询，查询不成功")
                errors += 1
            else:
                self.parent.logger.info(f"已完成第{totalChecked}次查询，查询成功")
                errors = 0
            if errors >= 5:
                self.parent.logger.error("多次查询失败，已停止查询")
                self.parent.logger.info("正在发送查询失败通知...")
                mailTools.sendMail("查询失败提醒", self.parent.mail,
                                   "<h2>多次查询成绩失败</h2><h3>目前已经停止查询，您可能需要尝试重新登录。</h3><br><p>本邮件由成绩查询服务自动发送，若您被骚扰可以将本地址添加黑名单。</p>")
                break
        self.parent.logger.info("查询已结束")
