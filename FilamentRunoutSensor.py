# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import RPi.GPIO as GPIO
import octoprint.plugin


class FilamoutRunoutSensorSetup(octoprint.plugin.StartupPlugin):
	def on_after_startup(self):
		# We're using the pin the GPIO number, not pin number
		GPIO.setmode(GPIO.BCM)  
		  
		# GPIO 17 set up as inputs, pulled up to avoid false detection.  
		# Wired to connect to GND on button press. Active Low
		GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
		  
		# callback function triggered on interrupt
		def FilamentRunoutCallbackFunc(channel):
			# TODO: Pause print job here if running
		    self._logger.info("falling edge detected on 17")
		  
		# when a falling edge is detected on port 17, define the what should be done
		GPIO.add_event_detect(17, GPIO.FALLING, callback=FilamentRunoutCallbackFunc, bouncetime=300)    		



__plugin_name__ = "FilamentRunoutSensor"
__plugin_version__ = "1.0.0"
__plugin_description__ = "Pauses the current print job when it detects a GPIO pin going low"
__plugin_pythoncompat__ = ">=2.7,<4"#!/usr/bin/env python2.7
__plugin_implementation__ = FilamoutRunoutSensorSetup()
