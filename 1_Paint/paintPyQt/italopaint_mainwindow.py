# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'italopaint_mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupTools = QtGui.QGroupBox(self.centralwidget)
        self.groupTools.setObjectName(_fromUtf8("groupTools"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupTools)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.btnPencil = QtGui.QPushButton(self.groupTools)
        self.btnPencil.setObjectName(_fromUtf8("btnPencil"))
        self.verticalLayout_5.addWidget(self.btnPencil)
        self.btnRectangle = QtGui.QPushButton(self.groupTools)
        self.btnRectangle.setObjectName(_fromUtf8("btnRectangle"))
        self.verticalLayout_5.addWidget(self.btnRectangle)
        self.btnCircle = QtGui.QPushButton(self.groupTools)
        self.btnCircle.setObjectName(_fromUtf8("btnCircle"))
        self.verticalLayout_5.addWidget(self.btnCircle)
        self.verticalLayout_3.addWidget(self.groupTools)
        self.groupOptions = QtGui.QGroupBox(self.centralwidget)
        self.groupOptions.setObjectName(_fromUtf8("groupOptions"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupOptions)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.btnClear = QtGui.QPushButton(self.groupOptions)
        self.btnClear.setObjectName(_fromUtf8("btnClear"))
        self.verticalLayout_4.addWidget(self.btnClear)
        self.labelTitleEspessura = QtGui.QLabel(self.groupOptions)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelTitleEspessura.setFont(font)
        self.labelTitleEspessura.setObjectName(_fromUtf8("labelTitleEspessura"))
        self.verticalLayout_4.addWidget(self.labelTitleEspessura)
        self.sliderEspessura = QtGui.QSlider(self.groupOptions)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sliderEspessura.sizePolicy().hasHeightForWidth())
        self.sliderEspessura.setSizePolicy(sizePolicy)
        self.sliderEspessura.setMinimumSize(QtCore.QSize(150, 0))
        self.sliderEspessura.setOrientation(QtCore.Qt.Horizontal)
        self.sliderEspessura.setObjectName(_fromUtf8("sliderEspessura"))
        self.verticalLayout_4.addWidget(self.sliderEspessura)
        self.labelTitleColor = QtGui.QLabel(self.groupOptions)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelTitleColor.setFont(font)
        self.labelTitleColor.setObjectName(_fromUtf8("labelTitleColor"))
        self.verticalLayout_4.addWidget(self.labelTitleColor)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.btnSelectColor = QtGui.QPushButton(self.groupOptions)
        self.btnSelectColor.setAutoFillBackground(False)
        self.btnSelectColor.setFlat(False)
        self.btnSelectColor.setObjectName(_fromUtf8("btnSelectColor"))
        self.gridLayout.addWidget(self.btnSelectColor, 0, 0, 1, 1)
        self.btnSelectBackColor = QtGui.QPushButton(self.groupOptions)
        self.btnSelectBackColor.setObjectName(_fromUtf8("btnSelectBackColor"))
        self.gridLayout.addWidget(self.btnSelectBackColor, 0, 1, 1, 1)
        self.graphicsViewBackColor = QtGui.QGraphicsView(self.groupOptions)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsViewBackColor.sizePolicy().hasHeightForWidth())
        self.graphicsViewBackColor.setSizePolicy(sizePolicy)
        self.graphicsViewBackColor.setMaximumSize(QtCore.QSize(85, 30))
        self.graphicsViewBackColor.setObjectName(_fromUtf8("graphicsViewBackColor"))
        self.gridLayout.addWidget(self.graphicsViewBackColor, 1, 1, 1, 1)
        self.graphicsViewMainColor = QtGui.QGraphicsView(self.groupOptions)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsViewMainColor.sizePolicy().hasHeightForWidth())
        self.graphicsViewMainColor.setSizePolicy(sizePolicy)
        self.graphicsViewMainColor.setMaximumSize(QtCore.QSize(85, 30))
        self.graphicsViewMainColor.setObjectName(_fromUtf8("graphicsViewMainColor"))
        self.gridLayout.addWidget(self.graphicsViewMainColor, 1, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout_3.addWidget(self.groupOptions)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.horizontalLayout.addWidget(self.graphicsView)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.labelStatusTitle = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelStatusTitle.sizePolicy().hasHeightForWidth())
        self.labelStatusTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelStatusTitle.setFont(font)
        self.labelStatusTitle.setObjectName(_fromUtf8("labelStatusTitle"))
        self.horizontalLayout_2.addWidget(self.labelStatusTitle)
        self.labelStatusMessage = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelStatusMessage.sizePolicy().hasHeightForWidth())
        self.labelStatusMessage.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setItalic(True)
        self.labelStatusMessage.setFont(font)
        self.labelStatusMessage.setObjectName(_fromUtf8("labelStatusMessage"))
        self.horizontalLayout_2.addWidget(self.labelStatusMessage)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Paint do Italo", None))
        self.groupTools.setTitle(_translate("MainWindow", "Ferramentas:", None))
        self.btnPencil.setText(_translate("MainWindow", "Lapís", None))
        self.btnRectangle.setText(_translate("MainWindow", "Retângulo", None))
        self.btnCircle.setText(_translate("MainWindow", "Círculo", None))
        self.groupOptions.setTitle(_translate("MainWindow", "Opções:", None))
        self.btnClear.setText(_translate("MainWindow", "Limpar", None))
        self.labelTitleEspessura.setText(_translate("MainWindow", "Espessura:", None))
        self.labelTitleColor.setText(_translate("MainWindow", "Cor:", None))
        self.btnSelectColor.setText(_translate("MainWindow", "Main", None))
        self.btnSelectBackColor.setText(_translate("MainWindow", "Back", None))
        self.labelStatusTitle.setText(_translate("MainWindow", "Status:", None))
        self.labelStatusMessage.setText(_translate("MainWindow", "Aguardando Comando...", None))

