# markup.py
# library for html markup

import urllib
import json
from flask import Markup

def printChart(chartName):

    chart = "<div id='" + chartName + "' style='height: 99%; width: 100%;'></div>"

    chartMarkup = Markup(chart)

    return chartMarkup

def noChart():

    chart = 'No evolution data'

    chartMarkup = Markup(chart)

    return chartMarkup


def ivChart(name, bestChart, possibleChart, idnum):

    chartname = "chart" + idnum

    chart =         "var " + chartname + " = new CanvasJS.Chart('" + chartname + "',{" \
                    "backgroundColor: '#FDF9E5'," \
                    "title:{" \
                        "text: '" + name + "'," \
                    "}," \
                    "theme: 'theme2'," \
                    "interval: 100," \
                    "exportEnabled: false," \
                    "animationEnabled: true," \
                    "axisY: {" \
                        "includeZero: false," \
                        "title: 'CP'," \
                    "}," \
                    "zoomEnabled: true," \
                    "axisX: {" \
                        "interval:1," \
                        "title: 'Level (Drag to scroll)'," \
                        "viewportMinimum: 30," \
                        "viewportMaximum: 40," \
                    "}," \
                    "toolTip: {" \
                        "shared: true," \
                    "}," \
                    "data: [" \
                    "{" \
                        "type: 'rangeArea'," \
                        "showInLegend: true," \
                        "name: 'Possible Range'," \
                        "yValueFormatString: '#0.## CP'," \
                        "xValueFormatString: 'Level #0'," \
                        "dataPoints: [" + bestChart + "]" \
                    "}," \
                    "{" \
                        "type: 'rangeArea'," \
                        "showInLegend: true," \
                        "name: 'Your Range'," \
                        "yValueFormatString: '#0.## CP'," \
                        "dataPoints: [" + possibleChart + "]" \
                    "}" \
                    "]" \
                "});" \
                "" + chartname + ".render();" \

    chartMarkup = Markup(chart)

    return chartMarkup 

def pkmndatalist():
    
    # load pokemon.json as data
    response = urllib.urlopen('http://chriskoh.io/static/pokemon.json')
    data = json.load(response)

    # get list of keys sorted in numerical order
    keylist = data.keys()
    keylist.sort()

    # create select options based on every pokemon found in pokemon.json
    pkmnSelect = ''
    for key in keylist:
        pkmnSelect += "<option value='" + str(data[key]["name"]) + "'>"

    # convert string in to mark up text
    pkmnSelectMarkup = Markup(pkmnSelect)

    return pkmnSelectMarkup

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

    cpRow = '<table>' \
                '<tr>' \
                    '<th>' + name + '</th>' \
                    '<th>CP</th>' \
                    '<th>HP</th>' \
                    '<th>Attack</th>' \
                    '<th>Defense</th>' \
                    '<th>Stamina</th>' \
                    '<th>Perfection</th>' \
                '</tr>' \
                '<tr>' \
                    '<td>' + str('Best Possible') + '</td>' \
                    '<td class="data">' + str(stats["BESTCP"]) + '</td>' \
                    '<td class="data">' + str(stats["BESTHP"]) + '</td>' \
                    '<td class="data">' + str(stats["BEST"][1]) + '</td>' \
                    '<td class="data">' + str(stats["BEST"][2]) + '</td>' \
                    '<td class="data">' + str(stats["BEST"][3]) + '</td>' \
                    '<td class="data">100%</td>' \
                '</tr>' \
                '<tr>' \
                    '<td>' + str('Best IV Set') + '</td>' \
                    '<td class="data">' + str(stats["possibleBESTCP"]) + '</td>' \
                    '<td class="data">' + str(stats["possibleBESTHP"]) + '</td>' \
                    '<td class="data">' + str(stats["possibleBEST"][1]) + '</td>' \
                    '<td class="data">' + str(stats["possibleBEST"][2]) + '</td>' \
                    '<td class="data">' + str(stats["possibleBEST"][3]) + '</td>' \
                    '<td class="data">' + str("%.2f" % (((stats["possibleBEST"][1] + stats["possibleBEST"][2] + stats["possibleBEST"][3])/float(45))*100)) + '%</td>' \
                '</tr>' \
                '<tr>' \
                    '<td>' + str('Worst IV Set') + '</td>' \
                    '<td class="data">' + str(stats["possibleWORSTCP"]) + '</td>' \
                    '<td class="data">' + str(stats["possibleWORSTHP"]) + '</td>' \
                    '<td class="data">' + str(stats["possibleWORST"][1]) + '</td>' \
                    '<td class="data">' + str(stats["possibleWORST"][2]) + '</td>' \
                    '<td class="data">' + str(stats["possibleWORST"][3]) + '</td>' \
                    '<td class="data">' + str("%.2f" % (((stats["possibleWORST"][1] + stats["possibleWORST"][2] + stats["possibleWORST"][3])/float(45))*100)) + '%</td>' \
                '</tr>' \
                '<tr>' \
                    '<td>' + str('Worst Possible') + '</td>' \
                    '<td class="data">' + str(stats["WORSTCP"]) + '</td>' \
                    '<td class="data">' + str(stats["WORSTHP"]) + '</td>' \
                    '<td class="data">' + str(stats["WORST"][1]) + '</td>' \
                    '<td class="data">' + str(stats["WORST"][2]) + '</td>' \
                    '<td class="data">' + str(stats["WORST"][3]) + '</td>' \
                    '<td class="data">0%</td>' \
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
                '<td class="data">' + str(stats["BESTCP"]) + '</td>' \
                '<td class="data">' + str(stats["BESTHP"]) + '</td>' \
                '<td class="data">' + str(stats["BEST"][1]) + '</td>' \
                '<td class="data">' + str(stats["BEST"][2]) + '</td>' \
                '<td class="data">' + str(stats["BEST"][3]) + '</td>' \
                '<td class="data">100%</td>' \
            '</tr>' \
            '<tr>' \
                '<td>' + str('Best IV Set') + '</td>' \
                '<td class="data">' + str(stats["possibleBESTCP"]) + '</td>' \
                '<td class="data">' + str(stats["possibleBESTHP"]) + '</td>' \
                '<td class="data">' + str(stats["possibleBEST"][1]) + '</td>' \
                '<td class="data">' + str(stats["possibleBEST"][2]) + '</td>' \
                '<td class="data">' + str(stats["possibleBEST"][3]) + '</td>' \
                '<td class="data">' + str("%.2f" % (((stats["possibleBEST"][1] + stats["possibleBEST"][2] + stats["possibleBEST"][3])/float(45))*100)) + '%</td>' \
            '</tr>' \
            '<tr>' \
                '<td>' + str('Worst IV Set') + '</td>' \
                '<td class="data">' + str(stats["possibleWORSTCP"]) + '</td>' \
                '<td class="data">' + str(stats["possibleWORSTHP"]) + '</td>' \
                '<td class="data">' + str(stats["possibleWORST"][1]) + '</td>' \
                '<td class="data">' + str(stats["possibleWORST"][2]) + '</td>' \
                '<td class="data">' + str(stats["possibleWORST"][3]) + '</td>' \
                '<td class="data">' + str("%.2f" % (((stats["possibleWORST"][1] + stats["possibleWORST"][2] + stats["possibleWORST"][3])/float(45))*100)) + '%</td>' \
            '</tr>' \
            '<tr>' \
                '<td>' + str('Worst Possible') + '</td>' \
                '<td class="data">' + str(stats["WORSTCP"]) + '</td>' \
                '<td class="data">' + str(stats["WORSTHP"]) + '</td>' \
                '<td class="data">' + str(stats["WORST"][1]) + '</td>' \
                '<td class="data">' + str(stats["WORST"][2]) + '</td>' \
                '<td class="data">' + str(stats["WORST"][3]) + '</td>' \
                '<td class="data">0%</td>' \
            '</tr>'

    ivRowMarkup = Markup(ivRow)
    cpRowMarkup = Markup(cpRow)

    markups = {
        "ivSets": ivRowMarkup,
        "cpSets": cpRowMarkup
    }

    return markups 











