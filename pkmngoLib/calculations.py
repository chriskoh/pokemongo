#!usr/bin/env python3

# calculateStats.py
# calculate various stats based on IVs (x3 variable range 0-15) and ECpM (Exact CP Modifier, static variable changes based on pokemon level)

import math
import json
import urllib

def calcEvolveStats(baseAttack, baseDefense, baseStamina, name, possibleBEST, possibleWORST):

    # load "CP Modifier" as cpm static variables
    response = urllib.urlopen('http://chriskoh.io/static/cpm.json')
    cpm = json.load(response)

    BEST = ["40.5", 15, 15, 15, 100]
    WORST = ["40.5", 0, 0, 0, 0]

    BESTCP = int(max(10,math.floor((baseAttack + BEST[1]) * math.pow((baseDefense + BEST[2]),0.5) * math.pow((baseStamina + BEST[3]),0.5) * math.pow((cpm["40.5"]["CpM"]),2) / 10)))
    WORSTCP = int(max(10,math.floor((baseAttack + WORST[1]) * math.pow((baseDefense + WORST[2]),0.5) * math.pow((baseStamina + WORST[3]),0.5) * math.pow((cpm["40.5"]["CpM"]),2) / 10)))
    possibleBESTCP = int(max(10,math.floor((baseAttack + possibleBEST[1]) * math.pow((baseDefense + possibleBEST[2]),0.5) * math.pow((baseStamina + possibleBEST[3]),0.5) * math.pow((cpm["40.5"]["CpM"]),2) / 10)))
    possibleWORSTCP = int(max(10,math.floor((baseAttack + possibleWORST[1]) * math.pow((baseDefense + possibleWORST[2]),0.5) * math.pow((baseStamina + possibleWORST[3]),0.5) * math.pow((cpm["40.5"]["CpM"]),2) / 10)))

    BESTHP = int(cpm["40.5"]["CpM"] * (baseStamina + BEST[3]))
    WORSTHP = int(cpm["40.5"]["CpM"] * (baseStamina + WORST[3]))
    possibleBESTHP = int(cpm["40.5"]["CpM"] * (baseStamina + possibleBEST[3]))
    possibleWORSTHP = int(cpm["40.5"]["CpM"] * (baseStamina + possibleWORST[3]))

    stats = {
        "possibleBEST": possibleBEST,
        "possibleWORST": possibleWORST,
        "possibleBESTCP": possibleBESTCP,
        "possibleWORSTCP": possibleWORSTCP,
        "BEST": BEST,
        "WORST": WORST,
        "BESTCP": BESTCP,
        "WORSTCP": WORSTCP,
        "BESTHP": BESTHP,
        "WORSTHP": WORSTHP,
        "possibleBESTHP": possibleBESTHP,
        "possibleWORSTHP": possibleWORSTHP
    }    

    return stats

def calcStats(baseAttack, baseDefense, baseStamina, cp, hp, dust):

    # load "CP Modifier" as cpm static variables
    response = urllib.urlopen('http://chriskoh.io/static/cpm.json')
    cpm = json.load(response)

    response = urllib.urlopen('http://chriskoh.io/static/upgrade.json')
    upgrade = json.load(response)

    levels = upgrade[dust]["level"]

    BEST = ["40.5", 15, 15, 15, 100]
    WORST = ["40.5", 0, 0, 0, 0]
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

    BESTCP = 1
    WORSTCP = 1
    BESTCP = int(max(10,math.floor((baseAttack + BEST[1]) * math.pow((baseDefense + BEST[2]),0.5) * math.pow((baseStamina + BEST[3]),0.5) * math.pow((cpm["40.5"]["CpM"]),2) / 10)))
    WORSTCP = int(max(10,math.floor((baseAttack + WORST[1]) * math.pow((baseDefense + WORST[2]),0.5) * math.pow((baseStamina + WORST[3]),0.5) * math.pow((cpm["40.5"]["CpM"]),2) / 10)))
    possibleBESTCP = int(max(10,math.floor((baseAttack + possibleBEST[1]) * math.pow((baseDefense + possibleBEST[2]),0.5) * math.pow((baseStamina + possibleBEST[3]),0.5) * math.pow((cpm["40.5"]["CpM"]),2) / 10)))
    possibleWORSTCP = int(max(10,math.floor((baseAttack + possibleWORST[1]) * math.pow((baseDefense + possibleWORST[2]),0.5) * math.pow((baseStamina + possibleWORST[3]),0.5) * math.pow((cpm["40.5"]["CpM"]),2) / 10)))

    BESTHP = int(cpm["40.5"]["CpM"] * (baseStamina + BEST[3]))
    WORSTHP = int(cpm["40.5"]["CpM"] * (baseStamina + WORST[3]))
    possibleBESTHP = int(cpm["40.5"]["CpM"] * (baseStamina + possibleBEST[3]))
    possibleWORSTHP = int(cpm["40.5"]["CpM"] * (baseStamina + possibleWORST[3]))

    bestChart = ''
    possibleChart = ''
    for cpmval in range(1, 41):

        level = str(cpmval)
        halflevel = str(cpmval + 0.5)

        BESTCPChart = int(max(10,math.floor((baseAttack + BEST[1]) * math.pow((baseDefense + BEST[2]),0.5) * math.pow((baseStamina + BEST[3]),0.5) * math.pow((cpm[level]["CpM"]),2) / 10)))
        WORSTCPChart = int(max(10,math.floor((baseAttack + WORST[1]) * math.pow((baseDefense + WORST[2]),0.5) * math.pow((baseStamina + WORST[3]),0.5) * math.pow((cpm[level]["CpM"]),2) / 10)))
        BESThalfCPChart = int(max(10,math.floor((baseAttack + BEST[1]) * math.pow((baseDefense + BEST[2]),0.5) * math.pow((baseStamina + BEST[3]),0.5) * math.pow((cpm[halflevel]["CpM"]),2) / 10)))
        WORSThalfCPChart = int(max(10,math.floor((baseAttack + WORST[1]) * math.pow((baseDefense + WORST[2]),0.5) * math.pow((baseStamina + WORST[3]),0.5) * math.pow((cpm[halflevel]["CpM"]),2) / 10)))
        
        possibleBESTCPChart = int(max(10,math.floor((baseAttack + possibleBEST[1]) * math.pow((baseDefense + possibleBEST[2]),0.5) * math.pow((baseStamina + possibleBEST[3]),0.5) * math.pow((cpm[level]["CpM"]),2) / 10)))
        possibleWORSTCPChart = int(max(10,math.floor((baseAttack + possibleWORST[1]) * math.pow((baseDefense + possibleWORST[2]),0.5) * math.pow((baseStamina + possibleWORST[3]),0.5) * math.pow((cpm[level]["CpM"]),2) / 10)))
        possibleBESThalfCPChart = int(max(10,math.floor((baseAttack + possibleBEST[1]) * math.pow((baseDefense + possibleBEST[2]),0.5) * math.pow((baseStamina + possibleBEST[3]),0.5) * math.pow((cpm[halflevel]["CpM"]),2) / 10)))
        possibleWORSThalfCPChart = int(max(10,math.floor((baseAttack + possibleWORST[1]) * math.pow((baseDefense + possibleWORST[2]),0.5) * math.pow((baseStamina + possibleWORST[3]),0.5) * math.pow((cpm[halflevel]["CpM"]),2) / 10)))

        BESTlevelstr = "{x:" + str(level) + ", y:[" + str(WORSTCPChart) + ", " + str(BESTCPChart) + "]},"
        BESThalflevelstr = "{x:" + str(halflevel) + ", y:[" + str(WORSTCPChart) + ", " + str(BESTCPChart) + "]},"
        possiblelevelstr = "{x:" + str(level) + ", y:[" + str(possibleWORSTCPChart) + ", " + str(possibleBESTCPChart) + "]},"
        possiblehalflevelstr = "{x:" + str(halflevel) + ", y:[" + str(possibleWORSTCPChart) + ", " + str(possibleBESTCPChart) + "]},"

        bestChart += BESTlevelstr
        bestChart += BESThalflevelstr
        possibleChart += possiblelevelstr
        possibleChart += possiblehalflevelstr

    stats = {
        "levels": levels,
        "possible": possibleHP,
        "possibleSET": possibleSET,
        "possibleBEST": possibleBEST,
        "possibleWORST": possibleWORST,
        "pctPerfect": pctPerfect,
        "possibleBESTCP": possibleBESTCP,
        "possibleWORSTCP": possibleWORSTCP,
        "BEST": BEST,
        "WORST": WORST,
        "BESTCP": BESTCP,
        "WORSTCP": WORSTCP,
        "BESTHP": BESTHP,
        "WORSTHP": WORSTHP,
        "possibleBESTHP": possibleBESTHP,
        "possibleWORSTHP": possibleWORSTHP,
        "bestChart": bestChart,
        "possibleChart": possibleChart
    }    

    return stats
