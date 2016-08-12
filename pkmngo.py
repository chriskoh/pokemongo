# pkmngo.py
# pokemon go flask application

import sys
from flask import Flask, render_template, request, url_for, Markup
import json
import math
import urllib
import plotly
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
    chart = ivChart(data[pkmnID]["name"], stats["bestChart"], stats["possibleChart"], "0")

    #evolves (if possible)
    if data[pkmnID]["candyToEvolve"] != 0:
        evolveID1 = int(pkmnID) + 1
        evolveID1 = "%03d" % (evolveID1)
        evolveID1Name = data[evolveID1]["name"]
        evolveID1Stats = calcEvolveStats(data[evolveID1]["baseAttack"], data[evolveID1]["baseDefense"], data[evolveID1]["baseStamina"], evolveID1Name, stats["possibleBEST"], stats["possibleWORST"])
        evolveID1ivSets = printEvolveIVs(evolveID1Stats, evolveID1Name)
        evolveID1chart = ivChart(data[evolveID1]["name"], evolveID1Stats["bestChart"], evolveID1Stats["possibleChart"], "1")
        
        if data[evolveID1]["candyToEvolve"] != 0:
            evolveID2 = int(evolveID1) + 1
            evolveID2 = "%03d" % (evolveID2)
            evolveID2Name = data[evolveID2]["name"]
            evolveID2Stats = calcEvolveStats(data[evolveID2]["baseAttack"], data[evolveID2]["baseDefense"], data[evolveID2]["baseStamina"], evolveID2Name, stats["possibleBEST"], stats["possibleWORST"])
            evolveID2ivSets = printEvolveIVs(evolveID2Stats, evolveID2Name)
            evolveID2chart = ivChart(data[evolveID2]["name"], evolveID2Stats["bestChart"], evolveID2Stats["possibleChart"], "2")
        else:
            evolveID2ivSets = ''
            evolveID2chart = ''

    else:
        evolveID1ivSets = ''
        evolveID2ivSets = ''
        evolveID1chart = ''
        evolveID2chart = ''

    catchrate = "{:.2f}".format((data[pkmnID]["rateCapture"]) * 100)
    fleerate = "{:.2f}".format((data[pkmnID]["rateFlee"]) * 100)

    # create dictionary to be passed in to cp.html
    pokemon = {
        "id": pkmnID,
        "name": data[pkmnID]["name"],
        "lname": data[pkmnID]["name"].lower(),
        "baseStamina": baseStamina,
        "baseAttack": baseAttack,
        "baseDefense": baseDefense,
        "type1": data[pkmnID]["type1"],
        "type2": data[pkmnID]["type2"],
        "rateCapture": catchrate,
        "rateFlee": fleerate,
        "candyToEvolve": data[pkmnID]["candyToEvolve"],
        "movement": data[pkmnID]["movement"],
        "quickMoves": data[pkmnID]["quickMoves"],
        "cinematicMoves": data[pkmnID]["cinematicMoves"],
        "family": data[pkmnID]["family"]
    }

    pkmnSelectMarkup = pkmnSelect()
 
    return render_template('cp.html', chart=chart, chart2=evolveID1chart, chart3=evolveID2chart, ev1=evolveID1ivSets, ev2=evolveID2ivSets, ivSets=ivSets, pkmnSelect=pkmnSelectMarkup, pokemon=pokemon, stats=stats)

if __name__ == "__main__":
    application.run(host='0.0.0.0')
