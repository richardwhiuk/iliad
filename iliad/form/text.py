import iliad.form

class Field(iliad.form.Field):

	def __init__(self, data, value, label, **args):
		self._value = value
		self._label = label
		if data.value():
			self._value(data.value())
		iliad.form.Field.__init__(self, label=label, value=value, **args)

	def render(self, env):
		template = env.get_template('form/text.html')
		return (False, template.render(id=self._id, value=self._value(), label=self._label))

