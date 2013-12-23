gimp-hw
=======

Control Gimp using Arduino

Midi
----------

The glue is a simple python program (see gimphw/poll_py_arduino.py), which uses PyArduino
to read the Arduino values, and generates Midi events using PyGame.

Those events are sent to the Alsa (using device "VirMIDI 2-0"), and read by
Gimp using /dev/snd/midiC2D0 (the virtual midi device is created by the kernel
module named "snd-virmidi").

Pros:
* well integrated to Gimp, since the shortcuts (configurable from Gimp) works well with the "active image" (ie: the image being edited)

Cons:
* requires to load a kernel module
* the MIDI layers loses information (ie: an analog read in arduino reads values from 0 to 1023, but the values sent using MIDI are from 0 to 127)

YouTube: [http://youtu.be/VhBr00d5uyo](http://youtu.be/VhBr00d5uyo)

PyRO
----------

The glue is a similar python program (see gimphw/poll_py_arduino_pyro.py), which uses PyArduino
to read the Arduino values, and communicate with Gimp using PyRO. To make this work,
the plugin at gimphw/pyro2gimp_plugin.py should be executed from Gimp.

Pros:
* avoids the MIDI layer
* posibility to use Gimp API directly

Cons:
* I have't found any way to get the active image: there is no way to know which of the images is the being edited. This makes imposible do basic things, like modify layers oppacity.
