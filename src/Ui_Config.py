# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Config.ui'
#
# Created: Thu Oct 22 15:50:25 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_Config(object):
    def setupUi(self, Config):
        Config.setObjectName(_fromUtf8("Config"))
        Config.setEnabled(True)
        Config.resize(479, 252)
        self.verticalLayoutWidget = QtGui.QWidget(Config)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 451, 221))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.geocoderComboBox = QtGui.QComboBox(self.verticalLayoutWidget)
        self.geocoderComboBox.setObjectName(_fromUtf8("geocoderComboBox"))
        self.verticalLayout.addWidget(self.geocoderComboBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.ZoomScale = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.ZoomScale.setMaximum(500000)
        self.ZoomScale.setSingleStep(100)
        self.ZoomScale.setObjectName(_fromUtf8("ZoomScale"))
        self.horizontalLayout_2.addWidget(self.ZoomScale)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtGui.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Config)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Config.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Config.reject)
        QtCore.QMetaObject.connectSlotsByName(Config)

    def retranslateUi(self, Config):
        Config.setWindowTitle(_translate("Config", "Settings", None))
        self.label_5.setText(_translate("Config", "Geocoder", None))
        self.label_3.setText(_translate("Config", "Zoom to scale when geocoding (0 = keep current)", None))
        self.label_4.setText(_translate("Config", "1:", None))

