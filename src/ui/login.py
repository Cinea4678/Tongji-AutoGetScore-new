"""

  登录窗口类

  Project Tongji-AutoGetScore
  Copyright (C) 2022 Cinea Zhan. All rights reserved.
  License: GNU General Public License v3.0

"""

import os
import threading
import time

import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
try:
    import src.ui.src.Ui_login as Ui_login
except ImportError:
    import src.Ui_login as Ui_login
import easyTongjiapi
from loguru import logger

currentDir = os.path.dirname(os.path.abspath(__file__))


class LoginDialog(QtWidgets.QDialog):
    submitResultSignal = QtCore.pyqtSignal(bool)

    def __init__(self, session: easyTongjiapi.Session):
        super(LoginDialog, self).__init__()
        self.ui = Ui_login.Ui_Dialog()
        self.ui.setupUi(self)

        # 初始化对话框

        self.setWindowIcon(QtGui.QIcon(os.path.abspath(os.path.join(currentDir, "../sources/nmck_bb.ico"))))
        self.ui.buttonBox.accepted.connect(self.clicked)
        self.setFixedSize(649, 480)
        self.setWindowTitle("登录到一系统")
        self.ui.progressBar.setMaximum(100)
        self.session = session
        self.submitResultSignal.connect(self.dealAccept)
        self.loginThd = None

    def clicked(self) -> None:
        if len(self.ui.stuID.text()) == 0 or len(self.ui.stuCode.text()) == 0:
            QtWidgets.QMessageBox.warning(self, "错误", "您填入的数据不完整")
            return
        self.ui.progressBar.setMaximum(0)
        self.loginThd = loginThread(self.submitResultSignal, self)
        self.loginThd.start()

    def accept(self) -> None:
        # 由其他函数处理
        pass

    def reject(self) -> None:
        if QtWidgets.QMessageBox.warning(self, "您确定要退出程序吗？", "若不登录，程序将会自动退出。",
                                         QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel,
                                         QtWidgets.QMessageBox.Cancel) == QtWidgets.QMessageBox.Cancel:
            return
        super().reject()

    def dealAccept(self, ok: bool):
        if ok:
            super(LoginDialog, self).accept()
        else:
            QtWidgets.QMessageBox.warning(self, "登录失败", "请检查学号、密码是否正确！")
            self.ui.progressBar.setMaximum(100)


class loginThread(threading.Thread):
    def __init__(self, submitResultSignal: QtCore.pyqtBoundSignal, parent: LoginDialog):
        super(loginThread, self).__init__()
        self.parent = parent
        self.submit = submitResultSignal

    def run(self) -> None:
        try:
            self.parent.session.login(self.parent.ui.stuID.text(), self.parent.ui.stuCode.text(), manual=True)
            self.submit.emit(True)
        except Exception as e:
            logger.error(str(e))
            self.submit.emit(False)
