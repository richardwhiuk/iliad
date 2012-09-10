import iliad.core.resource
import iliad.core.database
import iliad.core.site
import iliad.core.module

class System:
	output = None

class Data:
	def __init__(self, data = None, value = None):
		self._ = {}
		self._v = value
		if data:
			for k in data:
				self._add(k, data[k])

	def _add(self, k, v):
		ks = k.split('/', 1)
		if len(ks) > 1:
			if ks[0] in self._:
				self._[ks[0]]._add(ks[1], v)
			else:
				self._[ks[0]] = Data({ks[1]: v})
		else:
			self._[k] = Data(value=v)

	def value(self):
		return self._v

	def __call__(self, k):
		if k in self._:
			return self._[k]
		else:
			return Data()

	def __str__(self):
		result = "{"
		for k in self._:
			result += k + '->' + str(self._[k]) + ","
		result += "}"
		if self._v:
			result += ':' + self._v
		return result

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
		logic = output.logic(resource=resource, data=Data(request.data))

		result = logic.display()

		output.render(result, response)
	
		return response

	response.status = 404

	return response

def shutdown():
	pass

