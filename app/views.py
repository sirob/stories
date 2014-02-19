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
	return render_template("index.html", stories = stories)


@app.route('/submit', methods = ['GET', 'POST'])
def submit():
	form = PostForm()
	if form.validate_on_submit():
		post = Story(title = form.title.data,
			body = form.body.data,
			location = form.location.data,
			pseudonym = form.pseudonym.data,
			time = form.time.data,
			timestamp = datetime.utcnow())
		db.session.add(post)
		db.session.commit()
		flash("Thank you, this site depends on people like you. Here's your story!")
		return redirect(url_for("story",
			id = str(post.id)))
	return render_template("submit.html",
		form = form)
		

@app.route('/story/<id>')
def story(id):
	story = models.Story.query.get(id)
	return render_template("story.html",
		story = story)