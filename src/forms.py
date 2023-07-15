from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, BooleanField, EmailField,DecimalField
from wtforms.validators import DataRequired, Length, Email, ValidationError

def length_check(form,field):
    if len(field.data) == 0:
        raise ValidationError('Fields should not be null')
    

class AddReaderForm(Form):
    course_name = StringField('Course Name', validators=[ DataRequired()])
    learning_hours = StringField('Learning Hours', validators = [DataRequired()])
    rating = StringField('Rating', validators=[ DataRequired()])
    course_type = StringField('Course Type', validators = [DataRequired()])
    price = DecimalField('Price', validators=[ DataRequired()])
    subject = StringField('Subject', validators = [DataRequired()])


class SignUpForm(Form):
    password = PasswordField('Password',validators=[ DataRequired(), Length(min=5)])
    user_id = StringField('User ID', validators= [DataRequired(), Length(min=5)])
    submit = SubmitField('Sign Up')


class SignInForm(Form):
    user_id = StringField('User ID', validators = [DataRequired(), Length(min=5)])
    password = PasswordField('Password', validators = [DataRequired(), Length(min=5, max=30)])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Sign In')
