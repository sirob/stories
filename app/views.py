#-*- coding: utf-8 -*-

from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, models
from forms import PostForm
from models import Story
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
	stories = models.Story.query.order_by('timestamp desc').all()
	t = [s.title for s in stories]
	i = [s.id for s in stories]
	return render_template("index.html",
		story1 = t[0], id1 = str(i[0]),
		story2 = t[1], id2 = str(i[1]),
		story3 = t[2], id3 = str(i[2]),
		story4 = t[3], id4 = str(i[3]),
		story5 = t[4], id5 = str(i[4]),
		story6 = t[5], id6 = str(i[5]),
		story7 = t[6], id7 = str(i[6]),
		story8 = t[7], id8 = str(i[7]),
		story9 = t[8], id9 = str(i[8]),
		story10 = t[9], id10 = str(i[9])) #tole se mi zdi zlo neelegantna rešitev?

@app.route('/submit', methods = ['GET', 'POST'])
def submit():
	form = PostForm()
	if form.validate_on_submit():
		post = Story(title = form.title.data,
			body = form.body.data,
			location = form.location.data,
			pseudonym = form.pseudonym.data,
			email = form.email.data,
			timestamp = datetime.utcnow()) #zakaj je eno uro prej?
		db.session.add(post)
		db.session.commit()
		flash("Here's your story!")
		return redirect(url_for("story",
			id = str(post.id)))
	return render_template("submit.html",
		form = form)
		

@app.route('/story/<id>')
def story(id):
	story = models.Story.query.get(id)
	return render_template("story.html",
		story = story)