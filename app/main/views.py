from flask import render_template,redirect, url_for,request
from flask_login import current_user,login_required
from . import main
from .forms import BlogForm, CommentForm
from app.models import Post,Comment
from app.request_handle import get_quote
from app import db

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


@main.route("/comment/delete/<int:comment_id>")
@login_required
def delete_comment(comment_id):
    comment=Comment.query.filter_by(id=comment_id).first()
    blog_id=comment.post_id
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for("main.blog",blog_id=blog_id))

@main.route("/blog/delete/<int:blog_id>")
def delete_blog(blog_id):
    blog=Post.query.filter_by(id=blog_id).first()
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for("main.index"))


@main.route("/blog/edit/<int:blog_id>",methods=["GET","POST"])
def edit_blog(blog_id):
    post=Post.query.filter_by(id=blog_id).first()
    blog_form=BlogForm()
    if request.method=="POST" and blog_form.validate_on_submit():
        post.title=blog_form.title.data
        post.text=blog_form.blog.data
        db.session.commit()
        return redirect(url_for("main.index"))
    blog_form.title.data=post.title
    blog_form.blog.data=post.text
    return render_template('./main/edit_blog.html',blog_form=blog_form,quote=get_quote())
