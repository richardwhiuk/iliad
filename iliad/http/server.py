import iliad.core.system
import preforkserver
import iliad.http.request
import iliad.http.response

import os
import re
import traceback

class Server(iliad.preforkserver.BaseChild):

	__http_request_first = re.compile('([A-Z]+) ([^ ]+) HTTP/([01].[901])$')
	__http_request_header = re.compile('([A-Za-z-]+):(.+)$')

	def initialize(self):
		self.debugLog = open('iliad-' + str(os.getpid())  + '.log', 'w')
		iliad.core.system.initalize(self.debug)

	def shutdown(self):
		iliad.core.system.shutdown()
		self.debugLog.close()

	def debug(self, entry):
		self.debugLog.write(str(entry) + '\r\n')

	def processRequest(self):
		try:
			self.data = ''
			lRequest = self.parse()
			self.debug(lRequest)
			if lRequest:
				lResponse = iliad.http.response.Response()
				try:
					iliad.core.system.process(lRequest, lResponse)
				except Exception as e:
					lResponse.status = 500
					lResponse.headers = {
						"Server": "Iliad",
						"Content-Type":"text/html; charset=UTF-8"
					}

					lResponse.body = "<!DOCTYPE html><html><head><title>Server Error</title></head><body><pre>" + traceback.format_exc(e) + "</pre></body></html>"

				self.respond(lResponse)
		except Exception as e:
			try:
				self.debug(traceback.format_exc(e))
			except Exception as e:
				print e

	def parse(self):

		lRequest = iliad.http.request.Request()

		lRequest.ip, lRequest.port = self.addr

		(First, Header, Done) = range(3)
		mode = First

		while mode != Done:

			additional = self.conn.recv(4096)
			if len(additional) == 0:
				return None
			self.data = self.data + additional

			start = 0
			end = 0
			search = 0
			while (mode != Done) and (search < (len(self.data) - 1)):
				end = self.data.find('\r\n', search)
				if end == -1:
					search = len(self.data) - 1
				elif mode == First:
					match = Server.__http_request_first.match(self.data[start:end])
					if match:
						search = end + 2
						start = end + 2
						lRequest.method = match.group(1)
						lRequest.path = match.group(2)
						lRequest.version = match.group(3)
						mode = Header
					else:
						raise Exception("Invalid iliad.http.request")
				elif mode == Header:
					if (end - start) == 0:
						mode = Done
						search = end + 2
						start = end + 2
					else:
						match = Server.__http_request_header.match(self.data[start:end])
						if match:
							search = end + 2
							start = end + 2
							key = match.group(1)
							if key in lRequest.headers:
								raise Exception("Duplicate header detected")
							lRequest.headers[key] = match.group(2)
						else:
							raise Exception("Invalid header")

			self.data = self.data[start:]

		return lRequest

	def respond(self, xiResponse):
		try:
			status = xiResponse.status
			reason = iliad.http.response.reason[status]
		except Exception as e:
			status = 500
			reason = iliad.http.response.reason[500]

		self.conn.send("HTTP/" + xiResponse.version + " " + str(status) + " " + reason + "\r\n")

		for (key, value) in xiResponse.headers.iteritems():
			self.conn.send(key + ": " + value + "\r\n")

		self.conn.send("\r\n")

		self.conn.send(xiResponse.body)

		self.conn.send("\r\n")

pass

