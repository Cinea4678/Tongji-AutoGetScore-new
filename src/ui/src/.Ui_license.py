# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'license.ui'
#
# Created by: PyQt6 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(806, 374)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        Dialog.setFont(font)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(440, 320, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 761, 271))
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "版权信息"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'SimSun\'; font-size:9pt;\">本软件使用</span><span style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:600;\">GPL</span><span style=\" font-family:\'SimSun\'; font-size:9pt;\">协议开源，你可以自由地使用除</span><span style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:600;\">邮箱账号</span><span style=\" font-family:\'SimSun\'; font-size:9pt;\">以外的所有源代码。</span><a href=\"https://github.com/Cinea4678/Tongji-AutoGetScore\"><span style=\" font-family:\'SimSun\'; font-size:9pt; text-decoration: underline; color:#0000ff;\">开源地址</span></a></p><p><span style=\" font-family:\'SimSun\'; font-size:9pt;\">本软件macOS版本的分发的图标来自</span><a href=\"https://www.flaticon.com/free-icons/paper\"><span style=\" font-family:\'SimSun\'; font-size:9pt; text-decoration: underline; color:#0000ff;\">Paper icons created by Freepik - Flaticon</span></a><span style=\" font-family:\'SimSun\'; font-size:9pt;\">，按照使用协议使用。</span></p><p><span style=\" font-family:\'SimSun\'; font-size:9pt;\">本软件内核使用了本人开发的同济大学API系统，由于信息办封号尚未完整开发，欢迎持续关注：</span><a href=\"https://github.com/Cinea4678/Tongji-EasyAPI\"><span style=\" font-size:9pt; text-decoration: underline; color:#094fd1;\">开源地址</span></a></p><p><span style=\" font-family:\'SimSun\'; font-size:9pt;\">本软件在开发过程中使用了如下的开源项目，感谢这些项目开发者的付出。限于作者水平，可能罗列不完全：</span></p><p><span style=\" font-family:\'Source Sans Pro\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:11pt; font-weight:600; color:#000000;\">GPL兼容 </span><span style=\" font-family:\'Source Sans Pro\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:9pt; font-weight:600; color:#000000;\">Python3</span></p><p><span style=\" font-family:\'Source Sans Pro\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:11pt; font-weight:600; color:#000000;\">Apache Software License  </span><span style=\" font-family:\'Source Sans Pro\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:9pt; font-weight:600; color:#000000;\">requests </span></p><p><span style=\" font-family:\'Source Sans Pro\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:11pt; font-weight:600; color:#000000;\">MIT License  </span><span style=\" font-family:\'Source Sans Pro\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:9pt; font-weight:600; color:#000000;\">loguru </span></p><p><span style=\" font-family:\'Source Sans Pro\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:11pt; font-weight:600; color:#000000;\">GPL v3  </span><span style=\" font-family:\'Source Sans Pro\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:9pt; font-weight:600; color:#000000;\">PyQt6 PyQtWebEngine</span></p><p><span style=\" font-family:\'Source Sans Pro\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:11pt; font-weight:600; color:#000000;\">GPL v2  </span><span style=\" font-family:\'Source Sans Pro\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:9pt; font-weight:600; color:#000000;\">git</span></p></body></html>"))
