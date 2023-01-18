#!/usr/bin/env python3
# Author: Shane Harrell

from signalwire.voice_response import *
import urllib.parse
from flask import Flask
from flask import request
denoise = Flask(__name__)

@amd.route('/', methods=['GET'])
def denoisify():

    dest = request.args.get('Dest')

    # Denoise=off param will override and set denoise off. 
    if request.args.get('Denoise') is not None:
        denoise = request.args.get('Denoise')
    else:
        # Set denoise as a default
        denoise = "on"

    # Are we going to a sip location?
    if dest.startswith('sip:'):
        dest = '<Sip>' + dest + '</Sip>'

    response = '''<?xml version="1.0" encoding="UTF-8"?>
    <Response>
        <Denoise>''' + denoise + '''</Denoise>
        <Dial>''' + dest + '''</Dial>
    </Response>'''

    return str(response)



if __name__ == '__main__':
    denoise.run()
