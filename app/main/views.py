from flask import render_template,redirect, url_for
from flask_login import current_user,login_required
from . import main
from app.models import Post

@main.route("/",methods=["GET","POST"])
def index():
    blogs=Post.query.all()
    return render_template('index.html',blogs=blogs)


