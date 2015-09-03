from flask_wtf import Form
from wtforms import TextField, TextAreaField
from wtforms.validators import DataRequired, Length


class MessageForm(Form):
	title = TextField('Title', validators=[DataRequired()])
	description = TextAreaField('Description', validators=[DataRequired(), Length(min=6, max=4096)])
