'''
reboot.py - reboots the extender by replicating some data from the POST packet
that's sent when rebooting the extender from the web interface. Takes one argument
(the hostname or IP), defaulting to dlinkap.local. No password required! :D

Copyright (c) 2016 gupti

This software is provided 'as-is', without any express or implied
warranty. In no event will the authors be held liable for any damages
arising from the use of this software.

Permission is granted to anyone to use this software for any purpose,
including commercial applications, and to alter it and redistribute it
freely, subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must not
   claim that you wrote the original software. If you use this software
   in a product, an acknowledgement in the product documentation would be
   appreciated but is not required.
2. Altered source versions must be plainly marked as such, and must not be
   misrepresented as being the original software.
3. This notice may not be removed or altered from any source distribution.
'''

import sys, urllib, http.client

# Default host does not work on Linux due to DNS shenanigans
host = "dlinkap.local"
parameters = {"action" : "reboot_needed"}
header = {"Content-type" : "application/x-www-form-urlencoded"}

if len(sys.argv) > 1:
	host = sys.argv[1]

print("Sending reboot packet to " + host + "...", end="")

connection = http.client.HTTPConnection(host)
form = urllib.parse.urlencode(parameters)

try:
	connection.request('POST', '', form, header)
	print(" done.");
except error:
	print("Error sending request.", end="")
