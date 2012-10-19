import iliad.form

class Field(iliad.form.Field):

	def __init__(self, data, values, value, label, **args):
		self._value = value
		self._values = values
		self._label = label
		if data.value():
			self._value(data.value())
		iliad.form.Field.__init__(self, label=label, value=value, **args)

	def render(self, env):
		template = env.get_template('form/select.html')
		return (False, template.render(id=self._id, value=self._value(), values=self._values, label=self._label))

