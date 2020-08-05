from flask import render_template
from flask_test import app 

@app.route('/')
@app.route('/index')
def index():
    email = {'emailID': 'asibubernard@email.com'}
    return render_template('index.html', title='Home', email=email)
