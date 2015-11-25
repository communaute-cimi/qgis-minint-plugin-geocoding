# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_GeoCoding.ui'
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

class Ui_GeoCoding(object):
    def setupUi(self, GeoCoding):
        GeoCoding.setObjectName(_fromUtf8("GeoCoding"))
        GeoCoding.resize(100, 30)
        self.gridLayout = QtGui.QGridLayout(GeoCoding)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.addressLabel = QtGui.QLabel(GeoCoding)
        self.addressLabel.setObjectName(_fromUtf8("addressLabel"))
        self.verticalLayout.addWidget(self.addressLabel)
        self.address = QtGui.QLineEdit(GeoCoding)
        self.address.setText(_fromUtf8(""))
        self.address.setObjectName(_fromUtf8("address"))
        self.verticalLayout.addWidget(self.address)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(GeoCoding)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(GeoCoding)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), GeoCoding.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), GeoCoding.reject)
        QtCore.QMetaObject.connectSlotsByName(GeoCoding)

    def retranslateUi(self, GeoCoding):
        GeoCoding.setWindowTitle(_translate("GeoCoding", "GeoCoding", None))
        self.addressLabel.setText(_translate("GeoCoding", "Address", None))

