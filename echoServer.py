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
from threading import Thread

host = ''
port = 50000
backlog = 1 # One client will be conencting to the server
size = 1024
LED_PORT = 12 # GPIO pin 18

s = None
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Uses IPv4 and TCP
	s.bind((host,port))
except socet.error, (value, message):
	if s:
		s.close()
	print "Could not open socket: " + message
	sys.exit(1)

print 'Socket successfully created and binded.'

def led_flash():
	GPIO.output(LED_PORT, GPIO.HIGH)
	time.sleep(0.5) #Blocking call
	GPIO.output(LED_PORT, GPIO.LOW)

# Start listening on socket
s.listen(backlog)
print 'Socket is listening...'

# Infinite loop reads a message from client and echos it back
while True:
     # Wait to accept a connection; blocking call
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
     	t=Thread(target=led_flash, args=(,))
	t.start()
	conn.send('Flash that LED!')
     else:
     	  conn.send('Invalid GPIO instruction or data not received.')

          #conn.send(data)
          #print data
conn.close()
