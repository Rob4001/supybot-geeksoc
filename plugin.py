###
# Copyright (c) 2012, Andrew Smillie
# All rights reserved.
#
#
###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import supybot.conf as conf
import time as epoch
import os, sys, requests


class GeekSoc(callbacks.Plugin):
    """Add the help for "@plugin help GeekSoc" here
    This should describe *how* to use this plugin."""
    threaded = True
    
    def __init__(self, irc):
        super(GeekSoc, self).__init__(irc)
    
    def userinfo(self, irc, msg, args, name):
		"""<username>

		Return information on a given username.
		"""
		user = name
		day = int(epoch.time()/(60*60*24))
		api_url = self.registryValue('protocol')+"://"+self.registryValue('user')+":"+self.registryValue('password')+"@"+self.registryValue('url')
		r=requests.get(api_url+"/users/"+user )
		entry = r.json()  
		if 'error' in entry:
			irc.reply(("Error: "+entry['error']).encode('utf-8'))
			return
		name = entry['displayname']
		email = entry['email']
		studentNo = entry['studentnumber'] if 'studentnumber' in entry else "N/A"
		expiry = entry['expiry'] if 'expiry' in entry else "999999"
		paid = entry['paid'] if 'paid' in entry else "N/A"
		
		
		groups = ""
		for group in entry['groups']:
			groups = groups + group +", "
		
		groups = groups[:-2]
    
		status = "Active"
		if (paid == False):
			status = "Active (Not Paid)"
		# if int(expiry) <= day+60:
			# status = "Expiring (in %s days)" % (int(expiry)-day)
		# if int(expiry) <= day:
			# status = "Expired (%s days ago)" % (day-int(expiry))
		if entry['isAdmin'] == True:
			status = "Admin"
        
		string = ( "User: %s, Name: %s, Email: %s, Student Number: %s, Status: %s, Expires: %s" % (user, name, email, studentNo, status, expiry) )
		irc.reply(string.encode('utf-8'))
		irc.reply(("Groups: "+groups).encode('utf-8'))

    userinfo = wrap(userinfo, ['text'])


    def group(self, irc, msg, args, name):
		"""<group>
		 
		 Return information on a given group.
		"""
		group = name
		api_url = self.registryValue('protocol')+"://"+self.registryValue('user')+":"+self.registryValue('password')+"@"+self.registryValue('url')
		r=requests.get(api_url+"/groups/"+group )
		entry = r.json()  
		if 'error' in entry:
			irc.reply(("Error: "+entry['error']).encode('utf-8'))
			return
		name = entry['name']
		
		members = ""
		for member in entry['members']:
			members = members + member +", "
		
		members = members[:-2]
		
		irc.reply(("Name: "+name+" Members: "+members).encode('utf-8'))

    group = wrap(group, ['text'])


Class = GeekSoc


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
