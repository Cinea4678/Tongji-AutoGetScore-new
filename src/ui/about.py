"""

  关于窗口类

  Project Tongji-AutoGetScore
  Copyright (C) 2022 Cinea Zhan. All rights reserved.
  License: GNU General Public License v3.0

"""

import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui

import src.ui.src.Ui_about as Ui_about
import src.ui.license as Ui_license


# 关于窗口类
class aboutDialog(QtWidgets.QDialog):
    def __init__(self):
        super(aboutDialog, self).__init__()
        self.ui = Ui_about.Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(780, 480)
        self.ui.copyRightMsg.clicked.connect(self.showLicense)

    @staticmethod
    def showLicense():
        ldlg = Ui_license.licenseDialog()
        ldlg.exec()
