## D-Bus-Service-Current-Time 
[![made with &hearts in Python](https://img.shields.io/badge/made%20with%20%E2%9D%A4%20in-Python-red.svg)](http://shields.io/#your-badge)


D-Bus is a message bus that Linux systems use in order to make programs communicate with each other or with the system itself. It allows applications to integrate amongst themselves using well-defined interfaces. This allows each application to provide services that can be used by others, sort of like adding API’s to your programs.

Here I have implemented a small D-Bus service and a client to consume it. It returns the current time. 

![alt text](https://github.com/PiyushBhangale/D-Bus-Service-Current-Time/blob/master/ezgif.com-video-to-gif.gif)

## How to run it

Run the service we wrote in a terminal and run the client from another terminal, you should get the time printed on your console.

To run the service.
```
python dbusservice.py
```

To run the client.
```
python dbus-client.py
```


