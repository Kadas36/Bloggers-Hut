from app.models import Blog
from flask import render_template, url_for, flash, redirect, request, abort
from flask.globals import session
from . import main
from flask_login import login_required, current_user
from ..import db
from .forms import BlogForm

@main.route('/')
def index():
    """
    Function that returns the index page
    """
    return render_template('index.html')



@main.route('/blogs', methods = ['GET','POST'])
@login_required
def new_blog():
    form = BlogForm()
    
    if form.validate_on_submit():
        blog_title = form.blog_title.data
        blog_body = form.blog_body.data

        #updated blog
        new_blog = Blog(blog_title=blog_title, blog_body=blog_body, user=current_user)

        #save blog
        new_blog.save_blog()
        return redirect(url_for('main.new_blog'))   

    blogs = Blog.get_blogs()

    return render_template('blogs.html', form = form, blogs_list = blogs) 