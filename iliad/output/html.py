import iliad.core.module
import iliad.content
import jinja2

class Module(iliad.core.module.Module):

	def __init__(self, **args):
		iliad.core.module.Module.__init__(self, **args)
		iliad.content.register_format('html', Content, self.id(), 'HTML')

class Page:

	def __init__(self, xiResource, xiPrefix, xiData):
		self._resource = xiResource
		self._main = xiResource.logic().load('Page.Main')(xiResource, xiPrefix + '/' + str(xiResource.id()), xiData(str(xiResource.id())))

	def display(self):
		env = jinja2.Environment(loader=jinja2.PackageLoader('iliad.output.html','templates'))
		template = env.get_template('page/main.html')
		main = self._main.render(env)
		if main[0]:
			return main
		return (False, template.render(main=main[1]))

class Content(iliad.content.Plain):

	def html(self):
		return self._content.body()

class Output(iliad.core.output.Output):

	def __init__(self, **args):

		iliad.core.output.Output.__init__(self, **args)

	def logic(self, resource, data, prefix=None):

		if prefix:
			prefix += '/page'
		else:
			prefix = 'page'

		return Page(resource,prefix,data('page'))

	def render(self, result, response):

		if result[0]:
			response.headers["Location"] = result[1]
			response.status = 303
		else:
			response.headers["Content-type"] = "text/html; charset=utf-8"
			response.status = 200
			response.body = result[1] 

