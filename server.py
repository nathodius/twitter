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
import sys

host = ''
port = 50000
backlog = 1 # One client will be conencting to the server
size = 1024
LED_PORT = 12 # GPIO pin 18

flashFlag = False; # Flag for flashing LED (on separate thread)

# Setup GPIO as output
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PORT, GPIO.OUT)
GPIO.output(LED_PORT, GPIO.LOW)

s = None
try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Uses IPv4 and TCP
        s.bind((host,port))
except socket.error, (value, message):
	if s:
		s.close()
	print "Could not open socket: " + message
	sys.exit(1)

print 'Socket successfully created and binded.'

def led_flash():
        while flashFlag == True:
		GPIO.output(LED_PORT, GPIO.HIGH)
		time.sleep(1) # Blocking call
		GPIO.output(LED_PORT, GPIO.LOW)
		time.sleep(1) # Blocking call
		if(flashFlag == False):
			break;

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
	flashFlag = False
	print "Mode: LED on"
        GPIO.output(LED_PORT, GPIO.HIGH)
        conn.send(data + 'received!')

     elif data == 'LEDOFF':
	flashFlag = False
	print "Mode: LED off"
        GPIO.output(LED_PORT, GPIO.LOW)
        conn.send(data + 'received!')

     elif data == 'LEDFLASH':
	flashFlag = True
	print "Mode: LED flash"
        t=Thread(target=led_flash, args=())
        t.start()
        conn.send('Flash that LED!')
     else:
          conn.send('Invalid GPIO instruction or data not received.')

conn.close()
