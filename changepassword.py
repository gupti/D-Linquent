'''
changepassword.py - Changes the extender's administrator password.
'''

import sys, urllib, http.client

# Default host does not work on Linux due to DNS shenanigans
host = ""
password = ""
header = {"Content-type" : "application/x-www-form-urlencoded"}

if len(sys.argv) > 2:
	host = sys.argv[1]
	password = sys.argv[2]
else:
	print("Too few parameters specified (2 required).")
	exit();

print("Changing admin password on " + host + " to " + password + "...", end="")

parameters = {"action" : "tools_admin", "admin_password_tmp" : password, "admin_password" : password, "admin_password1" : password}
connection = http.client.HTTPConnection(host)
form = urllib.parse.urlencode(parameters)

try:
	connection.request('POST', '', form, header)
	print(" done.");
	print("Will require a reboot to apply.")
except error:
	print("Error sending request.", end="")
