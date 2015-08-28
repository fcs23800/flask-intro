# import the flask class from the Flask module
from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from functools import wraps

import sqlite3

# create the application object
app = Flask(__name__)

# create a secret key for sessions and cookies
app.secret_key = "hari-om-tat-sat"
app.database = "sample.db"

#login required decorator
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('You need to login first.')
			return redirect(url_for('login'))
	return wrap

# use decorators to link the function to a url - Home page
@app.route('/')
@login_required
def home():
	# return "Hello, World!"  # return a string
	g.db = connect_db()
	cur = g.db.execute('select * from posts')
	posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
	g.db.close()
	return render_template('index.html', posts=posts)  # render a template

@app.route('/welcome')
def welcome():
	return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid Credentials. Please try again.'
		else:
			session['logged_in'] = True
			flash('You are logged in.')
			return redirect(url_for('home'))
	return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in', None)
	flash('You are logged out.')
	return redirect(url_for('welcome'))

# connect to database
def connect_db():
	return sqlite3.connect(app.database)

# start the server with the run() method
if __name__ == '__main__':
	app.run(debug=True)
