import preforkserver
import os

class Manager(preforkserver.Manager):
	def preBind(self):
		pass

	def run(self):
		pid = os.fork()
		if pid:
			self.__pid = pid
		else:
			preforkserver.Manager.run(self)
			os._exit(0)

	def wait(self):
		os.waitpid(self.__pid, 0)

