from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=150)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=150)])
    password = PasswordField('Password', validators=[DataRequired()])
    verify_password = PasswordField('Verify Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=4, max=150)])
    description = StringField('Description', validators=[DataRequired(), Length(min=4, max=150)])
    deadline = DateField('Deadline', validators=[DataRequired()])
    submit = SubmitField('Submit')