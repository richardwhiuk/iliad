import iliad.core.module

class Module(iliad.core.module.Module):
	
	def __init__(self, **args):

		iliad.core.module.Module.__init__(self, **args)

class Content:

	def __init__(self, id, title, body, format):
		self._id = id
		self._data = { 'title': title, 'body': body, 'format': format }
		self._pending = {}

	def __value(self, name, value=None):
		if(value):
			self._pending[name] = value
			self._data[name] = value
		return self._data[name]

	def id(self):
		return self._id

	def title(self, title=None):
		return self.__value('title', title)

	def body(self, body=None):
		return self.__value('body', body)

	def save(self):
		if len(self._pending) > 0:
			update = {}
			if 'title' in self._pending:
				update['title'] = ('s', self._pending['title'])
			if 'body' in self._pending:
				update['body'] = ('s', self._pending['body'])
			iliad.core.system.System.database.update(table='content', where=( '=', ('column','id'), ('u', self._id)), update=update)

def Get(id=None):
	if id != None:
		result = iliad.core.system.System.database.select(table='content', where=( '=', ('column', 'id'), ('u', id) ))
		return result.fetch(load)

def load(row):
	module = iliad.core.system.module(id=row['format'])
	return module.load('Content')

class Page:

	class Main:

		def __init__(self, resource):
			self._resource = resource
			arg = resource.get_argument()
			if arg == 'new':
				resource.pop_argument()
				self.new()
			elif arg == 'list':
				resource.pop_argument()
				self.list()
			else:
				try:
					self._content = Get(id=int(arg))
					resource.pop_argument()
				except ValueError:
					self.list()
					return
				
				arg = resource.get_argument()
				if arg == 'view':
					resource.pop_argument()
					self.view()
				elif arg == 'edit':
					resource.pop_argument()
					self.edit()
				elif arg == 'delete':
					resource.pop_argument()
					self.delete()
				else:
					self.view()

		def view(self):
			self._mode = 'view'

		def render(self, env):
			if self._mode == 'view':
				template = env.get_template('page/main/content/view.html')
				return (False, template.render(body=self._content.html()))

