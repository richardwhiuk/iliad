
class Request:
	def __init__(self):
		self.method = None
		self.path = None
		self.version = None
		self.headers = {}
		self.ip = None
		self.port = None
	def __str__(self):
		result = self.ip + ':' + str(self.port)
		result += "\r\n"
		result += self.method + ' ' + self.path + ' ' + self.version
		result += "\r\n"
		for k in self.headers.keys():
			result += k + '=>' + self.headers[k]
			result += "\r\n"
		return result

