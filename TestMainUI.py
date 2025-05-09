# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestMainUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(958, 721)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setMinimumSize(QtCore.QSize(0, 80))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame.setStyleSheet("QFrame{\n"
"background-color: rgb(169, 152, 255);\n"
"}\n"
"QPushButton{\n"
"    border-radius:5px;\n"
"    background-color: rgb(211, 217, 255, 0);\n"
"    \n"
"    color: rgb(118, 118, 177);\n"
"    \n"
"    font: 14pt \"幼圆\";\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_7.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 20pt \"微软雅黑\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/Game_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_3.addWidget(self.pushButton_7)
        self.horizontalLayout_4.addWidget(self.frame_5)
        spacerItem = QtWidgets.QSpacerItem(336, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ico/8530586_window_minimize_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_4.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ico/normal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_5.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/ico/3671914_window_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_6.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/ico/1564505_close_delete_exit_remove_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.horizontalLayout_4.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setStyleSheet("background-color: rgb(207, 205, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(18)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("background-color: rgb(189, 223, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("")
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setStyleSheet("background-color: rgb(213, 225, 255);")
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_3.addWidget(self.listWidget)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_3.setStyleSheet("QFrame{\n"
"background-color: rgb(169, 152, 255);\n"
"}\n"
"QPushButton{\n"
"    border-radius:5px;\n"
"    background-color: rgb(211, 217, 255);\n"
"    \n"
"    color: rgb(118, 118, 177);\n"
"    \n"
"    font: 14pt \"幼圆\";\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(249, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem2 = QtWidgets.QSpacerItem(247, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setMinimumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_8.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout.addWidget(self.pushButton_8)
        spacerItem3 = QtWidgets.QSpacerItem(249, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.frame_3)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton_6.clicked.connect(Form.close) # type: ignore
        self.pushButton_5.clicked.connect(Form.showFullScreen) # type: ignore
        self.pushButton_4.clicked.connect(Form.showNormal) # type: ignore
        self.pushButton_3.clicked.connect(Form.showMinimized) # type: ignore
        self.pushButton.clicked.connect(Form.launch) # type: ignore
        self.pushButton_8.clicked.connect(Form.gameAdd) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_7.setText(_translate("Form", "GameLauncher"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "全部"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "分类1"))
        self.pushButton_2.setText(_translate("Form", "选项"))
        self.pushButton.setText(_translate("Form", "启动"))
        self.pushButton_8.setText(_translate("Form", "添加"))
import img_rc
import music_rc
