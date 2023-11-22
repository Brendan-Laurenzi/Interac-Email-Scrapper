# 1. MAKE SURE THE PATH IS IN THIS FOLDER

## CONVERT ui filetype to python format

#2. c:\Users\brend\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts\pyuic6.exe -x .\interface.ui -o 'c:\Users\brend\Desktop\Coding Stuff\Interac-Email-Scrapper\ui_interface.py'

## CONVERT qrc filetype to python format

#3. pyside6-rcc .\resources.qrc -o 'c:\Users\brend\Desktop\Coding Stuff\Interac-Email-Scrapper\resources_re.py'

## Include qrc import in ui_py file

#4. import resources_re