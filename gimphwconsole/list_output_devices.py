'''
Created on Dec 22, 2013

@author: Horacio G. de Oro
'''
import pygame
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
