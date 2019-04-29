from flask import render_template,redirect, url_for
from flask_login import current_user,login_required
from . import main

@main.route("/",methods=["GET","POST"])
def index():
    return render_template('index.html')


