from flask_test import app 

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Bernard'}
    return '''
<html>
    <head>
        <title>Home Page - Flask_Test_Project</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''