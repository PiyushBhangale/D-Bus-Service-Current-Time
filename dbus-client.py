import dbus
from dbusservice import *

bus = dbus.SessionBus()
t = bus.get_object('com.gkbrk.Time', '/Time')
while True:
    time.sleep(1)
    curr = t.CurrentTime()
    print('The current time is', curr)
