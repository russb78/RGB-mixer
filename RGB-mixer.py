#!/usr/bin/env python
# RGB LED dimmer test
# Russell Barnes - 04 Sept 2013 (Updated 19th November for issue 134 of Linux User magazine).

from nanpy import Arduino
from time import sleep

# set LED pin numbers
redPin = 3
greenPin = 6
bluePin = 9

# set pot pin numbers
pot_r_Pin = 0
pot_g_Pin = 3
pot_b_Pin = 5

#set three coloured pins as outputs
for pins in (redPin, greenPin, bluePin):
	Arduino.pinMode(pins, Arduino.OUTPUT)

# set pot pins as inputs
for pins in (pot_r_Pin, pot_g_Pin, pot_b_Pin):
	Arduino.pinMode(pins, Arduino.INPUT)

# prints values to the terminal when True
debug = False

def get_pots():
	"""
	Grab a reading from each of the pot pins and 
	send it to a tuple to be read by the colour mixer
	"""
	r = Arduino.analogRead(pot_r_Pin) / 4
	Arduino.delay(1)
	g = Arduino.analogRead(pot_g_Pin) / 4
	Arduino.delay(1)
	b = Arduino.analogRead(pot_b_Pin) / 4
	Arduino.delay(1)
	return r, g, b

def colour_mixing():
	"""
	Call get_pots() and set 
	the colour pins accordingly
	"""
	r, g, b = get_pots()
	Arduino.analogWrite(redPin, r)
	Arduino.analogWrite(greenPin, g)
	Arduino.analogWrite(bluePin, b)
	return r, g, b

def set_colour(r, g, b):
	"""
	simple colour fade for R, G, B.
	Colours can be set indivdually or mixed automatically
	by calling the 'get' functions below.
	"""
	Arduino.analogWrite(redPin, r)
	Arduino.analogWrite(greenPin, g)
	Arduino.analogWrite(bluePin, b)

def get_r():
	r_val = Arduino.analogRead(pot_r_Pin) / 4
	Arduino.delay(1)
	return r_val

def get_g():
	g_val = Arduino.analogRead(pot_g_Pin) / 4
	Arduino.delay(1)
	return g_val

def get_b():
	b_val = Arduino.analogRead(pot_b_Pin) / 4
	Arduino.delay(1)
	return b_val

def close_pins():
	"""
	Close pins to quit cleanly (doesn't work with a 'for
	loop' despite the pins happily initialising that way!)
	"""
	Arduino.digitalWrite(redPin,Arduino.LOW)
	Arduino.digitalWrite(greenPin,Arduino.LOW)
	Arduino.digitalWrite(bluePin,Arduino.LOW)

def main():
	"""
	Mix the colours using three pots. 
	Ctrl+C cleans up the pins on exit.
	"""
	while True:
		try:
			colour_mixing()
			if debug:
				print "Red: {:d} | Green: {:d} | Blue: {:d}".format(r, g, b)

		except KeyboardInterrupt:
			close_pins()
			
close_pins()
