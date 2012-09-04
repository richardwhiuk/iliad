
reason = {
	100: "Continue",
	200: "OK",
	404: "Not Found",
	500: "Internal Server Error"
}

class Response:

	def __init__(self):
		self.version = "1.0"
		self.status = 500
		self.body = ""
		self.headers = {}

