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

from PyQt5.QtCore import QTimer, QPropertyAnimation, QEasingCurve, pyqtProperty
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QVBoxLayout, QSlider
from PyQt5.QtGui import QFont, QFontDatabase


################################################################################################
# Convert UI to PyQt5 py file
################################################################################################
os.system("pyuic5 -o interface_ui.py interface.ui")
# os.system("pyuic5 -o analoggaugewidget_demo_ui.py analoggaugewidget_demo.ui.oQCkCR")

################################################################################################
# Import the generated UI
################################################################################################
from interface_ui import *


################################################################################################
# MAIN WINDOW CLASS
################################################################################################
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

        ################################################################################################
        # Setup the UI main window
        ################################################################################################
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
        ################################################################################################
        # Show window
        ################################################################################################
        self.show()

        ################################################################################################
        # Customize the analog gauge widget
        ################################################################################################
        self.ui.widget.enableBarGraph = False

        ################################################################################################
        # Set Gauge Unit
        ################################################################################################
        self.ui.widget.units = "%"

        ################################################################################################
        # Set the minimun gauge value
        ################################################################################################
        self.ui.widget.minValue = 0

        ################################################################################################
        # Set the maximun gauge value
        ################################################################################################
        self.ui.widget.maxValue = 100

        ################################################################################################
        # Set Scale Divisins
        ################################################################################################
        self.ui.widget.scalaCount = 10

        # Start from the minimum value
        self.ui.widget.updateValue(self.ui.widget.minValue)
        # OR
        # Start from half/middle value
        # self.ui.widget.updateValue(int(self.ui.widget.maxValue - self.ui.widget.minValue)/2)
        # Start from a value
        # self.ui.widget.updateValue(50)

        ################################################################################################
        # Select Gauge theme  [ from 0 to 24 ]
        ################################################################################################
        self.ui.widget.setGaugeTheme(24)

        ################################################################################################
        # Select Gauge theme with colors    Video Links: Color Picker: https://image-color.com/
        ################################################################################################
        #self.ui.widget.setCustomGaugeTheme(
        #    color1 = "#FF2B00",
        #    color2 = "#821600",
        #    color3 = "#260600"
        #)

        ################################################################################################
        # set scale polygonColor
        ################################################################################################
        #self.ui.widget.setScalePolygonColor( color1 = "red")

        ################################################################################################
        # set scale polygonColor
        ################################################################################################
        self.ui.widget.setNeedleCenterColor( color1 = "red")
        #self.ui.widget.setOuterCircleColor(color1 = "white" , color2 = "red" , color3 = "green")
        #self.ui.widget.setBigScaleColor("red")
        #self.ui.widget.setFineScaleColor("white")

        ################################################################################################
        ################################################################################################
        # Set Custom Font
        ################################################################################################
        ################################################################################################
        #QFontDatabase.addApplicationFont(os.path.dirname(__file__), 'font/ds_digital/DS-DIGIB.TTF')
        #self.ui.widget.setValueFontFamily("DS-Digital")

        ################################################################################################
        ################################################################################################
        # Mouse Tracking
        ################################################################################################
        ################################################################################################
        self.ui.widget.setMouseTracking(False)

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
        # read the data from the serial port
        data = self.ser.readline()
        if data:
            # detect the encoding of the data
            encoding = chardet.detect(data)['encoding']
            # decode the data using the detected encoding
            decoded_data = data.decode(encoding).rstrip()
            # convert the data to a float and display it on the LCD
            try:
                value1 = float(decoded_data)
                #self.ui.widget.value = value1
                #self.ui.widget.repaint()
                start_value = self.ui.widget.value
                self.smooth_update_value(start_value, value1, 10)  # Duration in milliseconds
                print("Received data: ", value1) # for debugging
            except ValueError:
                print("Invalid data format: ", decoded_data) # for debugging
                pass
        else:
            print("No data received") # for debugging

########################################################################
## smooth update for the value momen
########################################################################

    def smooth_update_value(self, start_value, end_value, duration):
        step_count = int(duration / 1)  # Update every 10 milliseconds
        value_diff = end_value - start_value
        step_value = value_diff / step_count

        for i in range(step_count):
            current_value = start_value + (i * step_value)
            self.ui.widget.setValue(current_value)
            QApplication.processEvents()
            QtCore.QThread.msleep(10)

        self.ui.widget.setValue(end_value)

########################################################################
## EXECUTE APP
########################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

########################################################################
## END===>
########################################################################  