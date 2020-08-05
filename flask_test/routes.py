from flask import render_template
from flask_test import app 
from flask_test.forms import LoginForm # new

@app.route('/')
@app.route('/index')
def index():
    email = {'emailID': 'asibubernard@email.com'}
    posts = [
        {
            'author': {'username': 'Maxwell'},
            'body' : 'It is a great day in Ghana'
        },
        {
            'author': {'username': 'Michael'},
            'body': 'The world is becoming a better place',
        }
    ]
    return render_template('index.html', title='Home', email=email, posts=posts)

@app.route('/login') # new
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)