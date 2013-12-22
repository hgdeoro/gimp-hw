'''
Created on Dec 22, 2013

@author: Horacio G. de Oro
'''
import pygame.midi

from gimphw.list_output_devices import get_output_device_id
from py_arduino.arduino import PyArduino


CHURCH_ORGAN = 19

NOTE_0 = 0
NOTE_1 = 1

arduino_dev = '/dev/ttyACM0'
threshold = 2


def map_1024_to_midi(value):
    assert value >= 0
    assert value <= 1023
    value = value / 5
    if value > 127:
        return 127
    return value


def main():

    print "Connecting to Arduino using", arduino_dev
    arduino = PyArduino()
    arduino.connect(arduino_dev, 9600)

    arduino.ping()
    print " + ping(): OK"

    print "midi.init()"
    pygame.midi.init()

    print "get_output_device_id()"
    device_id = get_output_device_id('VirMIDI 2-0')
    #
    # In console, run:
    #    $ sudo modprobe snd-virmidi
    #
    assert device_id is not None
    print " + device:", device_id

    print "midi.Output()"
    midi_out = pygame.midi.Output(device_id, 0)
    print "midi_out.set_instrument()"
    midi_out.set_instrument(CHURCH_ORGAN)

    last_a0 = arduino.analogRead(0)
    last_a1 = arduino.analogRead(1)

    print "Entering loop()..."
    while True:
        a0 = arduino.analogRead(0)
        a1 = arduino.analogRead(1)

        if abs(a0 - last_a0) >= threshold:
            midi_out.note_on(NOTE_0, map_1024_to_midi(a0))
            last_a0 = a0
            print "a0 ->", a0
            midi_out.note_off(NOTE_0)

        if abs(a1 - last_a1) >= threshold:
            midi_out.note_on(NOTE_1, map_1024_to_midi(a1))
            last_a1 = a1
            print "a1 ->", a1
            midi_out.note_off(NOTE_1)

if __name__ == '__main__':
    main()
