from flask import render_template, flash, redirect # new
from flask_test import app 
from flask_test.forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST']) # new
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)