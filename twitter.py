#!/usr/bin/env python 

"""
Client Raspberry Pi: RPi1
"""

import time
from twython import Twython
from twython import TwythonStreamer
import socket
import sys

# Begin Twitter stream configuration.

# Search terms
TERMS = '@nathodius'

host = '10.0.0.134'
port = 50000
size = 1024
s = None

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    s.connect((host,port))
except socket.error, (value, message):
    if s: 
        s.close()
    print "Could not open socket: " + message
    sys.exit(1)

s.send('LEDFLASH')
data = s.recv(size)
s.close()
s.close()
print 'Received:', data

# def connectToHost(ip):
#     # Begin socket configuarion

#     host = ip

#     try:
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         s.settimeout(5)
#         s.connect((host,port))
#     except socket.error, (value, message):
#         if s: 
#             s.close()
#         print "Could not open socket: " + message
#         sys.exit(1)

# # # End socket configuration

# def sendCommand(command):
#     parsedCommand = command.split('_')
#     byte1 = parsedCommand[1]
#     byte2 = parsedCommand[2]
#     byte3 = parsedCommand[3]
#     byte4 = parsedCommand[4]
#     gpioCommand = parsedCommand[5]
#     host = byte1 + '.' + byte2 + '.' + byte3 + '.' + byte4
#     print host
#     connectToHost(host)
#     s.send(gpioCommand)

# #Twitter application authentication
# APP_KEY = 'unNmv51PCE2eVPOQluDFM2OSH'
# APP_SECRET = 'IugneaTKwmTygdr0oYpHnAvrWGCVyCix1ezPj8jvg8W0mVPrHH'
# OAUTH_TOKEN = '192687808-79frLMJTsz3ogb2vFJdRZH7gEovCcvTlwZ315i0T'
# OAUTH_TOKEN_SECRET = 'TzWz8QUolxaUPgt0G0DYmILMqPiTbfSeL67dnwRAcvGpB'

# # #Setup callbacks from Twython Streamer
# class TweetStreamer(TwythonStreamer):
#         def on_success(self, data):
#                 if 'text' in data:
#                         txt = data['text'].encode('utf-8')
#                         words = txt.split()
#                         print words
#                         for word in words:
#                             if word.starswith('#'):
#                                 print word
#                         #s.send('Blink')

#         def on_error(self, status_code, data):
#             print status_code
#             self.disconnect()

# try:
#         stream = TweetStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
#         stream.statuses.filter(track=TERMS)
#         # while True:
#         #     user_timeline = t.get_mentions_timeline(count=1)
#         #     for tweet in user_timeline:
#         #         if '#ECE4564' in tweet['text'].encode('utf-8'):
#         #             print 'getting a command'
#         #             command = tweet['text'].encode('utf-8')
#         #             sendCommand(command)
#         #     time.sleep(5)
# except KeyboardInterrupt:
#         #s.close()
#         print 'KeyboardInterrupt'

# End Twitter stream configuration


