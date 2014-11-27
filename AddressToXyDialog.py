"""
/***************************************************************************
Name			 	 : Address to Lat Long
Description          : takes address fields and adds lat / long fields to the attribute table.
Date                 : 13/Nov/14 
copyright            : (C) 2014 by Barry Warnock
email                : warnock@unbc.ca 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4 import QtCore, QtGui 
from Ui_AddressToXy import Ui_AddressToXy
# create the dialog for AddressToXy
class AddressToXyDialog(QtGui.QDialog):
  def __init__(self, main): 
    QtGui.QDialog.__init__(self) 
    self.main = main
    self.layer_list = []
    # Set up the user interface from Designer. 
    self.ui = Ui_AddressToXy ()
    self.ui.setupUi(self)
  def OK(self):
	  self.close()
  def Cancle(self):
	  self.close()
  def CsvSelect(self, num):
	  self.id = num
	  lay = self.main.iface.mapCanvas().layer(num)
	  lay.	
  def AddressSelect(self):
	  print "Nothing much going on here quite yet"
