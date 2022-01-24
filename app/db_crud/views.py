# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from crypt import methods
from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from app.db_crud.forms import SensorData
from . import db_crud

@db_crud.route("/", methods=["GET", "POST"])
def home():
    """Home page."""
    #current_app.logger.info("Hello from the home page!")
    # Handle logging in 
    return render_template("db_crud/home.html")

@db_crud.route("/about/")
def about():
    return render_template('db_crud/about.html')

@db_crud.route("/CRUD/", methods=["GET","POST"])
def crud():
    form = SensorData()
    return render_template('db_crud/crud.html', form = form)

'''
@blueprint.route("/logout/")
@login_required
def logout():
    """Logout."""
    logout_user()
    flash("You are logged out.", "info")
    return redirect(url_for("db_crud.home"))


@blueprint.route("/register/", methods=["GET", "POST"])
def register():
    """Register new user."""
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        User.create(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
            active=True,
        )
        flash("Thank you for registering. You can now log in.", "success")
        return redirect(url_for("db_crud.home"))
    else:
        flash_errors(form)
    return render_template("db_crud/register.html", form=form)


@blueprint.route("/about/")
def about():
    """About page."""
    form = LoginForm(request.form)
    return render_template("db_crud/about.html", form=form)

@blueprint.route("/search/",methods=['GET', 'POST'])
def search():    
    """search."""
    db = SQLManager()
    data = db.showversion()
    #print(data)
    db.close()
    return render_template("db_crud/search.html", data = data) 
'''