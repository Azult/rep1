#!/usr/bin/python
from socket import socket

mySock = socket()
mySock.connect(('10.0.0.5',8820))
mySock.send('EXIT')
data = mySock.recv(1024)
print "Server respond:",data
mySock.close()



