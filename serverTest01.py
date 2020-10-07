#!/usr/bin/python

import socket
import sys
from thread import *

HOST = ''
PORT = 8888

#make socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('...socket created...ä)

#bind socket

try:
	s.bind((HOST, PORT))
except socket.errors, msg:
	print('...bind failed...error code: ' + str(msg[0]) + ', messgae: ' + msg[1])
	sys.exit()

print('...socket bind complete...')

#make socket listen

s.listen(10)
print('...socket listening...')

#function for connection-handling

def clientThread(conn):
	
	conn.send('...welcome to the server...type something and hit enter \n')
	
	while True:
		data = conn.recv(1024)
		reply = '...OK...' + data
		if not data:
			break
		
		conn.sendall(reply)
	conn.close()

#keep the conversation going

while 1:
	conn, addr = s.acept()
	
	print('...connected with: ' + addr[0] + ': ' + str(addr[1])
	
	start_new_thread(clientThread, (conn,))
	
s.close()
