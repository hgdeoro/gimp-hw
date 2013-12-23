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

import hmac

from gimpfu import register, main, gimp, pdb  #@UnresolvedImport


def start_pyro4_server(*args, **kwargs):
    try:
        import Pyro4  #@UnresolvedImport

    except ImportError:
        print "ERROR: couldn't import 'Pyro4'"
        raise
    Pyro4.config.HMAC_KEY = hmac.new('gimp').digest()
    Pyro4.config.SOCK_REUSE = True

    print "Launching Pyro4 server..."
    Pyro4.Daemon.serveSimple(
        {
            gimp: "gimp",
            pdb: "pdb",
        },
        host="localhost", port=16319, ns=False)


def start_pyro3_server(*args, **kwargs):
    try:
        import Pyro  #@UnresolvedImport
        import Pyro.core  #@UnresolvedImport
    except ImportError:
        print "ERROR: couldn't import 'Pyro'"
        raise

    class Pyro3Server(Pyro.core.ObjBase):
        def __init__(self):
            Pyro.core.ObjBase.__init__(self)

        def set_layer_opacity(self, opacity):
            print "Setting layer opacity to {}".format(opacity)
            try:
                image = gimp.image_list()[0]
                layer = pdb.gimp_image_get_active_layer(image)
                value = opacity / float(10.0)
                if value > 100.0:
                    layer.opacity = 100.0
                else:
                    layer.opacity = value
            except:
                print "ERROR"

        def set_paintbrush_opacity(self, opacity):
            print "Setting paintbrush opacity to {}".format(opacity)

    print "Instantiating server..."
    remote_gimp = Pyro3Server()

    # Bypass NS
    # proxy = Pyro.core.getProxyForURI('PYROLOC://hostname:port/objectname')
    print "Pyro.core.initServer()..."
    Pyro.core.initServer()
    print "Instantiating daemon..."
    daemon = Pyro.core.Daemon(host="localhost", port=16319)
    daemon.connect(remote_gimp, 'remote_gimp')
    print "Entering loop..."
    daemon.requestLoop()

# This is the plugin registration function
# I have written each of its parameters on a different line
register(# @UndefinedVariable
    "pyro2gimp",
    "Launches a PyRO server",
    "Launches a PyRO (Python Remote Objects) server to access Gimp internals",
    "Horacio G. de Oro",
    "Horacio G. de Oro",
    "December 2013",
    "<Image>/Filters/Python-Fu/PyRO Server",
    "*",
    [],
    [],
    start_pyro3_server,
    )

main()  # @UndefinedVariable
