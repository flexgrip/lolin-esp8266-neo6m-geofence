#from machine import UART
import utime

uart = UART(0, 9600)
uart.init(9600)

while True==True:
    val = uart.read()
    print(val)
    utime.sleep(1)
