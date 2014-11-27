# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_AddressToXy.ui'
#
# Created: Fri Nov 21 11:57:55 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AddressToXy(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(242, 124)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Ok_button = QtGui.QPushButton(self.centralwidget)
        self.Ok_button.setGeometry(QtCore.QRect(20, 80, 75, 21))
        self.Ok_button.setObjectName(_fromUtf8("Ok_button"))
        self.Cancle_button = QtGui.QPushButton(self.centralwidget)
        self.Cancle_button.setGeometry(QtCore.QRect(100, 80, 75, 21))
        self.Cancle_button.setObjectName(_fromUtf8("Cancle_button"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 131, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.Column_dropdown = QtGui.QComboBox(self.centralwidget)
        self.Column_dropdown.setGeometry(QtCore.QRect(110, 50, 111, 22))
        self.Column_dropdown.setObjectName(_fromUtf8("Column_dropdown"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.CsvDropdown = QtGui.QComboBox(self.centralwidget)
        self.CsvDropdown.setGeometry(QtCore.QRect(110, 20, 111, 22))
        self.CsvDropdown.setObjectName(_fromUtf8("CsvDropdown"))
        #MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        #MainWindow.setStatusBar(self.statusbar)
	
	#build a list of current layers by index and add them to CsvDropdown
	self.size = MainWindow.main.iface.mapCanvas().layerCount()
        for i in range(self.size):
		MainWindow.layer_list.append((MainWindow.main.iface.mapCanvas().layer(i).id()))
		self.CsvDropdown.addItem(MainWindow.main.iface.mapCanvas().layer(i).name())

        self.retranslateUi(MainWindow)
	self.Ok_button.clicked.connect(MainWindow.OK)    
	self.Cancle_button.clicked.connect(MainWindow.Cancle)
	self.CsvDropdown.currentIndexChanged.connect(MainWindow.CsvSelect)
	self.Column_dropdown.highlighted.connect(MainWindow.AddressSelect)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "AddressToXy", None, QtGui.QApplication.UnicodeUTF8))
        self.Ok_button.setText(QtGui.QApplication.translate("MainWindow", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.Cancle_button.setText(QtGui.QApplication.translate("MainWindow", "Cancle", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", ".csv file ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Address Column", None, QtGui.QApplication.UnicodeUTF8))

