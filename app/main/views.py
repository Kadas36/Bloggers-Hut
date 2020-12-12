from flask import render_template, url_for, flash, redirect, request, abort
from . import main
from flask_login import login_required, current_user
from ..models import User
from ..import db

@main.route('/')
def index():
   return render_template('index.html')



  