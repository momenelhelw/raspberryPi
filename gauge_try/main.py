#Github: https://github.com/KhamisiKibet/QT-Py...
#PyPi / Installing Custom Widgets: https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbmVKb21BY3pQZUFTcUdQYkNJeWNXYWtnRDV1d3xBQ3Jtc0tuNWNndFE0b2ZlR3FnTkxFTXNZcUtCUmEwbXo1b0FWc3ZSeENOSTVWVDVFdk1Ndy1TR3hzanZhSmtmWkJvYWdZSmdfOVlQSFZGTzVkbkhKbUFJLXpZM2V1UlJCek01OGwyeEZITlN5ckRiU0RpNnlzWQ&q=https%3A%2F%2Fpypi.org%2Fproject%2FQT-PyQt-PySide-Custom-Widgets%2F&v=5WHnlRQcUy4
########################################################################
# IMPORTS
########################################################################
import os
import sys
import serial
import chardet
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, QPropertyAnimation, QEasingCurve, QDateTime
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QVBoxLayout, QSlider, QDateTimeEdit
from PyQt5.QtGui import QFont, QFontDatabase

###########################################################################################
# Convert UI to PyQt5 py file
###########################################################################################
os.system("pyuic5 -o interface_ui.py interface.ui")
# os.system("pyuic5 -o analoggaugewidget_demo_ui.py analoggaugewidget_demo.ui.oQCkCR")

os.system("pyrcc5 -o Resources_rc.py Resources.qrc")
###################################################
# Import the generated UI
###################################################
from interface_ui import *

####################################################
# MAIN WINDOW CLASS
####################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
    
        ########################################################################
        ## Pyserial setting momen
        ########################################################################
                # configure the serial port
        self.ser = serial.Serial(
            port='/dev/ttyS0', # replace with the appropriate port name
            baudrate=9600, # set the baud rate
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1 # set the timeout value
        )

        #############################################
        # Setup the UI main window
        #############################################
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
        #############################################
        # Show window
        #############################################
        self.show()

########################################################################################################
################################################# SPEED ################################################
########################################################################################################
        self.ui.speed.enableBarGraph = False
        self.ui.speed.units = "k/h"
        self.ui.speed.minValue = 0
        self.ui.speed.maxValue = 300
        self.ui.speed.scalaCount = 10
        # Start from the minimum value
        self.ui.speed.updateValue(self.ui.speed.minValue)
        ##################################################################
        # Select Gauge theme  [ from 0 to 24 ]
        ##################################################################
        self.ui.speed.setGaugeTheme(24)
        self.ui.speed.setMouseTracking(False)

########################################################################################################
################################################# tempreture ###########################################
########################################################################################################
        self.ui.temp.enableBarGraph = False
        self.ui.temp.units = "°C"
        self.ui.temp.minValue = 0
        self.ui.temp.maxValue = 100
        self.ui.temp.scalaCount = 10
        # Start from the minimum value
        self.ui.temp.setEnableFineScaleGrid(False)
        self.ui.temp.updateValue(self.ui.temp.minValue)
        ####################################################################
        # Select Gauge theme  [ from 0 to 24 ]
        ####################################################################
        self.ui.temp.setGaugeTheme(23)
        self.ui.temp.setMouseTracking(False)

########################################################################################################
################################################# battery ##############################################
########################################################################################################
        self.ui.battery.enableBarGraph = False
        self.ui.battery.units = "%"
        self.ui.battery.minValue = 0
        self.ui.battery.maxValue = 100
        self.ui.battery.scalaCount = 10
        # Start from the minimum value
        self.ui.battery.updateValue(self.ui.battery.minValue)
        #######################################################################
        # Select Gauge theme  [ from 0 to 24 ]
        #######################################################################
        self.ui.battery.setGaugeTheme(7)
        self.ui.battery.setMouseTracking(False)


########################################################################
## Timer momen
########################################################################

    
        # create a timer to periodically update the LCD display
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_lcd)
        self.timer.start(100) # update every 100 milliseconds
        


########################################################################
## update value momen
########################################################################

    def update_lcd(self):
        #this is for current time update for time date
        self.ui.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        #this is for no select the day section of the time date
        self.ui.dateTimeEdit.setCurrentSection(QDateTimeEdit.NoSection)
        # read the data from the serial port
        data = self.ser.readline()
        if data:
            # detect the encoding of the data
            encoding = chardet.detect(data)['encoding']
            # decode the data using the detected encoding
            decoded_data = data.decode(encoding).rstrip()
            # convert the data to a float and display it on the LCD
            try:
                if decoded_data.startswith('S'):
                    speed_value = float(decoded_data[1:])
                    start_value = self.ui.speed.value
                    self.smooth_update_speed_value(start_value, speed_value, 10)  # Duration in milliseconds
                    print("Received data: ", decoded_data) # for debugging

                elif decoded_data.startswith('B'):
                    battery_value = float(decoded_data[1:])
                    start_value = self.ui.battery.value
                    self.smooth_update_battery_value(start_value, battery_value, 10)  # Duration in milliseconds
                    print("Received data: ", decoded_data) # for debugging

                elif decoded_data.startswith('T'):
                    temp_value = float(decoded_data[1:])
                    start_value = self.ui.temp.value
                    self.smooth_update_temp_value(start_value, temp_value, 10)  # Duration in milliseconds
                    print("Received data: ", decoded_data) # for debugging

                elif decoded_data.startswith('F'):
                    self.ui.graphicsView.setStyleSheet(u"background-color: rgb(157, 157, 157);\n"
"border-image: url(:/light/lightbulb.png);")

                elif decoded_data.startswith('O'):
                    self.ui.graphicsView.setStyleSheet(u"background-color: rgb(157, 157, 157);\n"
"border-image: url(:/light/light-bulb-on.png);")
                    print("Received data: ", decoded_data)  # for debugging

            except ValueError:
                print("Invalid data format: ", decoded_data) # for debugging
                pass
        
        else:
            print("No data received") # for debugging

########################################################################
## smooth update for the value momen
########################################################################

    def smooth_update_speed_value(self, start_value, end_value, duration):
        step_count = int(duration / 1)  # Update every 10 milliseconds
        value_diff = end_value - start_value
        step_value = value_diff / step_count
        
        for i in range(step_count):
            current_value = start_value + (i * step_value)
            self.ui.speed.setValue(current_value)
            QApplication.processEvents()
            QtCore.QThread.msleep(10)

        self.ui.speed.setValue(end_value)

#########           battery           #########

    def smooth_update_battery_value(self, start_value, end_value, duration):
        step_count = int(duration / 1)  # Update every 10 milliseconds
        value_diff = end_value - start_value
        step_value = value_diff / step_count
        
        for i in range(step_count):
            current_value = start_value + (i * step_value)
            self.ui.battery.setValue(current_value)
            self.ui.progressBar.setValue(current_value)
            QApplication.processEvents()
            QtCore.QThread.msleep(10)

        self.ui.battery.setValue(end_value)
        self.ui.progressBar.setValue(end_value)

#########           tempreture           #########

    def smooth_update_temp_value(self, start_value, end_value, duration):
        step_count = int(duration / 1)  # Update every 10 milliseconds
        value_diff = end_value - start_value
        step_value = value_diff / step_count
        
        for i in range(step_count):
            current_value = start_value + (i * step_value)
            self.ui.temp.setValue(current_value)
            QApplication.processEvents()
            QtCore.QThread.msleep(10)

        self.ui.temp.setValue(end_value)

##################CLOCK / DATE ########################################
        self.ui.dateTimeEdit = QDateTimeEdit()
        self.ui.dateTimeEdit.setDateTime(QDateTime.currentDateTime())

########################################################################
## EXECUTE APP
########################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
