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
#these are the methods I wrote before that I will be using in the plugin:
import urllib
import json
import csv
from PyQt4 import QtCore, QtGui 
from Ui_AddressToXy import Ui_AddressToXy
from qgis.core import *

#uses an address to create a url to use to retrieve lat long values
def addressToUrl(address):
		url = "https://apps.gov.bc.ca/pub/geocoder/addresses.geojson?addressString="
		url += address
		urlReturn = urllib.urlopen(url)
		return urlReturn

#takes a url and returns a json
def urlToJson(url):
        data = json.load(url)
        return data

#takes an address, uses it to get a url, uses the url to get a json and pulls the lat long values from the json
def addressToXy(address):
        url = addressToUrl(address)
        data = urlToJson(url)
        print(data['features'][0]['geometry']['coordinates']);
        return data['features'][0]['geometry']['coordinates']

#pulls the addresses out of the full 2d list by taking everything under the attribute with the given name
def getAddressList(fullList, attributeName):     
	#finds the column the addresses are in by itterating through the header until a name matches the given one
	for col in range(len(fullList[0])):
		if fullList[0][col] == attributeName:
			addressRow = col
	addressList = []
	#takes whatever is in that column in every other row	
	for row in range(len(fullList)-1):
		addressList.append(fullList[row+1][addressRow] if fullList[row+1][addressRow] else "")
	return addressList

#uses addressToXy on every element in the given list of addresses
def addressListToXy(addressList):
	latLongList = []	
	for address in addressList:
		latLongList.append(addressToXy(address))
	return latLongList

#adds the lat long values to the 2d list then writes it to csv and adds it to the map
def writeToCsv(mainDialog, latLong, array):	
        #add lat and long to the header
	array[0].append("lat")
	array[0].append("long")
        #display the save dialog
	name = QtGui.QFileDialog.getSaveFileName(mainDialog, "Save as?", "/home")	
	#if the user didn't hit cancel open the csv, write to it and add to map
        if name:	
		o = open((name), "w+")
		writer = csv.writer(o)
		writer.writerow(array[0])
		for row in range(len(array)-1):
			array[row+1].append(latLong[row][1])
			array[row+1].append(latLong[row][0])
			writer.writerow(array[row+1])
		o.close()										
		lay = QgsVectorLayer(name + "?delimiter=%s&xField=%s&yField=%s" % (",", "long", "lat"), (mainDialog.selectedLayer.name() + "_with_lat_long"), "delimitedtext")
		QgsMapLayerRegistry.instance().addMapLayer(lay)
		return 1
	#otherwise return false so the plugin knows not to close yet	
	else:
		return 0


# create the dialog for AddressToXy
class AddressToXyDialog(QtGui.QDialog):
  def __init__(self, iface): 
    QtGui.QDialog.__init__(self) 
    self.iface = iface
    # Set up the user interface from Designer. 
    #Ui_AddressToXy handles all of the buttons and the main window
    self.ui = Ui_AddressToXy ()
    #setupUi adds all of the current layers to the csv dropdown list and also connects all the widgets to their respective functions
    self.ui.setupUi(self)
    #I use these variables to ensure that the user doesn't cause the plugin to try to find addresses before it knows what layer and 
    #attributes it is going to use to do so
    self.layerIsSelected = 0
    self.attributeIsSelected = 0

  #csvToList turns the selected layer into a 2d list that is easy to opperate on for the rest of the methods
  def csvToList(self):
	array = []	
	row = []
	#build the header	
	for i in range(len(self.selectedLayer.pendingAllAttributesList())):
		row.append(self.selectedLayer.attributeDisplayName(i))
	array.append(row)
	row = []
        #add each feature	
	itr = self.selectedLayer.getFeatures()
	for i in itr:
	  array.append(i.attributes())
	return array

  #when the Ok button is pressed and the user has selected a layer and an attribute this method uses a variety of other methods to turn
  #save the selected layer as a .csv with lat long values and add this new file to the map
  def OK(self):
	  if self.layerIsSelected and self.attributeIsSelected:
		#Idealy this would be a progress bar but due to time constraints I just went with what was easy		
		QtGui.QMessageBox.information(self, "", "The lat long values are being loaded from the internet, please be patient as this may take a while.")
		#builds the 2d list to be used by other methods		
		wholeCsv = self.csvToList()
		#pulls a list of addresses from the full 2d list
		addresses = getAddressList(wholeCsv, self.selectedLayer.attributeDisplayName(self.selectedAttribute))				
		#queries the web tool to get a set of lat long values for each address		
		latLong = addressListToXy(addresses)
		#as long as the user doesn't hit cancel in the save dialog this method saves the csv with lat long and adds it to the map		
		if writeToCsv(self, latLong, wholeCsv) == 1:
			self.close()
		
  def Cancle(self):
	  self.close()
  
  #if the user selects a layer it is retrieved and its attributes are added to the attribute drop down box
  def CsvSelect(self, num):
	  self.selectedLayer = self.iface.mapCanvas().layer(num)
	  self.layerIsSelected = 1
	  self.ui.Column_dropdown.clear()
	  for i in range(len(self.selectedLayer.pendingAllAttributesList())):
		self.ui.Column_dropdown.addItem(self.selectedLayer.attributeDisplayName(i))
  
  #when the user selects an attribute it is saved for further use		
  def AddressSelect(self, i):
	  self.selectedAttribute = i
	  self.attributeIsSelected = 1

