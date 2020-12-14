from app.requests import get_quote
from app.models import Blog, Comment, User
from flask import render_template, url_for, flash, redirect, request, abort
from flask.globals import session
from . import main
from flask_login import login_required, current_user
from ..import db
from .forms import BlogForm, CommentForm
from ..email import mail_message

@main.route('/')
def index():
    """
    Function that returns the index page
    """
    random_quote = get_quote()
    
    return render_template('index.html', random_quote = random_quote)



@main.route('/blogs', methods = ['GET','POST'])
@login_required
def new_blog():
    form = BlogForm()
    subscribers = User.query.filter_by(subscribe_blogs = True).all()
    if form.validate_on_submit():
        blog_title = form.blog_title.data
        blog_body = form.blog_body.data

        #updated blog
        new_blog = Blog(blog_title=blog_title, blog_body=blog_body, user=current_user)

        #save blog
        new_blog.save_blog()
        return redirect(url_for('main.new_blog'))  

        mail_message = ("New post alert", "email/new_post", user.email, subscribers) 

    blogs = Blog.get_blogs()

    return render_template('blogs.html', form = form, blogs_list = blogs) 
    



@main.route('/recent_blogs', methods = ['GET'])
@login_required
def recent_blogs():
        
    blogs = reversed(Blog.get_blogs())

    return render_template('recent.html', recent_list = blogs)     



@main.route('/blogs/<int:blog_id>', methods = ['GET','POST'])
@login_required
def blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)

    commentform = CommentForm()
    
    if commentform.validate_on_submit():
        comment = commentform.comment.data

        #updated comment
        new_comment = Comment(comment=comment, blog_id=blog_id)

        #save comment
        new_comment.save_comment()
        return redirect(url_for('main.new_blog'))   

    comments = Comment.query.filter_by(blog_id=blog_id).all()

    title = blog.blog_title
    return render_template('comment.html', title=title, blog=blog, commentform = commentform, comments_list = comments)   

