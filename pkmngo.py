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

    pkmndatalistmarkup = pkmndatalist()

    return render_template('form.html', pkmndatalist=pkmndatalistmarkup)

@application.route('/pokemongo/cp/', methods=["POST"])
def cp():

    # get information from form.html
    actualCP = request.form["aCP"]
    hp = request.form["HP"]
    dust = request.form["DUST"]
    pkmnIDph = request.form["nameph"]
    pkmnIDph = pkmnIDph.lower()

    response = urllib.urlopen('http://chriskoh.io/static/ids.json')
    iddata = json.load(response)
    pkmnID = "{0:0>3}".format(iddata[pkmnIDph]["id"])

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
        printChart1 = printChart('chart1')
        printChart2 = printChart('chart2')
        noChart1 = ''
        noChart2 = ''
        
        if data[evolveID1]["candyToEvolve"] != 0:
            evolveID2 = int(evolveID1) + 1
            evolveID2 = "%03d" % (evolveID2)
            evolveID2Name = data[evolveID2]["name"]
            evolveID2Stats = calcEvolveStats(data[evolveID2]["baseAttack"], data[evolveID2]["baseDefense"], data[evolveID2]["baseStamina"], evolveID2Name, stats["possibleBEST"], stats["possibleWORST"])
            evolveID2ivSets = printEvolveIVs(evolveID2Stats, evolveID2Name)
            evolveID2chart = ivChart(data[evolveID2]["name"], evolveID2Stats["bestChart"], evolveID2Stats["possibleChart"], "2")
            printChart2 = printChart('chart2')
            noChart2 = ''
        else:
            evolveID2ivSets = ''
            evolveID2chart = ''
            printChart2 = ''
            noChart2 = noChart()

    else:
        evolveID1ivSets = ''
        evolveID2ivSets = ''
        evolveID1chart = ''
        evolveID2chart = ''
        printChart2 = ''
        printChart1 = ''
        noChart1 = noChart()
        noChart2 = noChart()

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
        "family": data[pkmnID]["family"],
        "cp": actualCP,
        "hp": hp,
        "dust": dust
    }

    pkmndatalistmarkup = pkmndatalist()
 
    return render_template('cp.html', printchart1=printChart1, printchart2=printChart2, nochart1=noChart1, nochart2=noChart2, pkmndatalist=pkmndatalistmarkup, chart=chart, chart2=evolveID1chart, chart3=evolveID2chart, ev1=evolveID1ivSets, ev2=evolveID2ivSets, ivSets=ivSets, pokemon=pokemon, stats=stats)

if __name__ == "__main__":
    application.run(host='0.0.0.0')
