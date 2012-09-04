import iliad.core.module

class Module(iliad.core.module.Module):
	
	def __init__(self, **args):

		iliad.core.module.Module.__init__(self, **args)

class Content:

	def __init__(self, id, content):
		pass

def Get(id=None):
	if id != None:
		result = iliad.core.system.System.database.select(table='content', where=( '=', ('column', 'id'), ('u', id) ))


		return result.fetch(lambda x: Content)

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

