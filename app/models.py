from app import db

class Story(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(90))
	body = db.Column(db.Text(1800))
	location = db.Column(db.String(64))
	time = db.Column(db.String(90))
	timestamp = db.Column(db.DateTime)
	pseudonym = db.Column(db.String(64))

	def __repr__(self):
		return '<Story %r>' % (self.title)