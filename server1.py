#!/usr/bin/python
from socket import socket
from time import localtime
from random import randrange
#from PIL import ImageGrab



server = socket()
#server.shutdown(1)
#server.close()
print "***Connecting..."
server.bind(('10.0.0.50',8821))
print "***Connected."
server.listen(1)
print "***Listenning..."
(client_socket, client_address) = server.accept()
while True:
	try:
		data = client_socket.recv(1024)
		if data == 'TIME':
			client_socket.send(str(localtime()))
			print "---sending time---\n"
		elif data == 'NAME':
			client_socket.send('Perlov Server\n')
			print "---sending server name---\n"
		elif data == 'RAND':
			client_socket.send(str(randrange(1,9)))
			print "---sending random number---\n"
#	elif data == "PrtScn":
#		im = ImageGrab.grab()
#		im.saver("/home/pi/python_programs/screen.jpg")
#		client_socket.send(load("/home/pi/python_programs/screen.jpg"))
		elif data.lower() == 'exit':
			client_socket.send('Goodbye\n')
			break
		else:
			client_socket.send('Wrong Command!\n')
			print "---recived wrong command---\n"
	except:
		break
print "Server shutdown\n"
client_socket.close()
server.close()
