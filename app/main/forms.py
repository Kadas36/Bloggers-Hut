from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from ..models import Blog, Comment
from wtforms.validators import DataRequired


class BlogForm(FlaskForm):

    blog_title = StringField('Title', validators=[DataRequired()])
    blog_body = TextAreaField('Blog', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = blog_title = TextAreaField('Comment', validators=[DataRequired()]) 
    submit = SubmitField('Submit')   