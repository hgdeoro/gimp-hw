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

#
# Based on script from Frédéric Jaume:
# http://www.exp-media.com/content/extending-gimp-python-python-fu-plugins-part-2
#

def get_pyro3_proxy():
    try:
        import Pyro  #@UnresolvedImport
        import Pyro.core  #@UnresolvedImport
    except ImportError:
        print "ERROR: couldn't import 'Pyro'"
        raise

    print "Pyro.core.initClient()..."
    Pyro.core.initClient()

    print "Instantiating daemon..."
    # Bypass NS
    # proxy = Pyro.core.getProxyForURI('PYROLOC://hostname:port/objectname')
    remote_gimp = Pyro.core.getProxyForURI('PYROLOC://localhost:16319/remote_gimp')
    return remote_gimp
