# markup.py
# library for html markup

import urllib
import json
from flask import Markup

def pkmnSelect():

    # load pokemon.json as data
    response = urllib.urlopen('http://chriskoh.io/static/pokemon.json')
    data = json.load(response)

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

def printEvolveIVs(stats, name):
#   possibleBEST, possibleBESTCP, BEST, BESTCP

    cpRow = '<table>' \
                '<tr>' \
                    '<th>' + name + '</th>' \
                    '<th>CP</th>' \
                    '<th>HP</th>' \
                    '<th>Attack</th>' \
                    '<th>Defense</th>' \
                    '<th>Stamina</th>' \
                '<tr>' \
                    '<td>' + str('Best Possible') + '</td>' \
                    '<td>' + str(stats["BESTCP"]) + '</td>' \
                    '<td>' + str(stats["BESTHP"]) + '</td>' \
                    '<td>' + str(stats["BEST"][1]) + '</td>' \
                    '<td>' + str(stats["BEST"][2]) + '</td>' \
                    '<td>' + str(stats["BEST"][3]) + '</td>' \
                '</tr>' \
                '<tr>' \
                    '<td>' + str('Best IV Set') + '</td>' \
                    '<td>' + str(stats["possibleBESTCP"]) + '</td>' \
                    '<td>' + str(stats["possibleBESTHP"]) + '</td>' \
                    '<td>' + str(stats["possibleBEST"][1]) + '</td>' \
                    '<td>' + str(stats["possibleBEST"][2]) + '</td>' \
                    '<td>' + str(stats["possibleBEST"][3]) + '</td>' \
                '</tr>' \
                '<tr>' \
                    '<td>' + str('Worst IV Set') + '</td>' \
                    '<td>' + str(stats["possibleWORSTCP"]) + '</td>' \
                    '<td>' + str(stats["possibleWORSTHP"]) + '</td>' \
                    '<td>' + str(stats["possibleWORST"][1]) + '</td>' \
                    '<td>' + str(stats["possibleWORST"][2]) + '</td>' \
                    '<td>' + str(stats["possibleWORST"][3]) + '</td>' \
                '</tr>' \
                '<tr>' \
                    '<td>' + str('Worst Possible') + '</td>' \
                    '<td>' + str(stats["WORSTCP"]) + '</td>' \
                    '<td>' + str(stats["WORSTHP"]) + '</td>' \
                    '<td>' + str(stats["WORST"][1]) + '</td>' \
                    '<td>' + str(stats["WORST"][2]) + '</td>' \
                    '<td>' + str(stats["WORST"][3]) + '</td>' \
                '</tr>' \
            '</table><br />'

    cpRowMarkup = Markup(cpRow)

    return cpRowMarkup 
       

def printIVs(stats):

    
    ivRow = ''
    for ivSet in stats["possibleSET"]:
        ivRow += '<tr>' \
                   '<td>' + str(ivSet[0]) + '</td>' \
                   '<td>' + str(ivSet[1]) + '</td>' \
                   '<td>' + str(ivSet[2]) + '</td>' \
                   '<td>' + str(ivSet[3]) + '</td>' \
                   '<td>' + str(ivSet[4]) + '%</td>' \
               '</tr>'

    cpRow = '<tr>' \
                '<td>' + str('Best Possible') + '</td>' \
                '<td>' + str(stats["BESTCP"]) + '</td>' \
                '<td>' + str(stats["BESTHP"]) + '</td>' \
                '<td>' + str(stats["BEST"][1]) + '</td>' \
                '<td>' + str(stats["BEST"][2]) + '</td>' \
                '<td>' + str(stats["BEST"][3]) + '</td>' \
            '</tr>' \
            '<tr>' \
                '<td>' + str('Best IV Set') + '</td>' \
                '<td>' + str(stats["possibleBESTCP"]) + '</td>' \
                '<td>' + str(stats["possibleBESTHP"]) + '</td>' \
                '<td>' + str(stats["possibleBEST"][1]) + '</td>' \
                '<td>' + str(stats["possibleBEST"][2]) + '</td>' \
                '<td>' + str(stats["possibleBEST"][3]) + '</td>' \
            '</tr>' \
            '<tr>' \
                '<td>' + str('Worst IV Set') + '</td>' \
                '<td>' + str(stats["possibleWORSTCP"]) + '</td>' \
                '<td>' + str(stats["possibleWORSTHP"]) + '</td>' \
                '<td>' + str(stats["possibleWORST"][1]) + '</td>' \
                '<td>' + str(stats["possibleWORST"][2]) + '</td>' \
                '<td>' + str(stats["possibleWORST"][3]) + '</td>' \
            '</tr>' \
            '<tr>' \
                '<td>' + str('Worst Possible') + '</td>' \
                '<td>' + str(stats["WORSTCP"]) + '</td>' \
                '<td>' + str(stats["WORSTHP"]) + '</td>' \
                '<td>' + str(stats["WORST"][1]) + '</td>' \
                '<td>' + str(stats["WORST"][2]) + '</td>' \
                '<td>' + str(stats["WORST"][3]) + '</td>' \
            '</tr>'

    ivRowMarkup = Markup(ivRow)
    cpRowMarkup = Markup(cpRow)

    markups = {
        "ivSets": ivRowMarkup,
        "cpSets": cpRowMarkup
    }

    return markups 











