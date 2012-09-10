import MySQLdb
import iliad.core.system

class Update:
	def __init__(self, cursor):
		self.__cursor = cursor

class Select:
	def __init__(self, cursor):
		self.__cursor = cursor

	def fetch(self,classl):
		row = self.__cursor.fetchone()
		if row:
			return classl(row)(**row)

	def fetchall(self, classl):
		result = []
		rows = self.__cursor.fetchall()
		for row in rows:
			result.append(classl(row)(**row))
		return result

class Database:

	@staticmethod
	def Load(url):
		return Database(url.username, url.password, url.path.strip('/'), url.hostname, url.port)

	def __init__(self, username, password, database, host, port):
		self.db = MySQLdb.connect(host=host, user=username, passwd=password, db=database, port=port)

	def select(self, table, where = None, order = None):
		stmt = "SELECT * FROM `%s`" % table
		params = []

		if where:
			wresult = _where(where)
			stmt += " WHERE " + wresult[0]
			params += wresult[1]
		
		cursor = self.db.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute(stmt, params)
		
		return Select(cursor)

	def update(self, table, update, where = None ):
		stmt = "UPDATE `%s` SET " % table
		params = []

		ustmt = []
		for k in update:
			cond = _wcond(update[k])
			ustmt.append( ("`%s` = " % k) + cond[0] )
			params += cond[1]

		stmt += ', '.join(ustmt)

		if where:
			wresult = _where(where)
			stmt += " WHERE " + wresult[0]
			params += wresult[1]
		
		cursor = self.db.cursor()
		cursor.execute(stmt, params)
		
		return Update(cursor)

def _where(where):

	if where[0] == '=':
		condl = _wcond(where[1])
		condr = _wcond(where[2])
		return (condl[0] + " = " + condr[0], condl[1] + condr[1])

def _wcond(condition):

	if condition[0] == 'column':
		return ('`%s`' % condition[1], [])
	else:
		return ('%s', [condition[1]])	

