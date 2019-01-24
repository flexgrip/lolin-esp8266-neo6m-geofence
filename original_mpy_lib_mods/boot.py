# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
import webrepl
import uos, machine

uos.dupterm(uart, 1)
webrepl.start()
gc.collect()
