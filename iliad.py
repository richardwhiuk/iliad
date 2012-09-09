#!/usr/bin/python

# Iliad Internet Server

import sys
import iliad.manager
import iliad.http.server

def main(args):
	http = None

	if 'http' in args:
		http = iliad.manager.Manager(iliad.http.server.Server, port=8080, bindIp='0.0.0.0')
		http.run()

	if http:
		http.wait()

if __name__ == "__main__":
	sys.exit(main(sys.argv))

