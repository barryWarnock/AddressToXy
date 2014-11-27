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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from AddressToXyDialog import AddressToXyDialog

#This class is the entrance point for QGis
class AddressToXy: 

  def __init__(self, iface):
    # Save reference to the QGIS interface
    self.iface = iface

  def initGui(self):  
    # Create action that will start plugin configuration
    self.action = QAction(QIcon(":/plugins/AddressToXy/icon.png"), \
        "Address To Xy", self.iface.mainWindow())
    # connect the action to the run method
    QObject.connect(self.action, SIGNAL("activated()"), self.run) 
    # Add toolbar button and menu item
    self.iface.addToolBarIcon(self.action)
    self.iface.addPluginToMenu("&Address To Xy", self.action)

  def unload(self):
    # Remove the plugin menu item and icon
    self.iface.removePluginMenu("&Address To Xy",self.action)
    self.iface.removeToolBarIcon(self.action)

  # run method that is called after initialization
  def run(self): 
    #create and show the dialog I passes the
    #of the qgisInterface to AddressToXyDialog
    #so that it could access the active layers
    dlg = AddressToXyDialog(self.iface) 
    # show the dialog
    dlg.show()
    #control is handed over to AddressToXyDialog
    #I did this so that the main code could be 
    #closer to the Qt interface
    dlg.exec_() 
    
