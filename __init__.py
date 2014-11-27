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
 This script initializes the plugin, making it known to QGIS.
"""
def name(): 
  return "Address to Lat Long" 
def description():
  return "takes address fields and adds lat / long fields to the attribute table."
def version(): 
  return "Version 0.1" 
def qgisMinimumVersion():
  return "2"
def classFactory(iface): 
  # load AddressToXy class from file AddressToXy
  from AddressToXy import AddressToXy 
  return AddressToXy(iface)
