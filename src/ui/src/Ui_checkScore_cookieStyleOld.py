# Form implementation generated from reading ui file 'checkScore_cookieStyleOld.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 628)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setSizeGripEnabled(False)
        self.InputBox = QtWidgets.QGroupBox(Dialog)
        self.InputBox.setGeometry(QtCore.QRect(10, 10, 671, 361))
        self.InputBox.setObjectName("InputBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.InputBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 651, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cookieLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.cookieLabel.setObjectName("cookieLabel")
        self.horizontalLayout.addWidget(self.cookieLabel)
        self.cookieLineEdt = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.cookieLineEdt.setObjectName("cookieLineEdt")
        self.horizontalLayout.addWidget(self.cookieLineEdt)
        self.cookieConfirmBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cookieConfirmBtn.setObjectName("cookieConfirmBtn")
        self.horizontalLayout.addWidget(self.cookieConfirmBtn)
        self.cookieHelpLebel = QtWidgets.QLabel(self.InputBox)
        self.cookieHelpLebel.setGeometry(QtCore.QRect(300, 100, 361, 31))
        self.cookieHelpLebel.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.cookieHelpLebel.setOpenExternalLinks(True)
        self.cookieHelpLebel.setObjectName("cookieHelpLebel")
        self.cookieHelpLebel_2 = QtWidgets.QLabel(self.InputBox)
        self.cookieHelpLebel_2.setGeometry(QtCore.QRect(90, 120, 571, 81))
        self.cookieHelpLebel_2.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.cookieHelpLebel_2.setScaledContents(False)
        self.cookieHelpLebel_2.setWordWrap(True)
        self.cookieHelpLebel_2.setObjectName("cookieHelpLebel_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.InputBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 190, 651, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.chooseTermLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.chooseTermLabel.setObjectName("chooseTermLabel")
        self.horizontalLayout_3.addWidget(self.chooseTermLabel)
        self.selectTermComboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectTermComboBox.sizePolicy().hasHeightForWidth())
        self.selectTermComboBox.setSizePolicy(sizePolicy)
        self.selectTermComboBox.setIconSize(QtCore.QSize(80, 20))
        self.selectTermComboBox.setPlaceholderText("")
        self.selectTermComboBox.setObjectName("selectTermComboBox")
        self.selectTermComboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.selectTermComboBox)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.InputBox)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 230, 651, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.mailLineEdt = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.mailLineEdt.setObjectName("mailLineEdt")
        self.horizontalLayout_4.addWidget(self.mailLineEdt)
        self.mailConfirmBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.mailConfirmBtn.setObjectName("mailConfirmBtn")
        self.horizontalLayout_4.addWidget(self.mailConfirmBtn)
        self.cookieHelpLebel_3 = QtWidgets.QLabel(self.InputBox)
        self.cookieHelpLebel_3.setGeometry(QtCore.QRect(90, 270, 571, 31))
        self.cookieHelpLebel_3.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.cookieHelpLebel_3.setScaledContents(False)
        self.cookieHelpLebel_3.setWordWrap(True)
        self.cookieHelpLebel_3.setIndent(-1)
        self.cookieHelpLebel_3.setObjectName("cookieHelpLebel_3")
        self.cookieHelpLebel_4 = QtWidgets.QLabel(self.InputBox)
        self.cookieHelpLebel_4.setGeometry(QtCore.QRect(90, 290, 571, 31))
        self.cookieHelpLebel_4.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.cookieHelpLebel_4.setScaledContents(False)
        self.cookieHelpLebel_4.setWordWrap(True)
        self.cookieHelpLebel_4.setIndent(-1)
        self.cookieHelpLebel_4.setObjectName("cookieHelpLebel_4")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.InputBox)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 310, 651, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.queryTimeEdit = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_4)
        self.queryTimeEdit.setMinimum(1.0)
        self.queryTimeEdit.setMaximum(10000.0)
        self.queryTimeEdit.setProperty("value", 30.0)
        self.queryTimeEdit.setObjectName("queryTimeEdit")
        self.horizontalLayout_5.addWidget(self.queryTimeEdit)
        self.delayTimeOK = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.delayTimeOK.setObjectName("delayTimeOK")
        self.horizontalLayout_5.addWidget(self.delayTimeOK)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_3.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.cookieHelpLebel_5 = QtWidgets.QLabel(self.InputBox)
        self.cookieHelpLebel_5.setGeometry(QtCore.QRect(10, 100, 131, 31))
        self.cookieHelpLebel_5.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.cookieHelpLebel_5.setOpenExternalLinks(True)
        self.cookieHelpLebel_5.setObjectName("cookieHelpLebel_5")
        self.setMailSuccessLabel = QtWidgets.QLabel(self.InputBox)
        self.setMailSuccessLabel.setEnabled(True)
        self.setMailSuccessLabel.setGeometry(QtCore.QRect(10, 270, 81, 31))
        self.setMailSuccessLabel.setObjectName("setMailSuccessLabel")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.InputBox)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 20, 651, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.studentNumberEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.studentNumberEdit.setObjectName("studentNumberEdit")
        self.horizontalLayout_2.addWidget(self.studentNumberEdit)
        self.sNumOKBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.sNumOKBtn.setObjectName("sNumOKBtn")
        self.horizontalLayout_2.addWidget(self.sNumOKBtn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.queryBox = QtWidgets.QGroupBox(Dialog)
        self.queryBox.setGeometry(QtCore.QRect(10, 380, 521, 231))
        self.queryBox.setObjectName("queryBox")
        self.progressBar = QtWidgets.QProgressBar(self.queryBox)
        self.progressBar.setGeometry(QtCore.QRect(10, 200, 501, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.progressBar.setObjectName("progressBar")
        self.outputWindow = QtWidgets.QTextEdit(self.queryBox)
        self.outputWindow.setGeometry(QtCore.QRect(10, 20, 501, 171))
        self.outputWindow.setUndoRedoEnabled(False)
        self.outputWindow.setReadOnly(True)
        self.outputWindow.setAcceptRichText(True)
        self.outputWindow.setObjectName("outputWindow")
        self.startButton = QtWidgets.QPushButton(Dialog)
        self.startButton.setGeometry(QtCore.QRect(540, 390, 141, 51))
        self.startButton.setObjectName("startButton")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(540, 450, 141, 161))
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        self.cookieConfirmBtn.clicked.connect(Dialog.accept) # type: ignore
        self.mailConfirmBtn.clicked.connect(Dialog.accept) # type: ignore
        self.selectTermComboBox.currentIndexChanged['int'].connect(Dialog.accept) # type: ignore
        self.delayTimeOK.clicked.connect(Dialog.accept) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.studentNumberEdit, self.sNumOKBtn)
        Dialog.setTabOrder(self.sNumOKBtn, self.cookieLineEdt)
        Dialog.setTabOrder(self.cookieLineEdt, self.cookieConfirmBtn)
        Dialog.setTabOrder(self.cookieConfirmBtn, self.selectTermComboBox)
        Dialog.setTabOrder(self.selectTermComboBox, self.mailLineEdt)
        Dialog.setTabOrder(self.mailLineEdt, self.mailConfirmBtn)
        Dialog.setTabOrder(self.mailConfirmBtn, self.queryTimeEdit)
        Dialog.setTabOrder(self.queryTimeEdit, self.delayTimeOK)
        Dialog.setTabOrder(self.delayTimeOK, self.startButton)
        Dialog.setTabOrder(self.startButton, self.outputWindow)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.InputBox.setTitle(_translate("Dialog", "????????????"))
        self.cookieLabel.setText(_translate("Dialog", "1??????cookie"))
        self.cookieConfirmBtn.setText(_translate("Dialog", "??????"))
        self.cookieHelpLebel.setText(_translate("Dialog", "<html><head/><body><p align=\"right\"><a href=\"https://www.cinea.com.cn\"><span style=\" text-decoration: underline; color:#0000ff;\">?????????????????????cookie????????????????????????????????????</span></a></p></body></html>"))
        self.cookieHelpLebel_2.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">?????????????????????cookie???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????</p></body></html>"))
        self.chooseTermLabel.setText(_translate("Dialog", "????????????"))
        self.selectTermComboBox.setCurrentText(_translate("Dialog", "????????????cookie"))
        self.selectTermComboBox.setItemText(0, _translate("Dialog", "????????????cookie"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><a href=\"https://www.cinea.com.cn\"><span style=\" text-decoration: underline; color:#0000ff;\">??????????????????????????????????????????????????????</span></a></p></body></html>"))
        self.label.setText(_translate("Dialog", "????????????????????????"))
        self.mailConfirmBtn.setText(_translate("Dialog", "??????"))
        self.cookieHelpLebel_3.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">???????????????????????????????????????????????????QQ?????????<span style=\" font-style:italic;\">??????QQ???</span>@qq.com???</p></body></html>"))
        self.cookieHelpLebel_4.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">????????????????????????????????????QQ???????????????????????????</p></body></html>"))
        self.label_2.setText(_translate("Dialog", "??????????????????"))
        self.queryTimeEdit.setSuffix(_translate("Dialog", "???"))
        self.delayTimeOK.setText(_translate("Dialog", "??????"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p>???????????????30??? <span style=\" font-weight:600; color:#ff0000;\">????????????????????????????????????</span></p></body></html>"))
        self.cookieHelpLebel_5.setText(_translate("Dialog", "<html><head/><body><p><a href=\"https://1.tongji.edu.cn\"><span style=\" text-decoration: underline; color:#0000ff;\">????????????1??????</span></a></p></body></html>"))
        self.setMailSuccessLabel.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">????????????</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "??????"))
        self.sNumOKBtn.setText(_translate("Dialog", "??????"))
        self.queryBox.setTitle(_translate("Dialog", "????????????"))
        self.progressBar.setToolTip(_translate("Dialog", "<html><head/><body><p>????????????????????????</p><p><span style=\" font-style:italic;\">???????????????????????????????????????????????????????????????</span></p></body></html>"))
        self.outputWindow.setToolTip(_translate("Dialog", "<html><head/><body><p>???????????????????????????</p></body></html>"))
        self.startButton.setText(_translate("Dialog", "????????????"))
        self.label_4.setToolTip(_translate("Dialog", "<html><head/><body><p>????????????????????????????????????????????????????????????</p><p>????????????????????????????????????</p><p>????????????</p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">??????: Cinea</p><p align=\"center\">???????????? 2021???</p><p align=\"center\">???????????????</p><p align=\"center\"><a href=\"https://www.cinea.com.cn\"><span style=\" text-decoration: underline; color:#0000ff;\">????????????</span></a></p><p align=\"center\"><a href=\"https://www.cinea.com.cn\"><span style=\" text-decoration: underline; color:#0000ff;\">??????BUG</span></a></p></body></html>"))
