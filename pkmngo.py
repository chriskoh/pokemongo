# pkmngo.py
# pokemon go flask application

import sys
from flask import Flask, render_template, request, url_for, Markup
import json
import math
from pkmngoLib.calculations import *

application = Flask(__name__)

@application.route('/pokemongo/')
def form():

    # load pokemon.json as data
    with open('data/pokemon.json') as data_file:
        data = json.load(data_file)

    # get list of keys sorted in numerical order
    keylist = data.keys()
    keylist.sort()

    # create select options based on every pokemon found in pokemon.json
    pkmnSelect = ''
    for key in keylist:
        pkmnSelect += "<option value='" + key + "'>" + key + ". " + str(data[key]["name"]) + "</option>"

    # create select options 1-40 for trainer levels
    lvlSelect = ''
    for x in range(1,41):
        lvlSelect += "<option value='" + str(x) + "'>" + str(x) + "</option>"

    # convert string in to mark up text
    pkmnSelectMarkup = Markup(pkmnSelect)
    lvlSelectMarkup = Markup(lvlSelect)

    return render_template('form.html', pkmnSelect=pkmnSelectMarkup, lvlSelect=lvlSelectMarkup)

@application.route('/pokemongo/cp/', methods=["POST"])
def cp():

    # get information from form.html
    pkmnID = request.form["pokemonSelect"]
    trainerLVL = request.form["levelSelect"]
    cpArc = request.form["cpArc"]
    actualCP = request.form["aCP"]

    # load pokemon data as data
    with open('data/pokemon.json') as data_file:
        data = json.load(data_file)

    # Calculate min and max for stats (Min = 0 IV, Max = 15 IV)
    baseAttack = data[pkmnID]["baseAttack"]
    baseDefense = data[pkmnID]["baseDefense"]
    baseStamina = data[pkmnID]["baseStamina"]
     
    # calclate stats based on pokemons level
    pkmnLVL = str(int(((float(cpArc)/100)*int(trainerLVL))))
    currentStats = calcStats(baseAttack, baseDefense, baseStamina, pkmnLVL)
    trainerStats = calcStats(baseAttack, baseDefense, baseStamina, trainerLVL)
    maxStats = calcStats(baseAttack, baseDefense, baseStamina, "40")
    ivRatio = int((float(int(actualCP) - currentStats["minCP"])/(currentStats["maxCP"] - currentStats["minCP"]))*100)
#    ivRatio = int((float(actualCP)/currentStats["maxCP"])*100)

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
 
    return render_template('cp.html', pokemonLVL=pkmnLVL, trainerLVL=trainerLVL, pokemon=pokemon, trainerStats=trainerStats, maxStats=maxStats, currentStats=currentStats, ivRatio=ivRatio)

if __name__ == "__main__":
    application.run(host='0.0.0.0')
