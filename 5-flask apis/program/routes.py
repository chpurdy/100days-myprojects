from program import app
from flask import render_template
import requests
from datetime import datetime




@app.route('/')
@app.route('/index')
def index():
    timenow = str(datetime.today())
    return render_template("index.html", time=timenow)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/classes')
def classes():
    return render_template("classes.html")

@app.route('/chuck')
def chuck():
    joke = get_chuck_joke()
    return render_template("chuck.html",joke=joke)


def get_chuck_joke():
    data = requests.get('https://api.chucknorris.io/jokes/random').json()
    return data['value']

