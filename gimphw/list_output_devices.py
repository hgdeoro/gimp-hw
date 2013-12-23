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


def get_output_device_id(device_name):
    """
    Return device id (int) for the given OUTPUT device.
    Returns None if not found

    Example:
        pygame.midi.init()
        get_device_id('VirMIDI 2-0')
        pygame.midi.quit()
    """
    for i in range(pygame.midi.get_count()):
        _, name, _, output, _ = pygame.midi.get_device_info(i)
        if output and name == device_name:
            return i
    return None


def main():
    pygame.midi.init()
    for i in range(pygame.midi.get_count()):
        _, name, _, output, _ = pygame.midi.get_device_info(i)

        if output:
            print i, "->", name
    pygame.midi.quit()

if __name__ == '__main__':
    main()
