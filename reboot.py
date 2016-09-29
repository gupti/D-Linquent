'''
reboot.py - reboots the extender by replicating some data from the POST packet
that's sent when rebooting the extender from the web interface. Takes one argument
(the hostname or IP), defaulting to dlinkap.local. No password required! :D
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
