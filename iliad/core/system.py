import iliad.core.resource
import iliad.core.database
import iliad.core.site
import iliad.core.module

class System:
	output = None

def initalize(output):
	iliad.core.system.System.output = output
	iliad.core.system.System.database = iliad.core.database.Database.Load()
	iliad.core.system.System.site = iliad.core.site.Site.Load()
	iliad.core.system.System.modules = iliad.core.module.Get(active=True)

def module(name=None, id=None):
	for module in iliad.core.system.System.modules:
		if module.id() == id:
			return module
	return None

def output(entity):
	iliad.core.system.System.output(entity)

def process(request, response):

	response.headers["Server"] = "Iliad"
	
	if len(request.path.strip('/')) == 0:
		path = 'home'
	else:
		path = request.path.strip('/')

	resources = iliad.core.resource.Get(paths=[path, 'error'])

	System.output(resources)

	for resource in resources:

		output = iliad.core.output.Get(module=resource.output())
		logic = output.logic(resource)

		result = logic.display()

		output.render(result, response)
	
		return response

	response.status = 404

	return response

def shutdown():
	pass

