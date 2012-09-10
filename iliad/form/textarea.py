import iliad.form.text

class Field(iliad.form.text.Field):

	def render(self, env):
		template = env.get_template('form/textarea.html')
		return (False, template.render(id=self._id, value=self._value(), label=self._label))

