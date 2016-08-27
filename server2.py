#!/usr/bin/python
from socket import socket
from time import localtime
from random import randrange
#from PIL import ImageGrab



server = socket()
#server.shutdown(1)
#server.close()
req = {}
print "***Connecting..."
port = input("Enter a port\n")
server.bind(('10.0.0.8',port))
print "***Connected."
server.listen(1)
print "***Listenning..."
(client_socket, client_address) = server.accept()
while True:
	req = {}
	try:
		data_temp = str(client_socket.recv(1024))
		data = data_temp.replace('\n','')
		data = data.split(' ')
		print data
		if len(data) != 3:
			client_socket.send('Did You Send a HTTP Request?\n')
                        print "Wrong Request"
			continue
		req['reqName'] = data[0]
		req['reqItem'] = data[1]
		temp = data[2].split('/')
		req['reqProtocol'] = temp[0]
		req['reqVersion'] = temp[1]	
		if req['reqName'] != 'GET':
			client_socket.send('We Only Except GET Requests\n')
			print "---Wrong Request---"
			continue
		elif (req['reqProtocol'] != 'HTTP') or (req['reqVersion'] != '1.1'):
			client_socket.send('We Only Except HTTP ver 1.1 Requests\n')
			print "---Wrong Request---\n"
			continue
		elif req['reqItem'][0]  != '/':
			client_socket.send("Wrong Item Location Request\n")
			print "---Wrong Item Request---\n"
			continue
		else:
			client_socket.send(str(req['reqItem']+'\n'))
			continue
	except socket.error:
		break
print "Server shutdown\n"
client_socket.close()
server.close()
