# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\yuanc\Desktop\aiui\schedule_face_manager\gui\res\msg_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_msg_window(object):
    def setupUi(self, msg_window):
        msg_window.setObjectName("msg_window")
        msg_window.resize(1280, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(msg_window.sizePolicy().hasHeightForWidth())
        msg_window.setSizePolicy(sizePolicy)
        msg_window.setMinimumSize(QtCore.QSize(1280, 800))
        msg_window.setMaximumSize(QtCore.QSize(1280, 800))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        msg_window.setFont(font)
        self.centralwidget = QtWidgets.QWidget(msg_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label_background = QtWidgets.QLabel(self.centralwidget)
        self.label_background.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_background.sizePolicy().hasHeightForWidth())
        self.label_background.setSizePolicy(sizePolicy)
        self.label_background.setMinimumSize(QtCore.QSize(1280, 800))
        self.label_background.setMaximumSize(QtCore.QSize(1280, 800))
        self.label_background.setText("")
        self.label_background.setPixmap(QtGui.QPixmap(":/background/background.png"))
        self.label_background.setScaledContents(True)
        self.label_background.setAlignment(QtCore.Qt.AlignCenter)
        self.label_background.setObjectName("label_background")
        self.msg_box = QtWidgets.QFrame(self.centralwidget)
        self.msg_box.setGeometry(QtCore.QRect(340, 100, 600, 500))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msg_box.sizePolicy().hasHeightForWidth())
        self.msg_box.setSizePolicy(sizePolicy)
        self.msg_box.setMinimumSize(QtCore.QSize(600, 500))
        self.msg_box.setMaximumSize(QtCore.QSize(600, 500))
        self.msg_box.setObjectName("msg_box")
        self.background_of_box = QtWidgets.QLabel(self.msg_box)
        self.background_of_box.setGeometry(QtCore.QRect(0, 0, 600, 500))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.background_of_box.sizePolicy().hasHeightForWidth())
        self.background_of_box.setSizePolicy(sizePolicy)
        self.background_of_box.setMinimumSize(QtCore.QSize(600, 500))
        self.background_of_box.setMaximumSize(QtCore.QSize(600, 500))
        self.background_of_box.setText("")
        self.background_of_box.setPixmap(QtGui.QPixmap(":/background/box_3.png"))
        self.background_of_box.setScaledContents(True)
        self.background_of_box.setAlignment(QtCore.Qt.AlignCenter)
        self.background_of_box.setObjectName("background_of_box")
        self.gridLayoutWidget = QtWidgets.QWidget(self.msg_box)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(80, 90, 441, 341))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.grid_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.grid_layout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.grid_layout.setObjectName("grid_layout")
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.grid_layout.addWidget(self.label_10, 1, 0, 1, 1)
        self.label_00 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_00.setObjectName("label_00")
        self.grid_layout.addWidget(self.label_00, 0, 0, 1, 1)
        self.label_01 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_01.setText("")
        self.label_01.setObjectName("label_01")
        self.grid_layout.addWidget(self.label_01, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.grid_layout.addWidget(self.label_11, 1, 1, 1, 1)
        self.who_schedule = QtWidgets.QLabel(self.msg_box)
        self.who_schedule.setGeometry(QtCore.QRect(90, 50, 91, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.who_schedule.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.who_schedule.setFont(font)
        self.who_schedule.setText("")
        self.who_schedule.setScaledContents(False)
        self.who_schedule.setAlignment(QtCore.Qt.AlignCenter)
        self.who_schedule.setWordWrap(True)
        self.who_schedule.setObjectName("who_schedule")
        self.time_display = QtWidgets.QLabel(self.centralwidget)
        self.time_display.setGeometry(QtCore.QRect(100, 50, 200, 90))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_display.sizePolicy().hasHeightForWidth())
        self.time_display.setSizePolicy(sizePolicy)
        self.time_display.setMinimumSize(QtCore.QSize(200, 90))
        self.time_display.setMaximumSize(QtCore.QSize(200, 90))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.time_display.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Monospac821 BT")
        font.setPointSize(50)
        self.time_display.setFont(font)
        self.time_display.setScaledContents(True)
        self.time_display.setAlignment(QtCore.Qt.AlignCenter)
        self.time_display.setObjectName("time_display")
        self.btn_know = QtWidgets.QPushButton(self.centralwidget)
        self.btn_know.setGeometry(QtCore.QRect(540, 610, 200, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_know.sizePolicy().hasHeightForWidth())
        self.btn_know.setSizePolicy(sizePolicy)
        self.btn_know.setMinimumSize(QtCore.QSize(200, 50))
        self.btn_know.setMaximumSize(QtCore.QSize(200, 50))
        self.btn_know.setDefault(False)
        self.btn_know.setFlat(False)
        self.btn_know.setObjectName("btn_know")
        msg_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(msg_window)
        self.btn_know.clicked.connect(msg_window.close)
        QtCore.QMetaObject.connectSlotsByName(msg_window)

    def retranslateUi(self, msg_window):
        _translate = QtCore.QCoreApplication.translate
        msg_window.setWindowTitle(_translate("msg_window", "msg_window"))
        self.label_10.setText(_translate("msg_window", "事情"))
        self.label_00.setText(_translate("msg_window", "时间"))
        self.time_display.setText(_translate("msg_window", "00:00"))
        self.btn_know.setText(_translate("msg_window", "知道了"))

import source_rc
