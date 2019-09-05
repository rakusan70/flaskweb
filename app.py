from flask import Flask

flask_app = Flask(__name__)

@flask_app.route("/")
def index():
    return "Hello World"

@flask_app.route("/admin/")
def admin():
    return "Hello Admin"