import string

import iliad.core.system
import iliad.core.output

class Resource:

	def __init__(self, id, path, base, additional, logic, output):
		self._output = output
		self._logic = logic
		self._base = base
		self._additional = additional
		self._arguments = None

	def get_argument(self):
		if not self._arguments:
			self._arguments = []
			if len(self._base) > 0:
				self._arguments += self._base.strip('/').split('/')
			if len(self._additional) > 0:
				self._arguments += self._additional.strip('/').split('/')
		return self._arguments[0]

	def pop_argument(self):
		self._arguments.pop(0)

	def logic(self):
		return iliad.core.system.module(id=self._logic)

	def output(self):
		return iliad.core.system.module(id=self._output)

def Get(paths=None, path=None, argument=None):
	if paths != None:
		resources = []
		for path in paths:
			resources += Get(path=path)
		return resources
	elif path != None and argument != None:
		result = iliad.core.system.System.database.select(table='resource', where=( '=', ('column', 'path'), ('s', path) ), order=('priority', False) )
			
		resources = result.fetchall(lambda x: Resource)

		if len(argument) > 0:
			for resource in resources:
				resource.additional = argument
		
		return resources
		
	elif path != None:
		path = path.strip('/')
		parts = string.split(path, '/')

		paths = [ (path, '')]
	
		for i in range(1, len(parts) + 1):
				
			paths.append( ( '/'.join(parts[:-i]) , '/'.join(parts[-i:]) ) )

		resources = []

		for (path, argument) in paths:

			resources += Get(path=path, argument=argument)

		return resources

