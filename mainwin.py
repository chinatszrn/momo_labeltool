# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(1037, 784)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.canvas = Canvas(self.centralwidget)
        self.canvas.setInteractive(True)
        self.canvas.setObjectName("canvas")
        self.gridLayout_3.addWidget(self.canvas, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fixitem = QtWidgets.QCheckBox(self.widget)
        self.fixitem.setObjectName("fixitem")
        self.horizontalLayout.addWidget(self.fixitem)
        self.index = QtWidgets.QCheckBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.index.sizePolicy().hasHeightForWidth())
        self.index.setSizePolicy(sizePolicy)
        self.index.setObjectName("index")
        self.horizontalLayout.addWidget(self.index)
        self.control = QtWidgets.QCheckBox(self.widget)
        self.control.setChecked(True)
        self.control.setObjectName("control")
        self.horizontalLayout.addWidget(self.control)
        self.keypoint = QtWidgets.QCheckBox(self.widget)
        self.keypoint.setChecked(True)
        self.keypoint.setObjectName("keypoint")
        self.horizontalLayout.addWidget(self.keypoint)
        self.contour = QtWidgets.QCheckBox(self.widget)
        self.contour.setChecked(True)
        self.contour.setObjectName("contour")
        self.horizontalLayout.addWidget(self.contour)
        self.left_eyebrown = QtWidgets.QCheckBox(self.widget)
        self.left_eyebrown.setChecked(True)
        self.left_eyebrown.setObjectName("left_eyebrown")
        self.horizontalLayout.addWidget(self.left_eyebrown)
        self.right_eyebrown = QtWidgets.QCheckBox(self.widget)
        self.right_eyebrown.setChecked(True)
        self.right_eyebrown.setObjectName("right_eyebrown")
        self.horizontalLayout.addWidget(self.right_eyebrown)
        self.left_eye = QtWidgets.QCheckBox(self.widget)
        self.left_eye.setChecked(True)
        self.left_eye.setObjectName("left_eye")
        self.horizontalLayout.addWidget(self.left_eye)
        self.right_eye = QtWidgets.QCheckBox(self.widget)
        self.right_eye.setChecked(True)
        self.right_eye.setObjectName("right_eye")
        self.horizontalLayout.addWidget(self.right_eye)
        self.nose = QtWidgets.QCheckBox(self.widget)
        self.nose.setChecked(True)
        self.nose.setObjectName("nose")
        self.horizontalLayout.addWidget(self.nose)
        self.mouth_outter = QtWidgets.QCheckBox(self.widget)
        self.mouth_outter.setChecked(True)
        self.mouth_outter.setObjectName("mouth_outter")
        self.horizontalLayout.addWidget(self.mouth_outter)
        self.mouth_inner = QtWidgets.QCheckBox(self.widget)
        self.mouth_inner.setChecked(True)
        self.mouth_inner.setObjectName("mouth_inner")
        self.horizontalLayout.addWidget(self.mouth_inner)
        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1037, 18))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.dockWidget_2 = QtWidgets.QDockWidget(main_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_2.sizePolicy().hasHeightForWidth())
        self.dockWidget_2.setSizePolicy(sizePolicy)
        self.dockWidget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout.setObjectName("gridLayout")
        self.file_list = FileList(self.dockWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_list.sizePolicy().hasHeightForWidth())
        self.file_list.setSizePolicy(sizePolicy)
        self.file_list.setObjectName("file_list")
        self.gridLayout.addWidget(self.file_list, 0, 0, 1, 1)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        main_window.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_2)
        self.actionload = QtWidgets.QAction(main_window)
        self.actionload.setObjectName("actionload")
        self.actionConvert = QtWidgets.QAction(main_window)
        self.actionConvert.setObjectName("actionConvert")
        self.menu.addAction(self.actionload)
        self.menu_2.addAction(self.actionConvert)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "关键点标注"))
        self.fixitem.setText(_translate("main_window", "固定图片(F)"))
        self.fixitem.setShortcut(_translate("main_window", "F"))
        self.index.setText(_translate("main_window", "序号(S)"))
        self.index.setShortcut(_translate("main_window", "S"))
        self.control.setText(_translate("main_window", "控制点(Q)"))
        self.control.setShortcut(_translate("main_window", "Q"))
        self.keypoint.setText(_translate("main_window", "关键点(W)"))
        self.keypoint.setShortcut(_translate("main_window", "W"))
        self.contour.setText(_translate("main_window", "脸轮廓(E)"))
        self.contour.setShortcut(_translate("main_window", "E"))
        self.left_eyebrown.setText(_translate("main_window", "左眉毛(R)"))
        self.left_eyebrown.setShortcut(_translate("main_window", "R"))
        self.right_eyebrown.setText(_translate("main_window", "右眉毛(T)"))
        self.right_eyebrown.setShortcut(_translate("main_window", "T"))
        self.left_eye.setText(_translate("main_window", "左眼睛(Y)"))
        self.left_eye.setShortcut(_translate("main_window", "Y"))
        self.right_eye.setText(_translate("main_window", "右眼睛(U)"))
        self.right_eye.setShortcut(_translate("main_window", "U"))
        self.nose.setText(_translate("main_window", "鼻子(I)"))
        self.nose.setShortcut(_translate("main_window", "I"))
        self.mouth_outter.setText(_translate("main_window", "嘴外轮廓(O)"))
        self.mouth_outter.setShortcut(_translate("main_window", "O"))
        self.mouth_inner.setText(_translate("main_window", "嘴内轮廓(P)"))
        self.mouth_inner.setShortcut(_translate("main_window", "P"))
        self.menu.setTitle(_translate("main_window", "文件"))
        self.menu_2.setTitle(_translate("main_window", "数据处理"))
        self.actionload.setText(_translate("main_window", "载入文件夹"))
        self.actionConvert.setText(_translate("main_window", "生成137点标注结果"))

from canvas import Canvas
from filelist import FileList
