#!usr/bin/env python3

# calculateStats.py
# calculate various stats based on IVs (x3 variable range 0-15) and ECpM (Exact CP Modifier, static variable changes based on pokemon level)

import math
import json

def calcStats(baseAttack, baseDefense, baseStamina, cp, hp, dust):

    # load "CP Modifier" as cpm static variables
    with open('/home/crees/pkmngo/data/cpm.json') as data_file:
        cpm = json.load(data_file)

    with open('/home/crees/pkmngo/data/upgrade.json') as data_file:
        upgrade = json.load(data_file)

    levels = upgrade[dust]["level"]

    possibleSET = []
    possibleBEST = ''
    possibleWORST = ''
    for lvl in levels:
        possibleHP = []
        for iv in range(16):
            test = max(10,math.floor((baseStamina + iv) * cpm[str(lvl)]["CpM"]))
            if int(hp) == int(test):
               possibleHP.append(iv)
        for ivHP in possibleHP:
            for ivSTR in range(16):
                for ivDEF in range(16):
                    test = max(10,math.floor((baseAttack + ivSTR) * math.pow((baseDefense + ivDEF),0.5) * math.pow((baseStamina + ivHP),0.5) * math.pow((cpm[str(lvl)]["CpM"]),2) / 10))
                    ivPCT = (ivSTR + ivDEF + ivHP)/float(45)
                    ivPCT = round(float(ivPCT) * 100,2)
                    currentSET = [lvl, ivSTR, ivDEF, ivHP, ivPCT]
                    if int(cp) == int(test):
                        possibleSET.append(currentSET)
                        if possibleBEST == '':
                            possibleBEST = currentSET
                            possibleWORST = currentSET
                        else:
                            if float(currentSET[4]) > float(possibleBEST[4]):
                                possibleBEST = currentSET
                            if float(currentSET[4]) < float(possibleWORST[4]):
                                possibleWORST = currentSET

    pctPerfect = 0
    for ivSet in possibleSET:
        pctPerfect += float(ivSet[4])
    pctPerfect /= len(possibleSET)

#    # Calculate MIN/MAX
#    minAttack = (baseAttack + 0) * ecpm
#    minDefense = (baseDefense + 0) * ecpm
#    minStamina = (baseStamina + 0) * ecpm

#    maxAttack = (baseAttack + 15) * ecpm
#    maxDefense = (baseDefense + 15) * ecpm
#    maxStamina = (baseStamina + 15) * ecpm

    stats = {
        "levels": levels,
        "possible": possibleHP,
        "possibleSET": possibleSET,
        "possibleBEST": possibleBEST,
        "possibleWORST": possibleWORST,
        "pctPerfect": pctPerfect
#        "ecpm": ecpm,
#        "minAttack": minAttack,
#        "minDefense": minDefense,
#        "minStamina": minStamina,
#        "maxAttack": maxAttack,
#        "maxDefense": maxDefense,
#        "maxStamina": maxStamina,
#        "minHP": int(math.floor(minStamina)),
#        "maxHP": int(math.floor(maxStamina)),
#        "minCP": int(max(10,math.floor(math.pow(minStamina,0.5) * minAttack * math.pow(minDefense,0.5) / 10))),
#        "maxCP": int(max(10,math.floor(math.pow(maxStamina,0.5) * maxAttack * math.pow(maxDefense,0.5) / 10)))
    }    

    return stats
