# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\算法实验室\17pyqt查成绩\Tongji-AutoGetScore\ui\about.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(780, 480)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        Dialog.setFont(font)
        self.img = QtWidgets.QLabel(Dialog)
        self.img.setGeometry(QtCore.QRect(160, 30, 471, 91))
        self.img.setStyleSheet("")
        self.img.setText("")
        self.img.setObjectName("img")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(240, 130, 321, 61))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(240, 170, 321, 61))
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(240, 230, 321, 21))
        self.label_4.setStyleSheet("line-height:5px")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(240, 250, 321, 21))
        self.label_5.setStyleSheet("line-height:5px")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 290, 361, 61))
        self.label_6.setStyleSheet("")
        self.label_6.setOpenExternalLinks(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(390, 290, 361, 61))
        self.label_7.setStyleSheet("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(170, 350, 451, 41))
        self.label_8.setStyleSheet("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(130, 380, 531, 41))
        self.label_9.setStyleSheet("")
        self.label_9.setObjectName("label_9")
        self.copyRightMsg = QtWidgets.QPushButton(Dialog)
        self.copyRightMsg.setGeometry(QtCore.QRect(340, 430, 131, 28))
        self.copyRightMsg.setObjectName("copyRightMsg")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "关于作者"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">自由摄影师</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">非专业Python爱好者</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">长期有偿/无偿承接各种爬虫业务</p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">（注：无偿单需要有公益属性且必须开源）</p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">个人网站：</span><a href=\"https://www.cinea.com.cn\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">www.cinea.com.cn</span></a></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"> 邮箱：cinea@cinea.com.cn</span></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">提交BUG请到Github Issue区或向我发送邮件</span></p></body></html>"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">严重/紧急的BUG也可以添加我的QQ：1650121748（注明来意）</span></p></body></html>"))
        self.copyRightMsg.setText(_translate("Dialog", "版权信息"))
