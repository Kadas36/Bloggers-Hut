from app.models import Blog, Comment
from flask import render_template, url_for, flash, redirect, request, abort
from flask.globals import session
from . import main
from flask_login import login_required, current_user
from ..import db
from .forms import BlogForm, CommentForm

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

    comments = Comment.get_comments()

    title = blog.blog_title
    return render_template('comment.html', title=title, blog=blog, commentform = commentform, comments_list = comments)   




# @main.route('/blogs/comments', methods = ['GET','POST'])
# @login_required
# def new_comment():
#     commentform = CommentForm()
    
#     if commentform.validate_on_submit():
#         comment = commentform.comment.data

#         #updated comment
#         new_comment = Comment(comment=comment)

#         #save comment
#         new_comment.save_comment()
#         return redirect(url_for('main.new_blog'))   

#     comments = Comment.get_comments()

#     return render_template('comments.html', commentform = commentform, comments_list = comments)     