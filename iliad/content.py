import iliad.core.module
import iliad.form
import cgi

class Module(iliad.core.module.Module):
	
	def __init__(self, **args):
		iliad.core.module.Module.__init__(self, **args)
		register_format('plain', Plain, self.id(), 'Plain')

content = {}

def get_format_id(module, format, **args):
	return str(module) + '/' + format

def register_format(format, implementation, module, description):
	lId = get_format_id(**{'module': module, 'format': format})
	registration = { 'implementation': implementation, 'module': module, 'id': lId, 'module': module, 'format': format, 'description': description }
	content[lId] = registration
	return registration

class Plain:
	
	def __init__(self, content):
		self._content = content

	def html(self):
		return cgi.escape(self._content.body())

class Content:

	def __init__(self, id=None, title=None, body=None, format=None, module=None):
		self._pending = {}
		if id == None:
			self._new = True
			for k in content:
				if content[k]['format'] == 'plain' and content[k]['implementation'] == Plain:
					plain = k
			self._data = { 'title': '', 'body': '', 'format': 'plain', 'module': content[k]['module']}
			self._implementation = Plain(self)
		else:
			self._new = False
			self._id = id
			self._data = { 'title': title, 'body': body, 'format': format, 'module': module }
			self._implementation = content[get_format_id(**self._data)]['implementation'](self)

	def __value(self, name, value=None):
		if(value):
			self._pending[name] = value
			self._data[name] = value
		return self._data[name]

	def html(self):
		return self._implementation.html()

	def id(self):
		return self._id

	def title(self, title=None):
		return self.__value('title', title)

	def body(self, body=None):
		return self.__value('body', body)

	def format_id(self, format_id=None):
		if format_id:
			(module, format) = format_id.split('/', 2)
			self.__value('module', module)
			self.__value('format', format)
			self._implementation = content[format_id]['implementation'](self)
			return format_id
		else:
			return str(self.__value('module', None)) + '/' + self.__value('format', None)

	def save(self):
		update = {}
		for key in ['title','body','format']:
			if key in self._pending:
				update[key] = ('s', self._pending[key])
		if 'module' in self._pending:
			update['module'] = ('u', self._pending['module'])
		if self._new:
			result = iliad.core.system.System.database.insert(table='content', insert=update)
			self._id = result.new_id()
		else:
			if len(update) > 0:
				iliad.core.system.System.database.update(table='content', where=( '=', ('column','id'), ('u', self._id)), update=update)
		self._pending = {}

def Get(id=None):
	if id != None:
		result = iliad.core.system.System.database.select(table='content', where=( '=', ('column', 'id'), ('u', id) ))
		return result.fetch(load)
	else:
		result = iliad.core.system.System.database.select(table='content')
		return result.fetchall(load)

def load(row):
	return Content

class Page:

	class Main:

		def __init__(self, resource, prefix, data):
			self._submit = None
			self._redirect = None
			self._resource = resource
			arg = resource.get_argument()
			if arg == 'new' or arg == 'add':
				resource.pop_argument()
				self.new(prefix + '/new', data('new'))
			elif arg == 'list':
				resource.pop_argument()
				self.list()
			elif arg:
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
					self.edit(prefix + '/' + str(self._content.id()) + '/edit', data(str(self._content.id()))('edit'))
				elif arg == 'delete':
					resource.pop_argument()
					self.delete()
				else:
					self.view()
			else:
				self.list()

		def save(self):
			self._submit = 'Save'

		def save_continue(self):
			self._submit = 'Save Continue'

		def preview(self):
			self._submit = 'Preview'
			self._preview = True

		def view(self):
			self._mode = 'view'

		def new(self, xiPrefix, xiData):
			self._mode = 'new'
			self._content = Content()
			self._update(xiPrefix, xiData)

		def edit(self, xiPrefix, xiData):
			self._mode = 'edit'
			self._update(xiPrefix, xiData)

		def _update(self, xiPrefix, xiData):
			self._preview = False

			lFormatValues = {}

			for (id, format) in content.iteritems():
				lFormatValues[id] = format['description']

			self._form = iliad.form.Form(
				prefix=xiPrefix,
				action=self._resource.url(),
				fields=[
					{ 'name': 'title', 'label': 'Title', 'type': 'iliad.form.text', 'value': self._content.title },
					{ 'name': 'format', 'label': 'Format', 'type': 'iliad.form.select', 'values': lFormatValues, 'value': self._content.format_id},
					{ 'name': 'body', 'label': 'Body', 'type': 'iliad.form.textarea', 'value': self._content.body },
					{ 'name': 'preview', 'label': 'Preview', 'type': 'iliad.form.submit', 'value': self.preview },
					{ 'name': 'save-continue', 'label': 'Save and Continue', 'type': 'iliad.form.submit', 'value': self.save_continue },
					{ 'name': 'save', 'label': 'Save', 'type': 'iliad.form.submit', 'value': self.save }
				],
				data=xiData
			)

			if self._submit:
				if self._submit == 'Save' or self._submit == 'Save Continue':
					self._content.save()
				if self._submit == 'Save':
					self._redirect = self._resource.url(argument=str(self._content.id()) + '/view')
				elif self._submit == 'Save Continue':
					self._redirect = self._resource.url(argument=str(self._content.id()) + '/edit')

		def list(self):
			self._mode = 'list'
			self._content = Get()

		def render(self, env):
			if self._mode == 'view':
				template = env.get_template('page/main/content/view.html')
				return (False, template.render(body=self._content.html()))
			elif self._mode == 'edit' or self._mode == 'new':
				if self._redirect:
					return (True, self._redirect)
				else:
					template = env.get_template('page/main/content/' + self._mode + '.html')
					form = self._form.render(env)
					if form[0]:
						return form
					return (False, template.render(form=form[1], preview=self._preview, body=self._content.html()))
			elif self._mode == 'list':
				template = env.get_template('page/main/content/list.html')
				content = []
				for entry in self._content:
					content.append({'title': entry.title(), 'url': self._resource.url(argument=str(entry.id()) + '/view')})
				return (False, template.render(content=content))

