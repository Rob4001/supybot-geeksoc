###
# Copyright (c) 2012, Andrew Smillie
# All rights reserved.
#
#
###

import supybot.conf as conf
import supybot.registry as registry

def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified himself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('GeekSoc', True)


GeekSoc = conf.registerPlugin('GeekSoc')
# This is where your configuration variables (if any) should go.  For example:
conf.registerGlobalValue(GeekSoc, 'url',registry.String("api.gas.geeksoc.org", """This is the URL of the API"""))
conf.registerGlobalValue(GeekSoc, 'protocol',registry.String("http", """This is the protocol of the API"""))
conf.registerGlobalValue(GeekSoc, 'user',registry.String("admin", """This is the User of the API"""))
conf.registerGlobalValue(GeekSoc, 'password',registry.String("geeksoc", """This is the Password of the User"""))


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
