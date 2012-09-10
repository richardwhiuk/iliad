import iliad.core.module
import iliad.form

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
			self._pending = {}

def Get(id=None):
	if id != None:
		result = iliad.core.system.System.database.select(table='content', where=( '=', ('column', 'id'), ('u', id) ))
		return result.fetch(load)
	else:
		result = iliad.core.system.System.database.select(table='content')
		return result.fetchall(load)

def load(row):
	module = iliad.core.system.module(id=row['format'])
	return module.load('Content')

class Page:

	class Main:

		def __init__(self, resource, prefix, data):
			self._submit = None
			self._redirect = None
			self._resource = resource
			arg = resource.get_argument()
			if arg == 'new':
				resource.pop_argument()
				self.new()
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

		def edit(self, xiPrefix, xiData):
			self._mode = 'edit'
			self._preview = False

			self._form = iliad.form.Form(
				prefix=xiPrefix,
				action=self._resource.url(),
				fields=[
					{ 'name': 'title', 'label': 'Title', 'type': 'iliad.form.text', 'value': self._content.title },
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
			elif self._mode == 'edit':
				if self._redirect:
					return (True, self._redirect)
				else:
					template = env.get_template('page/main/content/edit.html')
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

