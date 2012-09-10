import iliad.core.module

class Module(iliad.core.module.Module):
	
	def __init__(self, **args):

		iliad.core.module.Module.__init__(self, **args)

class Form:

	def __init__(self, prefix, action, fields, data):

		self._prefix = prefix
		self._action = action
		self._fields = []
		self._method = "POST"

		for field in fields:
			self._fields.append(create_field(id=prefix + '/' + field['name'],data=data(field['name']),**field))

	def valid(self):
		return True

	def render(self, env):
		template = env.get_template('form/main.html')
		fields = []
		for field in self._fields:
			frender = field.render(env)
			if frender[0]:
				return frender
			fields.append(frender[1])
		return (False, template.render(action=self._action,method=self._method,fields=fields))

def create_field(type, **args):
	base = __import__(type)
	paths = (type.split('.'))[1:]
	for path in paths:
		base = getattr(base, path)
	base = getattr(base, 'Field')
	return base(type=type, **args)

class Field:

	def __init__(self, type, id, name, **args):
		self._name = name
		self._id = id
		self._type = type


