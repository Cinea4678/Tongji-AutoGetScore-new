# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1043, 702)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.configGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.configGroupBox.setGeometry(QtCore.QRect(10, 10, 1021, 171))
        self.configGroupBox.setObjectName("configGroupBox")
        self.label = QtWidgets.QLabel(self.configGroupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 83, 29))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.configGroupBox)
        self.label_2.setGeometry(QtCore.QRect(120, 20, 45, 29))
        self.label_2.setObjectName("label_2")
        self.nameLabel = QtWidgets.QLabel(self.configGroupBox)
        self.nameLabel.setGeometry(QtCore.QRect(170, 20, 64, 29))
        self.nameLabel.setObjectName("nameLabel")
        self.label_4 = QtWidgets.QLabel(self.configGroupBox)
        self.label_4.setGeometry(QtCore.QRect(260, 20, 51, 29))
        self.label_4.setObjectName("label_4")
        self.fLabel = QtWidgets.QLabel(self.configGroupBox)
        self.fLabel.setGeometry(QtCore.QRect(310, 20, 211, 29))
        self.fLabel.setObjectName("fLabel")
        self.label_6 = QtWidgets.QLabel(self.configGroupBox)
        self.label_6.setGeometry(QtCore.QRect(530, 20, 51, 29))
        self.label_6.setObjectName("label_6")
        self.gradeLabel = QtWidgets.QLabel(self.configGroupBox)
        self.gradeLabel.setGeometry(QtCore.QRect(580, 20, 81, 29))
        self.gradeLabel.setObjectName("gradeLabel")
        self.chooseTermLabel = QtWidgets.QLabel(self.configGroupBox)
        self.chooseTermLabel.setGeometry(QtCore.QRect(10, 60, 71, 31))
        self.chooseTermLabel.setObjectName("chooseTermLabel")
        self.selectTermComboBox_2 = QtWidgets.QComboBox(self.configGroupBox)
        self.selectTermComboBox_2.setGeometry(QtCore.QRect(80, 60, 250, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectTermComboBox_2.sizePolicy().hasHeightForWidth())
        self.selectTermComboBox_2.setSizePolicy(sizePolicy)
        self.selectTermComboBox_2.setMinimumSize(QtCore.QSize(250, 0))
        self.selectTermComboBox_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.selectTermComboBox_2.setBaseSize(QtCore.QSize(0, 0))
        self.selectTermComboBox_2.setIconSize(QtCore.QSize(60, 20))
        self.selectTermComboBox_2.setPlaceholderText("")
        self.selectTermComboBox_2.setObjectName("selectTermComboBox_2")
        self.selectTermComboBox_2.addItem("")
        self.label_8 = QtWidgets.QLabel(self.configGroupBox)
        self.label_8.setGeometry(QtCore.QRect(340, 60, 281, 31))
        self.label_8.setOpenExternalLinks(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.configGroupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 98, 120, 31))
        self.label_9.setObjectName("label_9")
        self.mailLineEdt = QtWidgets.QLineEdit(self.configGroupBox)
        self.mailLineEdt.setGeometry(QtCore.QRect(140, 100, 301, 26))
        self.mailLineEdt.setObjectName("mailLineEdt")
        self.cookieHelpLebel_3 = QtWidgets.QLabel(self.configGroupBox)
        self.cookieHelpLebel_3.setGeometry(QtCore.QRect(530, 90, 491, 31))
        self.cookieHelpLebel_3.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.cookieHelpLebel_3.setScaledContents(False)
        self.cookieHelpLebel_3.setWordWrap(True)
        self.cookieHelpLebel_3.setIndent(-1)
        self.cookieHelpLebel_3.setObjectName("cookieHelpLebel_3")
        self.cookieHelpLebel_4 = QtWidgets.QLabel(self.configGroupBox)
        self.cookieHelpLebel_4.setGeometry(QtCore.QRect(630, 110, 381, 31))
        self.cookieHelpLebel_4.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.cookieHelpLebel_4.setScaledContents(False)
        self.cookieHelpLebel_4.setWordWrap(True)
        self.cookieHelpLebel_4.setIndent(-1)
        self.cookieHelpLebel_4.setObjectName("cookieHelpLebel_4")
        self.label_10 = QtWidgets.QLabel(self.configGroupBox)
        self.label_10.setGeometry(QtCore.QRect(10, 130, 90, 41))
        self.label_10.setObjectName("label_10")
        self.queryTimeEdit = QtWidgets.QDoubleSpinBox(self.configGroupBox)
        self.queryTimeEdit.setGeometry(QtCore.QRect(110, 135, 100, 26))
        self.queryTimeEdit.setMinimum(1.0)
        self.queryTimeEdit.setMaximum(10000.0)
        self.queryTimeEdit.setProperty("value", 30.0)
        self.queryTimeEdit.setObjectName("queryTimeEdit")
        self.label_11 = QtWidgets.QLabel(self.configGroupBox)
        self.label_11.setGeometry(QtCore.QRect(320, 130, 290, 41))
        self.label_11.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.label_11.setObjectName("label_11")
        self.startButton = QtWidgets.QPushButton(self.configGroupBox)
        self.startButton.setGeometry(QtCore.QRect(700, 20, 141, 51))
        self.startButton.setObjectName("startButton")
        self.aboutBtn = QtWidgets.QPushButton(self.configGroupBox)
        self.aboutBtn.setGeometry(QtCore.QRect(860, 20, 141, 51))
        self.aboutBtn.setObjectName("aboutBtn")
        self.mailConfirmBtn_2 = QtWidgets.QPushButton(self.configGroupBox)
        self.mailConfirmBtn_2.setGeometry(QtCore.QRect(450, 100, 100, 32))
        self.mailConfirmBtn_2.setObjectName("mailConfirmBtn_2")
        self.delayTimeOK = QtWidgets.QPushButton(self.configGroupBox)
        self.delayTimeOK.setGeometry(QtCore.QRect(219, 133, 91, 32))
        self.delayTimeOK.setObjectName("delayTimeOK")
        self.queryBox = QtWidgets.QGroupBox(self.centralwidget)
        self.queryBox.setGeometry(QtCore.QRect(10, 430, 1021, 231))
        self.queryBox.setObjectName("queryBox")
        self.progressBar = QtWidgets.QProgressBar(self.queryBox)
        self.progressBar.setGeometry(QtCore.QRect(10, 200, 1001, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.progressBar.setObjectName("progressBar")
        self.outputWindow = QtWidgets.QTextEdit(self.queryBox)
        self.outputWindow.setGeometry(QtCore.QRect(10, 20, 1001, 171))
        self.outputWindow.setUndoRedoEnabled(False)
        self.outputWindow.setReadOnly(True)
        self.outputWindow.setAcceptRichText(True)
        self.outputWindow.setObjectName("outputWindow")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 190, 1021, 231))
        self.groupBox.setObjectName("groupBox")
        self.scoreTable = QtWidgets.QTableWidget(self.groupBox)
        self.scoreTable.setGeometry(QtCore.QRect(10, 20, 1001, 201))
        self.scoreTable.setObjectName("scoreTable")
        self.scoreTable.setColumnCount(0)
        self.scoreTable.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "??????????????????"))
        self.configGroupBox.setTitle(_translate("MainWindow", "????????????"))
        self.label.setText(_translate("MainWindow", "1???????????????"))
        self.label_2.setText(_translate("MainWindow", "?????????"))
        self.nameLabel.setText(_translate("MainWindow", "?????????"))
        self.label_4.setText(_translate("MainWindow", "?????????"))
        self.fLabel.setText(_translate("MainWindow", "?????????"))
        self.label_6.setText(_translate("MainWindow", "?????????"))
        self.gradeLabel.setText(_translate("MainWindow", "?????????"))
        self.chooseTermLabel.setText(_translate("MainWindow", "????????????"))
        self.selectTermComboBox_2.setCurrentText(_translate("MainWindow", "????????????1??????"))
        self.selectTermComboBox_2.setItemText(0, _translate("MainWindow", "????????????1??????"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://blog.cinea.com.cn/TJAGS/NoWantedTerm.html\"><span style=\" text-decoration: underline; color:#0000ff;\">??????????????????????????????????????????????????????</span></a></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "????????????????????????"))
        self.cookieHelpLebel_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">???????????????????????????????????????????????????QQ?????????<span style=\" font-style:italic;\">??????QQ???</span>@qq.com???</p></body></html>"))
        self.cookieHelpLebel_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">????????????????????????????????????QQ???????????????????????????</p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "??????????????????"))
        self.queryTimeEdit.setSuffix(_translate("MainWindow", "???"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p>???????????????30??? <span style=\" font-weight:600; color:#ff0000;\">????????????????????????????????????</span></p></body></html>"))
        self.startButton.setText(_translate("MainWindow", "????????????"))
        self.aboutBtn.setText(_translate("MainWindow", "??????"))
        self.mailConfirmBtn_2.setText(_translate("MainWindow", "??????"))
        self.delayTimeOK.setText(_translate("MainWindow", "??????"))
        self.queryBox.setTitle(_translate("MainWindow", "????????????"))
        self.progressBar.setToolTip(_translate("MainWindow", "<html><head/><body><p>????????????????????????</p><p><span style=\" font-style:italic;\">???????????????????????????????????????????????????????????????</span></p></body></html>"))
        self.outputWindow.setToolTip(_translate("MainWindow", "<html><head/><body><p>???????????????????????????</p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "????????????"))
