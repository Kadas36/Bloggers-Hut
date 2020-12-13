from datetime import datetime
from sqlalchemy.orm import backref
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255), unique = True, index = True)
    password = db.Column(db.String(255))
    blogs = db.relationship('Blog', backref = 'user', lazy = "dynamic")
    pass_secure = db.Column(db.String(255))
    comment_id = db.relationship('Comment', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'


class Blog(db.Model):
    __tablename__= 'blogs'

    id = db.Column(db.Integer, primary_key = True)
    blog_title = db.Column(db.String,index = True)
    blog_body = db.Column(db.String,index = True)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref = 'blogs', lazy = "dynamic")

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blogs(cls):    
        blogs = Blog.query.all()
        return blogs

class Comment(db.Model):
    __tablename__= 'comments'

    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String,index = True)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

          