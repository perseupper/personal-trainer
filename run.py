#!/usr/bin/python3
from app import app
from sense_hat import SenseHat

sense = SenseHat()

sense.show_message("Starting...")
app.run(host='0.0.0.0', port=80, debug=True)
