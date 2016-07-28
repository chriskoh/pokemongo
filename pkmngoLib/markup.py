# markup.py
# library for html markup

import json
from flask import Markup

def pkmnSelect():

    # load pokemon.json as data
    with open('/home/crees/pkmngo/data/pokemon.json') as data_file:
        data = json.load(data_file)

    # get list of keys sorted in numerical order
    keylist = data.keys()
    keylist.sort()

    # create select options based on every pokemon found in pokemon.json
    pkmnSelect = ''
    for key in keylist:
        pkmnSelect += "<option value='" + key + "'>" + str(data[key]["name"]) + "</option>"

    # convert string in to mark up text
    pkmnSelectMarkup = Markup(pkmnSelect)

    return pkmnSelectMarkup
