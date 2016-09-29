# Main program file

# Parse arguments
import argparse, sys, urllib, http.client

argParser = argparse.ArgumentParser()

# Options

# Required argument
argParser.add_argument("host", help="Host IP or address of the extender")

argParser.add_argument("-r", "--reboot",
	help = "reboot the extender",
	action = "store_true")


args = argParser.parse_args()

if args.reboot:
	print("Rebooting")