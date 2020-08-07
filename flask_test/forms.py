from flask_wtf import FlaskForm 
from wtforms import StringField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    name = StringField('Username', validators=[DataRequired()])
    email = StringField('Password', validators=[DataRequired()])
    subject = StringField('Phone_Number', validators=[DataRequired()])
    message = TextAreaField('Text Area', validators=[DataRequired()])
    submit = SubmitField('Sign in')