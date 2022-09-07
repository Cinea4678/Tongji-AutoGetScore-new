"""

  邮箱验证窗口类

  Project Tongji-AutoGetScore
  Copyright (C) 2022 Cinea Zhan. All rights reserved.
  License: GNU General Public License v3.0

"""

import threading
import time
import json

import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui

try:
    import src.ui.src.Ui_verifyMail as Ui_ve
except ImportError:
    import ui.src.Ui_verifyMail as Ui_ve

from loguru import logger
import requests

stopVerifyCounterDownFlag = False
veLastSendTime = 0


# 倒计时类
class timeCounterDown(threading.Thread):
    def __init__(self, btn: QtWidgets.QPushButton):
        super(timeCounterDown, self).__init__()
        self.button = btn

    def run(self) -> None:
        while not stopVerifyCounterDownFlag:
            diff = int(veLastSendTime + 60 - time.time())
            if diff > 0:
                btnText = "重新发送(%d)" % diff
                self.button.setText(btnText)
                self.button.setDisabled(True)
            else:
                self.button.setText("重新发送")
                self.button.setDisabled(False)
            time.sleep(1)


# 验证窗口类
class verifyMailDialog(QtWidgets.QDialog):
    verifyOKSignal = QtCore.pyqtSignal(bool)

    def __init__(self, mailAddr: str, veLastTime: int, parent: QtWidgets.QMainWindow):
        global veLastSendTime, stopVerifyCounterDownFlag
        super(verifyMailDialog, self).__init__()
        self.ui = Ui_ve.Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(522, 223)
        self.setWindowTitle("验证您的邮箱")

        self.mail = mailAddr
        self.lastTime = veLastTime
        veLastSendTime = veLastTime
        stopVerifyCounterDownFlag = False
        self.verifyOKSignal.connect(parent.verifiedMail)
        self.counterDown = timeCounterDown(self.ui.resendBtn)
        self.counterDown.start()

    def __del__(self):
        global stopVerifyCounterDownFlag
        logger.info("邮件验证窗口调用析构函数")
        stopVerifyCounterDownFlag = True

    def resend(self):
        global veLastSendTime
        if veLastSendTime + 60 - time.time() > 0:
            res = json.loads(requests.get(f"https://www.cinea.com.cn/api/sqp/check?mail={self.mail}",
                                          params={'code': 'ccczzz'}).text)
            veLastSendTime = res["lastSendTime"]

    def accept(self) -> None:
        resp = requests.post("https://www.cinea.com.cn/api/sqp/verify", params={"mail": self.mail,
                                                                                "code": self.ui.varifyCodeLE.text().encode(
                                                                                    "utf-8").decode("latin1")})
        if resp.status_code == 403:
            QtWidgets.QMessageBox.warning(self, "验证码错误", "您输入的验证码有误，请重新输入！")
            return
        elif resp.status_code == 200:
            self.verifyOKSignal.emit(True)
            return super(verifyMailDialog, self).accept()
        else:
            QtWidgets.QMessageBox.warning(self, "未知错误", "发生未知错误，请重试！")
            return

    def reject(self) -> None:
        return super(verifyMailDialog, self).reject()
