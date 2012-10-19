from __future__ import absolute_import
import iliad.core.module
import iliad.content
import markdown as pymarkdown

class Module(iliad.core.module.Module):

	def __init__(self, **args):
	
		iliad.core.module.Module.__init__(self, **args)
		iliad.content.register_format('markdown', Content, self.id(), 'Markdown')

converter = pymarkdown.Markdown().convert

class Content(iliad.content.Plain):

	def html(self):
		return converter(self._content.body())

