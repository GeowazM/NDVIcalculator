# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NDVI_calculator_dialog_base.ui'
#
# Created: Thu Jun 30 21:42:45 2016
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

class Ui_NDVIcalculatorDialogBase(object):
    def setupUi(self, NDVIcalculatorDialogBase):
        NDVIcalculatorDialogBase.setObjectName(_fromUtf8("NDVIcalculatorDialogBase"))
        NDVIcalculatorDialogBase.resize(400, 259)
        self.verticalLayout = QtGui.QVBoxLayout(NDVIcalculatorDialogBase)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_5 = QtGui.QGroupBox(NDVIcalculatorDialogBase)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.lineEdit_input = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_input.setText(_fromUtf8(""))
        self.lineEdit_input.setObjectName(_fromUtf8("lineEdit_input"))
        self.horizontalLayout_7.addWidget(self.lineEdit_input)
        self.button_input = QtGui.QPushButton(self.groupBox_5)
        self.button_input.setObjectName(_fromUtf8("button_input"))
        self.horizontalLayout_7.addWidget(self.button_input)
        self.verticalLayout.addWidget(self.groupBox_5)
        self.groupBox_4 = QtGui.QGroupBox(NDVIcalculatorDialogBase)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.spinBox_nir = QtGui.QSpinBox(self.groupBox_3)
        self.spinBox_nir.setSpecialValueText(_fromUtf8(""))
        self.spinBox_nir.setMinimum(1)
        self.spinBox_nir.setProperty("value", 4)
        self.spinBox_nir.setObjectName(_fromUtf8("spinBox_nir"))
        self.horizontalLayout.addWidget(self.spinBox_nir)
        self.label_nir = QtGui.QLabel(self.groupBox_3)
        self.label_nir.setObjectName(_fromUtf8("label_nir"))
        self.horizontalLayout.addWidget(self.label_nir)
        self.spinBox_red = QtGui.QSpinBox(self.groupBox_3)
        self.spinBox_red.setSpecialValueText(_fromUtf8(""))
        self.spinBox_red.setMinimum(1)
        self.spinBox_red.setProperty("value", 3)
        self.spinBox_red.setObjectName(_fromUtf8("spinBox_red"))
        self.horizontalLayout.addWidget(self.spinBox_red)
        self.label_red = QtGui.QLabel(self.groupBox_3)
        self.label_red.setObjectName(_fromUtf8("label_red"))
        self.horizontalLayout.addWidget(self.label_red)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_6 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.spinBox_x = QtGui.QSpinBox(self.groupBox_6)
        self.spinBox_x.setSpecialValueText(_fromUtf8(""))
        self.spinBox_x.setMinimum(1)
        self.spinBox_x.setProperty("value", 5)
        self.spinBox_x.setObjectName(_fromUtf8("spinBox_x"))
        self.horizontalLayout_5.addWidget(self.spinBox_x)
        self.label_x = QtGui.QLabel(self.groupBox_6)
        self.label_x.setObjectName(_fromUtf8("label_x"))
        self.horizontalLayout_5.addWidget(self.label_x)
        self.spinBox_y = QtGui.QSpinBox(self.groupBox_6)
        self.spinBox_y.setSpecialValueText(_fromUtf8(""))
        self.spinBox_y.setMinimum(1)
        self.spinBox_y.setProperty("value", 5)
        self.spinBox_y.setObjectName(_fromUtf8("spinBox_y"))
        self.horizontalLayout_5.addWidget(self.spinBox_y)
        self.label_y = QtGui.QLabel(self.groupBox_6)
        self.label_y.setObjectName(_fromUtf8("label_y"))
        self.horizontalLayout_5.addWidget(self.label_y)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3.addWidget(self.groupBox_6)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox_2 = QtGui.QGroupBox(NDVIcalculatorDialogBase)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.lineEdit_output = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_output.setText(_fromUtf8(""))
        self.lineEdit_output.setObjectName(_fromUtf8("lineEdit_output"))
        self.horizontalLayout_6.addWidget(self.lineEdit_output)
        self.button_output = QtGui.QPushButton(self.groupBox_2)
        self.button_output.setObjectName(_fromUtf8("button_output"))
        self.horizontalLayout_6.addWidget(self.button_output)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.button_box = QtGui.QDialogButtonBox(NDVIcalculatorDialogBase)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.verticalLayout.addWidget(self.button_box)

        self.retranslateUi(NDVIcalculatorDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), NDVIcalculatorDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), NDVIcalculatorDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(NDVIcalculatorDialogBase)

    def retranslateUi(self, NDVIcalculatorDialogBase):
        NDVIcalculatorDialogBase.setWindowTitle(_translate("NDVIcalculatorDialogBase", "NDVI calculator", None))
        self.groupBox_5.setTitle(_translate("NDVIcalculatorDialogBase", "Input File", None))
        self.button_input.setText(_translate("NDVIcalculatorDialogBase", "Open ...", None))
        self.groupBox_4.setTitle(_translate("NDVIcalculatorDialogBase", "Settings", None))
        self.groupBox_3.setTitle(_translate("NDVIcalculatorDialogBase", "Band numbers", None))
        self.label_nir.setText(_translate("NDVIcalculatorDialogBase", "NIR", None))
        self.label_red.setText(_translate("NDVIcalculatorDialogBase", "RED", None))
        self.groupBox_6.setTitle(_translate("NDVIcalculatorDialogBase", "Tile size", None))
        self.label_x.setText(_translate("NDVIcalculatorDialogBase", "X", None))
        self.label_y.setText(_translate("NDVIcalculatorDialogBase", "Y", None))
        self.groupBox_2.setTitle(_translate("NDVIcalculatorDialogBase", "Output file", None))
        self.button_output.setText(_translate("NDVIcalculatorDialogBase", "Open ...", None))

