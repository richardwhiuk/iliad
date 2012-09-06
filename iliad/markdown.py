from __future__ import absolute_import
import iliad.core.module
import iliad.content
import markdown as pymarkdown

class Module(iliad.core.module.Module):

	def __init__(self, **args):
	
		iliad.core.module.Module.__init__(self, **args)

converter = pymarkdown.Markdown().convert

class Content(iliad.content.Content):

	def html(self):
		return converter(self._body)

