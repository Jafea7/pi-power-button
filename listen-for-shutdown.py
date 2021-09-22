#!/usr/bin/env python3

import RPi.GPIO as GPIO
import subprocess
import time

def blink():
  """
  Lowers brightness of activity LED,
  blinks power led to heartbeat
  """
  with open('/sys/class/leds/led1/brightness', 'w') as pwr: print('1', file=pwr)
  with open('/sys/class/leds/led1/trigger', 'w') as hb: print('heartbeat', file=hb)
  with open('/sys/class/leds/led0/brightness', 'w') as act: print('0', file=act)
  with open('/sys/class/leds/led0/trigger', 'w') as trg: print('none', file=trg)
  time.sleep(3)

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(3, GPIO.FALLING)

blink()
subprocess.call(['shutdown', '-h', 'now'], shell=False)
