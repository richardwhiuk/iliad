#!/usr/bin/python

# Iliad Internet Server

import sys
import iliad.manager
import iliad.http.server

def main(args):
	manager = iliad.manager.Manager(iliad.http.server.Server, port=8080, bindIp='0.0.0.0')
	manager.run()

if __name__ == "__main__":
	sys.exit(main(sys.argv))

