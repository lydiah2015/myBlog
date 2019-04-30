from flask import render_template,redirect, url_for
from flask_login import current_user,login_required
from . import main
from .forms import BlogForm, CommentForm
from app.models import Post,Comment
from app.request_handle import get_quote

@main.route("/",methods=["GET","POST"])
def index():
    blogs=Post.query.all()
    return render_template('index.html',blogs=blogs,quote=get_quote())

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
    return render_template('./main/add_blog.html',blog_form=blog_form,quote=get_quote())


@main.route("/blog/<int:blog_id>",methods=["GET","POST"])
def blog(blog_id):
    comment_form=CommentForm()
    if comment_form.validate_on_submit():
        comment=Comment(
            user_id=current_user.id,
            post_id=blog_id,
            text=comment_form.comment.data
        )
        comment.save()
    comments=Comment.query.filter_by(post_id=blog_id)
    blog=Post.query.filter_by(id=blog_id).first()
    context={"blog":blog,"comments":comments,"comment_form":comment_form,"quote":get_quote()}
    return render_template("./main/blog.html",**context)