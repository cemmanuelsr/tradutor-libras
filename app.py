import os
from flask import Flask, render_template, send_from_directory


app = Flask(__name__, static_folder="./templates/static")
app.config["SECRET_KEY"] = "secret!"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )