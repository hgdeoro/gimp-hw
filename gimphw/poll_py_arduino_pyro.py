# -*- coding: utf-8 -*-

#
# WARNING: this is just a prototype, a proof of concept
#  made to test different options to integrate Arduino to Gimp.
#
# This code laks tests, and no effort of any kind was made
# to create robust, good quality, maintainable code!
#
# You have been averted :-D
#

from py_arduino.arduino import PyArduino
from pyro2gimp_client import get_pyro3_proxy

CHURCH_ORGAN = 19

NOTE_0 = 0
NOTE_1 = 1

arduino_dev = '/dev/ttyACM0'
threshold = 2


def main():

    proxy = get_pyro3_proxy()

    print "Connecting to Arduino using", arduino_dev
    arduino = PyArduino()
    arduino.connect(arduino_dev, 9600)

    arduino.ping()
    print " + ping(): OK"

    last_a0 = arduino.analogRead(0)
    last_a1 = arduino.analogRead(1)

    print "Entering loop()..."
    while True:
        a0 = arduino.analogRead(0)
        a1 = arduino.analogRead(1)

        if abs(a0 - last_a0) >= threshold:
            last_a0 = a0
            print "a0 ->", a0
            proxy.set_layer_opacity(a0)

        if abs(a1 - last_a1) >= threshold:
            last_a1 = a1
            print "a1 ->", a1
            proxy.set_paintbrush_opacity(a1)

if __name__ == '__main__':
    main()
