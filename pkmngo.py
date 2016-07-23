# pkmngo.py
# pokemon go flask application

from flask import Flask, render_template, request, url_for, Markup
import json

application = Flask(__name__)

@application.route('/pokemongo/')
def form():

    with open('data/pokemon.json') as data_file:
        data = json.load(data_file)

    keylist = data.keys()
    keylist.sort()

    select = ''
    for key in keylist:
        select += "<option value='" + key + "'>" + key + ". " + str(data[key]["name"]) + "</option>"

    markupSelect = Markup(select)

    return render_template('form.html', pkmnselect=markupSelect)

@application.route('/pokemongo/cp/', methods=["POST"])
def cp():

    pkmnID = request.form["pokemonSelect"]

    with open('data/pokemon.json') as data_file:
        data = json.load(data_file)

    pokemon = {}    
    pokemon["id"] = pkmnID
    pokemon["name"] = data[pkmnID]["name"]
    pokemon["baseStamina"] = data[pkmnID]["baseStamina"]
    pokemon["baseAttack"] = data[pkmnID]["baseAttack"]
    pokemon["baseDefense"] = data[pkmnID]["baseDefense"]
    pokemon["type1"] = data[pkmnID]["type1"]
    pokemon["type2"] = data[pkmnID]["type2"]
    pokemon["rateCapture"] = data[pkmnID]["rateCapture"]
    pokemon["rateFlee"] = data[pkmnID]["rateFlee"]
    pokemon["candyToEvolve"] = data[pkmnID]["candyToEvolve"]
    pokemon["movement"] = data[pkmnID]["movement"]        
    pokemon["quickMoves"] = data[pkmnID]["quickMoves"]
    pokemon["cinematicMoves"] = data[pkmnID]["cinematicMoves"]
    pokemon["family"] = data[pkmnID]["family"]

    return render_template('cp.html', pokemon=pokemon)

if __name__ == "__main__":
    application.run(host='0.0.0.0')
