var = raw_input("remake .py? y/n: ")
if (var == 'y'):
	import os
	os.system("pyuic4 Ui_AddressToXy.ui -o Ui_AddressToXy.py")
import py_compile
py_compile.compile("Ui_AddressToXy.py")
