import dbus
import dbus.service
import time


class Time(dbus.service.Object):
    def __init__(self):
        self.bus = dbus.SessionBus()
        name = dbus.service.BusName('com.gkbrk.Time', bus=self.bus)
        dbus.service.Object.__init__(self, name, '/Time')
        # super().__init__(name, '/Time')

    @dbus.service.method('com.gkbrk.Time', out_signature='s')
    def CurrentTime(self):
        """Use strftime to return a formatted timestamp
        that looks like 23-02-2018 06:57:04."""

        formatter = '%d-%m-%Y %H:%M:%S'
        return time.strftime(formatter)


if __name__ == '__main__':
    import dbus.mainloop.glib
    from gi.repository import GLib

    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

    loop = GLib.MainLoop()
    object = Time()
    # print(object.CurrentTime())
    loop.run()
