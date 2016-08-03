'''
changepassword.py - Takes two arguments, the host and a new password.
Changes the extender's administrator password.

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
