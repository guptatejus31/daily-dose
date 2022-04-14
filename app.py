from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.debug = True

@app.route("/<name>")
def index(name):
    return render_template("index.html",title=name)

if __name__ == '__main__':
    app.run()
