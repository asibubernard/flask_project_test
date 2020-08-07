from flask import render_template, flash, redirect, url_for, request # new
from flask_test import app 
from flask_test.forms import LoginForm
from flask_test.email import send_message


@app.route('/')
@app.route('/index')
def index():
    email = {'emailID': 'email.com'}
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print("++++++++++++++++++++++")
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['subject'])
        print(request.form['message'])
        flash('Login requested for the name {}, email {}, subject {} message{}'.format(
            form.name.data, form.email.data, form.subject.data, form.message.data))
        send_message(request.form)
        return redirect(url_for('index'))  # new
    return render_template('login.html', title='Sign In', form=form)

