from wtforms import Form, StringField
from wtforms.validators import Length
class SearchForm(Form):
  q = StringField(validators=[Length(min=1, max=30)])