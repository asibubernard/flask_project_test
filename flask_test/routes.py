from flask import render_template
from flask_test import app 


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
