from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField
from wtforms.validators import Required, Length, Email
import datetime

class PostForm(Form):
	title = TextField('title', validators = [Required(), Length(min = 1, max = 140)])
	body = TextAreaField('body', validators = [Required(), Length(min = 100, max = 1800)])
	location = TextField('location', validators = [Length(min = 2, max = 64)])
	timestamp = datetime.datetime.utcnow()
	pseudonym = TextField('pseudonym', validators = [Required(), Length(min = 1, max = 64)])
	email = TextField('email', validators = [Email(), Required(), Length(min = 5, max = 120)])