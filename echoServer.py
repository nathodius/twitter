#!/usr/bin/env python
# -*- coding: utf-8 -*- 

""" 
	Nathaniel Hughes
	Christina Nguyen

	ECE 4564, Fall 2015
	Assignment 1
"""

"""
	Pi2: Server
"""

import socket
import time
import RPi.GPIO as GPIO

host = ''
port = 50000
backlog = 1 # One client will be conencting to the server
size = 1024
LED_PORT = 12 # GPIO pin 18

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

# Infinite loop reads a message from client and echos it back
while 1:
     # conn is a new socket object used to communicate with the client
     conn, addr = s.accept() 
     data = conn.recv(1024)
     if data == 'LEDON':
     	  GPIO.output(LED_PORT, GPIO.HIGH)
	  conn.send(data + 'received!')

     else if data == 'LEDOFF':
     	  GPIO.output(LED_PORT, GPIO.LOW)
	  conn.send(data + 'received!')

     else if data == 'LEDFLASH':
     	  GPIO.output(LED_PORT, GPIO.HIGH)
	  time.sleep(0.5) # Blocking call
	  GPIO.output(LED_PORT, GPIO.LOW)
	  conn.send('Huzzah! LED is flashing!')
     else:
     	  conn.send('Invalid GPIO instruction.')

          #conn.send(data)
          #print data
conn.close()
