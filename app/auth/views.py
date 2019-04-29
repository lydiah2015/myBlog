from flask import render_template,redirect,url_for
from flask_login import login_user,login_required,current_user,logout_user
from . import auth
from .forms import RegisterForm,LoginForm
from app.models import User

@auth.route("/login",methods=["POST","GET"])
def login():
    form=LoginForm()
    error=False
    if form.validate_on_submit():
        username=form.username.data
        user=User.query.filter_by(username=username).first()
        if user and user.verifypass(form.password.data):
            login_user(user,form.remember.data)
            return redirect(url_for("main.index"))
        error="Wrong username or password!"
    return render_template("./auth/login.html",form=form,error=error)

@auth.route("/register",methods=["POST","GET"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    title = 'Register'
    form = RegisterForm()
    error=False
    if form.validate_on_submit():
        username=str(form.username.data)
        password=str(form.password.data)
        email=str(form.email.data)
        user=User.query.filter_by(username=username).first()
        user=User.query.filter_by(email=email).first()
        if not user:
            user=User(username=username,passwd=password,email=email)
            user.save()
            return redirect(url_for('auth.login'))
        error='User with that email or name already exists'
    return render_template("./auth/register.html", title = title ,form=form,error=error)

@auth.route("/logout")
@login_required
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect(url_for('main.index'))

@auth.route("/profile")
@login_required
def profile():
    return render_template("./auth/profile.html")



