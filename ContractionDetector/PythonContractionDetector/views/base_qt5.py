# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'base.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(735, 538)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(597, 538))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayoutOptions = QtWidgets.QVBoxLayout()
        self.verticalLayoutOptions.setObjectName("verticalLayoutOptions")
        self.lbl_options = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_options.sizePolicy().hasHeightForWidth())
        self.lbl_options.setSizePolicy(sizePolicy)
        self.lbl_options.setMaximumSize(QtCore.QSize(16777215, 50))
        self.lbl_options.setObjectName("lbl_options")
        self.verticalLayoutOptions.addWidget(self.lbl_options)
        self.horizontalLayoutBtns = QtWidgets.QHBoxLayout()
        self.horizontalLayoutBtns.setObjectName("horizontalLayoutBtns")
        spacerItem = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutBtns.addItem(spacerItem)
        self.verticalLayoutBtns = QtWidgets.QVBoxLayout()
        self.verticalLayoutBtns.setObjectName("verticalLayoutBtns")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy)
        self.btn_start.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btn_start.setObjectName("btn_start")
        self.verticalLayoutBtns.addWidget(self.btn_start)
        self.btn_calib = QtWidgets.QPushButton(self.centralwidget)
        self.btn_calib.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btn_calib.setObjectName("btn_calib")
        self.verticalLayoutBtns.addWidget(self.btn_calib)
        self.horizontalLayoutBtns.addLayout(self.verticalLayoutBtns)
        spacerItem1 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutBtns.addItem(spacerItem1)
        self.verticalLayoutOptions.addLayout(self.horizontalLayoutBtns)
        self.verticalLayoutThreshould = QtWidgets.QVBoxLayout()
        self.verticalLayoutThreshould.setObjectName("verticalLayoutThreshould")
        self.lbl_threshould = QtWidgets.QLabel(self.centralwidget)
        self.lbl_threshould.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_threshould.setObjectName("lbl_threshould")
        self.verticalLayoutThreshould.addWidget(self.lbl_threshould)
        self.horizontalLayoutThreshould = QtWidgets.QHBoxLayout()
        self.horizontalLayoutThreshould.setObjectName("horizontalLayoutThreshould")
        spacerItem2 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutThreshould.addItem(spacerItem2)
        self.sl_threshould = QtWidgets.QSlider(self.centralwidget)
        self.sl_threshould.setOrientation(QtCore.Qt.Vertical)
        self.sl_threshould.setObjectName("sl_threshould")
        self.horizontalLayoutThreshould.addWidget(self.sl_threshould)
        spacerItem3 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutThreshould.addItem(spacerItem3)
        self.verticalLayoutThreshould.addLayout(self.horizontalLayoutThreshould)
        self.verticalLayoutCheckBoxes = QtWidgets.QVBoxLayout()
        self.verticalLayoutCheckBoxes.setObjectName("verticalLayoutCheckBoxes")
        self.cb_emg = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_emg.setObjectName("cb_emg")
        self.verticalLayoutCheckBoxes.addWidget(self.cb_emg)
        self.cb_hbt = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_hbt.setObjectName("cb_hbt")
        self.verticalLayoutCheckBoxes.addWidget(self.cb_hbt)
        self.cb_ret = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_ret.setObjectName("cb_ret")
        self.verticalLayoutCheckBoxes.addWidget(self.cb_ret)
        self.cb_env = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_env.setObjectName("cb_env")
        self.verticalLayoutCheckBoxes.addWidget(self.cb_env)
        self.cb_lim = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_lim.setObjectName("cb_lim")
        self.verticalLayoutCheckBoxes.addWidget(self.cb_lim)
        self.cb_det = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_det.setObjectName("cb_det")
        self.verticalLayoutCheckBoxes.addWidget(self.cb_det)
        self.verticalLayoutThreshould.addLayout(self.verticalLayoutCheckBoxes)
        self.verticalLayoutOptions.addLayout(self.verticalLayoutThreshould)
        self.horizontalLayout.addLayout(self.verticalLayoutOptions)
        self.verticalLayoutGraphStatus = QtWidgets.QVBoxLayout()
        self.verticalLayoutGraphStatus.setObjectName("verticalLayoutGraphStatus")
        self.verticalLayoutGraph = QtWidgets.QVBoxLayout()
        self.verticalLayoutGraph.setObjectName("verticalLayoutGraph")
        self.label_replace = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_replace.sizePolicy().hasHeightForWidth())
        self.label_replace.setSizePolicy(sizePolicy)
        self.label_replace.setObjectName("label_replace")
        self.verticalLayoutGraph.addWidget(self.label_replace)
        self.verticalLayoutGraphStatus.addLayout(self.verticalLayoutGraph)
        self.lbl_status = QtWidgets.QLabel(self.centralwidget)
        self.lbl_status.setObjectName("lbl_status")
        self.verticalLayoutGraphStatus.addWidget(self.lbl_status)
        self.horizontalLayout.addLayout(self.verticalLayoutGraphStatus)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 735, 28))
        self.menubar.setObjectName("menubar")
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setObjectName("menuArquivo")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Contraction Detector"))
        self.lbl_options.setText(_translate("MainWindow", "Opções:"))
        self.btn_start.setToolTip(_translate("MainWindow", "Start"))
        self.btn_start.setText(_translate("MainWindow", "S"))
        self.btn_calib.setToolTip(_translate("MainWindow", "Calibrar"))
        self.btn_calib.setText(_translate("MainWindow", "C"))
        self.lbl_threshould.setText(_translate("MainWindow", "Limiar:"))
        self.cb_emg.setText(_translate("MainWindow", "EMG"))
        self.cb_hbt.setText(_translate("MainWindow", "HBT"))
        self.cb_ret.setText(_translate("MainWindow", "RET"))
        self.cb_env.setText(_translate("MainWindow", "ENV"))
        self.cb_lim.setText(_translate("MainWindow", "LIM"))
        self.cb_det.setText(_translate("MainWindow", "DET"))
        self.label_replace.setText(_translate("MainWindow", "Here will be the chart"))
        self.lbl_status.setText(_translate("MainWindow", "Status:"))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))

