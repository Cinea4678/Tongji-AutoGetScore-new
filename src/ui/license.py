"""

  条款窗口类

  Project Tongji-AutoGetScore
  Copyright (C) 2022 Cinea Zhan. All rights reserved.
  License: GNU General Public License v3.0

"""

import PyQt6.QtWidgets as QtWidgets
import PyQt6.QtCore as QtCore
import PyQt6.QtGui as QtGui

import src.ui.src.Ui_license as Ui_license


# 条款窗口类
class licenseDialog(QtWidgets.QDialog):
    def __init__(self):
        super(licenseDialog, self).__init__()
        self.ui = Ui_license.Ui_Dialog()
        self.ui.setupUi(self)
