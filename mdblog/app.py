from flask import Flask
from flask import render_template

flask_app = Flask(__name__)

@flask_app.route("/")
def index():
    return render_template("index.html")

@flask_app.route("/articles/")
def articles():
    return render_template("articles.html")

@flask_app.route("/admin/")
def admin():
    return render_template("admin.html")

