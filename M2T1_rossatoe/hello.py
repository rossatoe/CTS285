# minimal flask app

from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello_world():
    return "<p>Hello, world ---- page!</p>"

@app.route("/a")

def hello_worldA():
    return "<p>Hello, world --aaa-- page!</p>"