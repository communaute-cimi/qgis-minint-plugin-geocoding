# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_PlaceSelection.ui'
#
# Created: Thu Oct 22 15:50:26 2015
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

class Ui_PlaceSelectionDialog(object):
    def setupUi(self, PlaceSelectionDialog):
        PlaceSelectionDialog.setObjectName(_fromUtf8("PlaceSelectionDialog"))
        PlaceSelectionDialog.resize(512, 116)
        self.verticalLayout = QtGui.QVBoxLayout(PlaceSelectionDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(PlaceSelectionDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.placesComboBox = QtGui.QComboBox(PlaceSelectionDialog)
        self.placesComboBox.setObjectName(_fromUtf8("placesComboBox"))
        self.verticalLayout_2.addWidget(self.placesComboBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.buttonBox = QtGui.QDialogButtonBox(PlaceSelectionDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(PlaceSelectionDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), PlaceSelectionDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), PlaceSelectionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PlaceSelectionDialog)

    def retranslateUi(self, PlaceSelectionDialog):
        PlaceSelectionDialog.setWindowTitle(_translate("PlaceSelectionDialog", "Dialog", None))
        self.label.setText(_translate("PlaceSelectionDialog", "The server found more than one places, please choose one or all", None))

