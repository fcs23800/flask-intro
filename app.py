# import the flask class from the Flask module
from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps

# create the application object
app = Flask(__name__)

# create a secret key for sessions and cookies
app.secret_key = "hari-om-tat-sat"

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
	return render_template('index.html')

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

# start the server with the run() method
if __name__ == '__main__':
	app.run(debug=True)
