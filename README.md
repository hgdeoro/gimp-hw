gimp-hw
=======

Control Gimp using Arduino


The glue is a simple python program (see gimphw/poll_py_arduino.py), which uses PyArduino
to read the Arduino values, and generates Midi events using PyGame.

Those events are sent to the Alsa (using device "VirMIDI 2-0"), and read by
Gimp using /dev/snd/midiC2D0 (the virtual midi device is created by the kernel
module named "snd-virmidi").


YouTube: [http://youtu.be/VhBr00d5uyo](http://youtu.be/VhBr00d5uyo)
