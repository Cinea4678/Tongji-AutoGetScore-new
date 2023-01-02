"""

  关于窗口类

  Project Tongji-AutoGetScore
  Copyright (C) 2022 Cinea Zhan. All rights reserved.
  License: GNU General Public License v3.0

"""
import json

import PyQt6.QtWidgets as QtWidgets
import PyQt6.QtCore as QtCore
import PyQt6.QtGui as QtGui

import src.ui.src.Ui_about as Ui_about
import src.ui.license as Ui_license


# 关于窗口类
class aboutDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super(aboutDialog, self).__init__()
        self.ui = Ui_about.Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(780, 480)
        self.parentDlg = parent
        self.ui.copyRightMsg.clicked.connect(self.showLicense)
        self.ui.debugTools.clicked.connect(self.dbgTools)

    @staticmethod
    def showLicense():
        ldlg = Ui_license.licenseDialog()
        ldlg.exec()

    def _getOriginExamDataBtn(self):
        data = json.dumps(self.parentDlg.session.getScore().data, ensure_ascii=False, indent=4)
        newDlg = QtWidgets.QDialog(self)
        layout=QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.Direction.TopToBottom, newDlg)
        edit = QtWidgets.QTextEdit(newDlg)
        edit.setText(data)
        edit.setReadOnly(True)
        layout.addWidget(edit)
        newDlg.setLayout(layout)
        newDlg.exec()

    def dbgTools(self):
        newDlg = QtWidgets.QDialog(self)
        newDlg.setWindowTitle("开发者工具")
        layout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.Direction.TopToBottom, newDlg)
        label1 = QtWidgets.QLabel("请在开发者指导下使用")
        layout.addWidget(label1)
        # 获取原始成绩数据
        getOriginExamDataBtn = QtWidgets.QPushButton("查看原始成绩数据", newDlg)
        getOriginExamDataBtn.clicked.connect(self._getOriginExamDataBtn)
        layout.addWidget(getOriginExamDataBtn)
        newDlg.setLayout(layout)
        newDlg.exec()
