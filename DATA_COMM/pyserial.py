#To install use pip.
#==>  sudo pip3 install pyserial

#To read serial data, you can use the Python serial library.
import serial
import pmd

#You need to specify the serial port you art using when you create your serial object. For instance:

#Additionally you may need to specify settings that are specific to
#the device that is communicating using the serial communication protocol.

ser = serial.Serial('dev/ttyAMA0',
                    baudrate=9600,
					parity=serial.PARITY_NONE,
					stopbits=serial.STOPBITS_ONE)

#Bytes are sent from your device to your computer at a set frequency.
#  Flow control for serial communication works on the principles of First In First Out (FIFO).
#  So when you call pmd.read() you are reading the oldest byte in the input buffer.

#Add two lines to store and the print out the oldest byte in the input buffer

# ==> pip install pmd   may also need ==> pip install numpy
#If you want to read more than a single byte, you can specify how many bytes to read
data = pmd.read(10)
print(bytes)

#Once you have read the bytes, they are removed from the input buffer.

#If you need to clear the input buffer, to remove old data, you can use the following line.
pmd.reset_output_buffer()

#Add the following lines to view the values of specific bytes. This will output the integer values of the bytes.
first_byte = data[0]
second_byte = data[1]

print(first_byte, second_byte)