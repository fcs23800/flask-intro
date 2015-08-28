# import the flask class from the Flask module
from flask import Flask, render_template

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url - Home page
@app.route('/')
def home():
	return render_template('index.html')

@app.route('/welcome')
def welcome():
	return render_template('welcome.html')

# start the server with the run() method
if __name__ == '__main__':
	app.run(debug=True)
