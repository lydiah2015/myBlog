from flask import render_template,redirect, url_for
from flask_login import current_user,login_required
from . import main
from .forms import BlogForm, CommentForm
from app.models import Post

@main.route("/",methods=["GET","POST"])
def index():
    blogs=Post.query.all()
    return render_template('index.html',blogs=blogs)

@main.route("/add_blog",methods=["GET","POST"])
@login_required
def add_blog():
    blog_form=BlogForm()
    if blog_form.validate_on_submit():
        blog=Post(
            title=blog_form.title.data,
            text=blog_form.blog.data,
            user_id=current_user.id,
        )
        blog.save()
        return redirect(url_for("main.index"))
    return render_template('./main/add_blog.html',blog_form=blog_form)
