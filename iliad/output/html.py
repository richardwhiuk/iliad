import iliad.core.module
import iliad.content
import jinja2

class Module(iliad.core.module.Module):

	def __init__(self, **args):
	
		iliad.core.module.Module.__init__(self, **args)

class Page:

	def __init__(self, resource):
		self._resource = resource
		self._main = resource.logic().load('Page.Main')(resource)

	def display(self):
		env = jinja2.Environment(loader=jinja2.PackageLoader('iliad.output.html','templates'))
		template = env.get_template('page/main.html')
		main = self._main.render(env)
		return template.render(main=main)

class Content(iliad.content.Content):

	def html(self):
		return self._body


class Output(iliad.core.output.Output):

	def __init__(self, **args):

		iliad.core.output.Output.__init__(self, **args)

	def logic(self, resource):

		return Page(resource)

	def render(self, result, response):

		response.headers["Content-type"] = "text/html; charset=utf-8"

		response.status = 200
		response.body = result 

