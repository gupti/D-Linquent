# Parse arguments
import argparse

argParser = argparse.ArgumentParser()

# Options
argParser.add_argument("-r", "--reboot",
	help = "reboot the extender",
	action = "store_true")

args = argParser.parse_args()

if args.reboot:
	print("Rebootin'")