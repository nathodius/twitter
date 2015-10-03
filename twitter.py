#!/usr/bin/env python 

"""
Client Raspberry Pi: RPi1
"""

from twython import TwythonStreamer
import socket
import sys

# Begin socket configuarion

host = '172.31.105.225'
port = 50000
size = 1024
s = None

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
except socket.error, (value, message):
    if s: 
        s.close()
    print "Could not open socket: " + message
    sys.exit(1)

# End socket configuration

# Begin Twitter stream configuration.

# Search terms
TERMS = '#___test___'

# Twitter application authentication
APP_KEY = 'unNmv51PCE2eVPOQluDFM2OSH'
APP_SECRET = 'IugneaTKwmTygdr0oYpHnAvrWGCVyCix1ezPj8jvg8W0mVPrHH'
OAUTH_TOKEN = '192687808-79frLMJTsz3ogb2vFJdRZH7gEovCcvTlwZ315i0T'
OAUTH_TOKEN_SECRET = 'TzWz8QUolxaUPgt0G0DYmILMqPiTbfSeL67dnwRAcvGpB'

# Setup callbacks from Twython Streamer
class TweetStreamer(TwythonStreamer):
        def on_success(self, data):
                if 'text' in data:
                        print data['text'].encode('utf-8')
                        s.send('Blink')

        def on_error(self, status_code, data):
            print status_code
            self.disconnect()

# Create streamer
try:
        stream = TweetStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        stream.statuses.filter(track=TERMS)
except KeyboardInterrupt:
        print '\ndone'
        s.close()

# End Twitter stream configuration


