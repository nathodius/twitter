#!/usr/bin/env python
# -*- coding: utf-8 -*- 

""" 
Nathaniel Hughes
Christina Nguyen

ECE 4564, Fall 2015
Assignment 1
"""

import socket

host = ''
port = 50000
backlog = 1 # One client will be conencting to the server
size = 1024

s = None
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Uses IPv4 and TCP
	s.bind((host,port))
	s.listen(backlog) 
except socet.error, (value, message):
	if s:
		s.close()
	print "Could not open socket: " + message
	sys.exit(1)

while 1:
     conn, addr = s.accept() 
     data = conn.recv(1024)
     if data:
          conn.send(data)
          print data
conn.close()
