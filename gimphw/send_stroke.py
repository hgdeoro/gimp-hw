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

import pygame.midi
import time

from gimphw.list_output_devices import get_output_device_id


CHURCH_ORGAN = 19

NOTE = 0


def main():
    print "Init()"
    pygame.midi.init()

    print "get_output_device_id()"
    device_id = get_output_device_id('VirMIDI 2-0')
    assert device_id is not None
    print " + device:", device_id

    print "Output()"
    midi_out = pygame.midi.Output(device_id, 0)
    print "set_instrument()"
    midi_out.set_instrument(CHURCH_ORGAN)
    # mouse_note, velocity, __, __  = regions.get_at(e.pos)

    print "Waiting 2 secs..."
    time.sleep(2)

    for velocity in (0, 25, 50, 75, 100, 127):
        print "note_on()"
        midi_out.note_on(NOTE, velocity)
    
        print "note_off()"
        midi_out.note_off(NOTE)

        time.sleep(1)

if __name__ == '__main__':
    main()
