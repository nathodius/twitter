#!/usr/bin/env python
# -*- coding: utf-8 -*- 

""" 
A simple echo server 
"""

import socket

host = ''
port = 50000
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
while 1:
     conn, addr = s.accept() 
     data = conn.recv(1024)
     if data:
          conn.send(data)
          print data
conn.close()
