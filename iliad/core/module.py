import iliad.core.system

import sys

def Get(active=None):
	result = iliad.core.system.System.database.select(table='module', where=( '=', ('column', 'active'), ('u', active) ))
			
	return result.fetchall(Create)

def load(path, additional = ''):
	base = __import__(path)
	paths = (path.split('.'))[1:]
	if len(additional) > 0:
		paths += additional.split('.')
	for path in paths:
		base = getattr(base, path)
	return base

def Create(row):
	return load(row['path']).Module

class Module:

	def __init__(self, id, name, version, active, path):
		self._path = path
		self._id = id
		self._name = name

	def id(self):
		return self._id

	def name(self):
		return self._name

	def load(self, section):
		return load(self._path, section)

