# External modules
from flask import render_template, redirect
# Local modules
from flaskapp.shared_variables import routes_module


# Index page
@routes_module.route("/", methods=["GET"])
def index_page():
    return redirect("/home")


# Home page
@routes_module.route("/home", methods=["GET"])
def home_page():
    return render_template("home.html")
