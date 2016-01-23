#!/usr/bin/python3
from app import app
from sense_hat import SenseHat
import netifaces as ni

ni.ifaddresses('eth0')
ip = ni.ifaddresses('eth0')[2][0]['addr']

sense = SenseHat()

sense.show_message("Starting on {}".format(ip))
app.run(host='0.0.0.0', port=80, debug=True)
