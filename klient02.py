#!/usr/bin/python

import socket
import sys
from time import sleep

#create socket

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
	print("...failed to create socket ... error code" + str(msg[0]) + ". error message: " + msg[1])
	sys.exit()
print("...socket created...")

#get IP adress of remote server

host = "172.17.202.30" #serveri aadress
port = 8888

try:
	remote_ip = socket.gethostbyname(host)
except socket.gaierror:
	print("...hostname could not be resolved...exiting...")
	sys.exit()

print("...IP adress of " + host + " is " + remote_ip)

#connect to remote server

s.connect((remote_ip, port))

print("...socket connected to " + host + " on IP " + remote_ip)

#recive data

reply = s.recv(4096)

print(reply)

#send data to remote server

message = "switchOn"
while True:

        try:
                s.sendall(message)
        except socket.error:
                print("...send failed...")
                sys.exit()
        print("...message sent successfully..." + message)

        sleep(5)

        while True:
                reply = s.recv(4096)
                print(reply)
                if reply == "switchedOn":
                        sleep(10)
                        message = "switchOff"
                        break
                if reply == "switchedOff":
                        message = "terminate"
                        break
                sleep(1)
                s.sendall("mis teen?")
        if message == "terminate":
                break

#recive data

##reply = s.recv(4096)
##
##print(reply)

#close the socket

s.close()
