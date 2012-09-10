import string

import iliad.core.system
import iliad.core.output

class Resource:

	def __init__(self, id, path, base, additional, logic, output):
		self._id = id
		self._path = path
		self._output = output
		self._logic = logic
		self._base = base
		self._additional = additional
		self._arguments = None
		self._argument = None

	def id(self):
		return self._id

	def get_argument(self):
		if not self._arguments:
			self._arguments = []
			if len(self._base) > 0:
				self._arguments += self._base.strip('/').split('/')
			if self._argument:
				self._arguments += self._argument.strip('/').split('/')
			elif len(self._additional) > 0:
				self._arguments += self._additional.strip('/').split('/')
		if len(self._arguments) > 0:
			return self._arguments[0]
		return None

	def argument(self, argument):
		if self._arguments:
			raise Exception("Arguments already defined.")
		else:
			argument = argument.strip('/')
			if argument != self._additional and len(argument) > 0:
				self._argument = argument

	def pop_argument(self):
		self._arguments.pop(0)

	def logic(self):
		return iliad.core.system.module(id=self._logic)

	def output(self):
		return iliad.core.system.module(id=self._output)

def Get(paths=None, path=None, argument=None, base=None, logic=None, output=None):
	if paths != None:
		resources = []
		for path in paths:
			resources += Get(path=path)
		return resources
	elif (path != None or base != None) and argument != None:
		where = ('AND', [])
		if path != None:
			where[1].append(  ('=', ('column', 'path'), ('s', path) ) )
		if base != None:
			where[1].append(  ('=', ('column', 'base'), ('s', base) ) )
		if logic != None:
			where[1].append( ('=', ('column', 'logic'), ('u', logic) ) )
		if output != None:
			where[1].append( ('=', ('column', 'output'), ('u', output) ) )

		result = iliad.core.system.System.database.select(table='resource', where=where, order=('priority', False) )

		resources = result.fetchall(lambda x: Resource)

		if len(argument) > 0:
			for resource in resources:
				resource.argument(argument)

		return resources

	elif argument != None:
		path = argument.strip('/')
		parts = string.split(path, '/')
		arguments = [ (argument, '')]
		resources = []

		for i in range(1, len(parts) + 1):
			arguments.append( ( '/'.join(parts[:-i]) , '/'.join(parts[-i:]) ) )

		for (base, additional) in arguments:
			resources += Get(base=base, argument=additional, logic=logic, output=output)

		return resources

	elif path != None:
		path = path.strip('/')
		parts = string.split(path, '/')
		paths = [ (path, '')]
		resources = []
	
		for i in range(1, len(parts) + 1):
			paths.append( ( '/'.join(parts[:-i]) , '/'.join(parts[-i:]) ) )

		for (path, argument) in paths:
			resources += Get(path=path, argument=argument, logic=logic, output=output)

		return resources

