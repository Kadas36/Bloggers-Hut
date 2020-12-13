from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from ..models import Blog
from wtforms.validators import DataRequired


class BlogForm(FlaskForm):

    blog_title = StringField('Break Time', validators=[DataRequired()])
    blog_body = TextAreaField('Enter Break Activity', validators=[DataRequired()])
    submit = SubmitField('Submit')