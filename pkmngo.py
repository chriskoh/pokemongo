# pkmngo.py
# pokemon go flask application

import sys
from flask import Flask, render_template, request, url_for, Markup
import json
import math
import urllib
from pkmngoLib.calculations import *
from pkmngoLib.markup import *

application = Flask(__name__)

@application.route('/pokemongo/')
def form():

    pkmnSelectMarkup = pkmnSelect()

    return render_template('form.html', pkmnSelect=pkmnSelectMarkup)

@application.route('/pokemongo/cp/', methods=["POST"])
def cp():

    # get information from form.html
    pkmnID = request.form["pokemonSelect"]
    actualCP = request.form["aCP"]
    hp = request.form["HP"]
    dust = request.form["DUST"]

    # load pokemon data as data
    response = urllib.urlopen('http://chriskoh.io/static/pokemon.json')
    data = json.load(response)

    # Calculate min and max for stats (Min = 0 IV, Max = 15 IV)
    baseAttack = data[pkmnID]["baseAttack"]
    baseDefense = data[pkmnID]["baseDefense"]
    baseStamina = data[pkmnID]["baseStamina"]
     
    # calclate stats based on pokemons level
    stats = calcStats(baseAttack, baseDefense, baseStamina, actualCP, hp, dust)
    ivSets = printIVs(stats)

    # create dictionary to be passed in to cp.html
    pokemon = {
        "id": pkmnID,
        "name": data[pkmnID]["name"],
        "baseStamina": baseStamina,
        "baseAttack": baseAttack,
        "baseDefense": baseDefense,
        "type1": data[pkmnID]["type1"],
        "type2": data[pkmnID]["type2"],
        "rateCapture": data[pkmnID]["rateCapture"],
        "rateFlee": data[pkmnID]["rateFlee"],
        "candyToEvolve": data[pkmnID]["candyToEvolve"],
        "movement": data[pkmnID]["movement"],
        "quickMoves": data[pkmnID]["quickMoves"],
        "cinematicMoves": data[pkmnID]["cinematicMoves"],
        "family": data[pkmnID]["family"]
    }

    pkmnSelectMarkup = pkmnSelect()
 
    return render_template('cp.html', ivSets=ivSets, pkmnSelect=pkmnSelectMarkup, pokemon=pokemon, stats=stats)

if __name__ == "__main__":
    application.run(host='0.0.0.0')
