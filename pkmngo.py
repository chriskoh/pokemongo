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

    # load pokemon data as data
    with open('data/pokemon.json') as data_file:
        data = json.load(data_file)

    # load "CP Modifier" as cpm static variables
#    with open('data/cpm.json') as data_file:
#        cpm = json.load(data_file)

    # calculate "Additional CP Modifier" (acpm), difference between two CPMs after upgrading
#    if int(trainerLVL) < 40:
#        acpm = cpm[str(int(trainerLVL) + 1)]["CpM"] - cpm[trainerLVL]["CpM"]
#    else:
#        acpm = 0

    # Excact CP Modifier (ecpm)
#    ecpm = cpm[trainerLVL]["CpM"] + acpm

    # Calculate min and max for stats (Min = 0 IV, Max = 15 IV)
    baseAttack = data[pkmnID]["baseAttack"]
    baseDefense = data[pkmnID]["baseDefense"]
    baseStamina = data[pkmnID]["baseStamina"]
     
#    minAttack = (baseAttack + 0) * ecpm
#    minDefense = (baseDefense + 0) * ecpm
#    minStamina = (baseStamina + 0) * ecpm

#    maxAttack = (baseAttack + 15) * ecpm
#    maxDefense = (baseDefense + 15) * ecpm
#    maxStamina = (baseStamina + 15) * ecpm

#    minHP = math.floor(minStamina)
#    maxHP = math.floor(maxStamina)

#    minCP = max(10,math.floor(math.pow(minStamina,0.5) * minAttack * math.pow(minDefense,0.5) / 10))
#    maxCP = max(10,math.floor(math.pow(maxStamina,0.5) * maxAttack * math.pow(maxDefense,0.5) / 10)) 

    # this is broken
    trainerStats = calcStats(baseAttack, baseDefense, baseStamina, trainerLVL)

    # create dictionary to be passed in to cp.html
    pokemon = {}    
    pokemon["id"] = pkmnID
    pokemon["name"] = data[pkmnID]["name"]
#    pokemon["ecpm"] = ecpm
    pokemon["baseStamina"] = baseStamina 
    pokemon["baseAttack"] = baseAttack
    pokemon["baseDefense"] = baseDefense
#    pokemon["minStamina"] = minStamina
#    pokemon["minAttack"] = minAttack
#    pokemon["minDefense"] = minDefense
#    pokemon["maxStamina"] = maxStamina
#    pokemon["maxAttack"] = trainerStats["minAttack"] 
#    pokemon["maxDefense"] = maxDefense
#    pokemon["minHP"] = minHP
#    pokemon["maxHP"] = maxHP
#    pokemon["minCP"] = minCP
#    pokemon["maxCP"] = maxCP
    pokemon["type1"] = data[pkmnID]["type1"]
    pokemon["type2"] = data[pkmnID]["type2"]
    pokemon["rateCapture"] = data[pkmnID]["rateCapture"]
    pokemon["rateFlee"] = data[pkmnID]["rateFlee"]
    pokemon["candyToEvolve"] = data[pkmnID]["candyToEvolve"]
    pokemon["movement"] = data[pkmnID]["movement"]        
    pokemon["quickMoves"] = data[pkmnID]["quickMoves"]
    pokemon["cinematicMoves"] = data[pkmnID]["cinematicMoves"]
    pokemon["family"] = data[pkmnID]["family"]
 
    return render_template('cp.html', pokemon=pokemon, trainerStats=trainerStats)

if __name__ == "__main__":
    application.run(host='0.0.0.0')
