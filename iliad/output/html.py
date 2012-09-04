import iliad.core.module

class Module(iliad.core.module.Module):

	def __init__(self, **args):
	
		iliad.core.module.Module.__init__(self, **args)

class Page:

	def __init__(self, resource):
		self._resource = resource
		self._main = resource.logic().load('Page.Main')(resource)

	def display(self):
		return ""

class Output(iliad.core.output.Output):

	def __init__(self, **args):

		iliad.core.output.Output.__init__(self, **args)

	def logic(self, resource):

		return Page(resource)

	def render(self, result, response):

		response.headers["Content-type"] = "text/html; charset=utf-8"

		response.status = 200
		response.body = result 

