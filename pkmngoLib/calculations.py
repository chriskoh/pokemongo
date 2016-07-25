#!usr/bin/env python3

# calculateStats.py
# calculate various stats based on IVs (x3 variable range 0-15) and ECpM (Exact CP Modifier, static variable changes based on pokemon level)

import math
import json

def calcStats(baseAttack, baseDefense, baseStamina, level):

    # load "CP Modifier" as cpm static variables
    with open('/home/crees/pkmngo/data/cpm.json') as data_file:
        cpm = json.load(data_file)

    # calculate "Additional CP Modifier" (acpm), difference between two CPMs after upgrading
    if int(level) < 40:
        acpm = cpm[str(int(level) + 1)]["CpM"] - cpm[level]["CpM"]
    else:
        acpm = 0

    # Excact CP Modifier (ecpm)
    ecpm = cpm[level]["CpM"] + acpm

    # Calculate MIN/MAX
    minAttack = (baseAttack + 0) * ecpm
    minDefense = (baseDefense + 0) * ecpm
    minStamina = (baseStamina + 0) * ecpm

    maxAttack = (baseAttack + 15) * ecpm
    maxDefense = (baseDefense + 15) * ecpm
    maxStamina = (baseStamina + 15) * ecpm

    stats = {
        "ecpm": ecpm,
        "minAttack": minAttack,
        "minDefense": minDefense,
        "minStamina": minStamina,
        "maxAttack": maxAttack,
        "maxDefense": maxDefense,
        "maxStamina": maxStamina,
        "minHP": int(math.floor(minStamina)),
        "maxHP": int(math.floor(maxStamina)),
        "minCP": int(max(10,math.floor(math.pow(minStamina,0.5) * minAttack * math.pow(minDefense,0.5) / 10))),
        "maxCP": int(max(10,math.floor(math.pow(maxStamina,0.5) * maxAttack * math.pow(maxDefense,0.5) / 10)))
    }    

    return stats
