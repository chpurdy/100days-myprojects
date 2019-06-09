from program import app
from flask import render_template, request
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

@app.route('/pokemon', methods=['GET','POST'])
def pokemon():
    pokemon = []
    if request.method == 'POST' and 'pokecolor' in request.form:
        color = request.form.get('pokecolor')
        pokemon = get_poke_colors(color)
    return render_template("pokemon.html", pokemon=pokemon)


def get_poke_colors(color):
    try:
        r = requests.get(f"https://pokeapi.co/api/v2/pokemon-color/{color.lower()}")
        pokedata = r.json()
    except:
        return ['Invalid Color']
    pokemon = []

    for i in pokedata['pokemon_species']:
        pr = requests.get(i['url']).json()
        shape = pr['shape']['name']

        pokemon.append((i['name'],shape))

    return pokemon

@app.route('/iss',methods=['POST','GET'])
def iss():
    location_url = ""
    if request.method == 'POST':
        location_url = get_iss_loc()
    return render_template('iss.html',location_url=location_url)

def get_iss_loc():
    r = requests.get('http://api.open-notify.org/iss-now.json')
    data = r.json()
    lat = data['iss_position']['latitude']
    lon = data['iss_position']['longitude']
    return f"https://www.latlong.net/c/?lat={lat}&long={lon}"