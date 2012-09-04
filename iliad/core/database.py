import urlparse
import os


class Database:

	@staticmethod
	def Load():
		if len(os.environ['ILIAD_DATABASE']) == 0:
			raise "No database defined"
		else:
			dsn = urlparse.urlparse(os.environ['ILIAD_DATABASE'])
			module = dsn.scheme + '.database'
			mdb = load(module,'Database')
			return mdb.Load(dsn)

def load(path, additional = ''):
	base = __import__(path)
	paths = (path.split('.'))[1:]
	if len(additional) > 0:
		paths += additional.split('.')
	for path in paths:
		base = getattr(base, path)
	return base


