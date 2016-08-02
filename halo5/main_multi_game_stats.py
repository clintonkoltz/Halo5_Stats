from collections import Counter
import cPickle as pickle
import os

homedir = '/home/clinton/python/halo5'
if (os.getcwd() != homedir):
    os.chdir(homedir)

execfile("match_breakdown.py")

match_details = []

for file in os.listdir("./ProL_matches"):
    match_pickle = pickle.load( open("./ProL_matches/" + file, "rb") )
    match_details.append(match_pickle)

breakdown = []

for i in range( len(match_details) ):
    breakdown.append(match_details[i])

kills = Counter()
assists = Counter()
kills1 = Counter()
deaths = Counter()
deaths1 = Counter()

for i in range(  len(breakdown) ):
    kills += Counter(breakdown[i].get_total_kills())
    deaths += Counter(breakdown[i].get_total_deaths())
    assists += Counter(breakdown[i].get_total_assists())
    kills1 += Counter(breakdown[i].get_1v1_kills())
    deaths1 += Counter(breakdown[i].get_1v1_deaths())

alias = {   'HukE6': 'E6 Huke HCS',
            'bubu dubu': 'E6 bubu dubu',
            'Rayne nV': 'nV RayneHCS',
            'Peng': 'RNG Penguin HCS',
            'HAMY': 'RNG Commonly',
            'aPG': 'OG APG HCS',
            'SStelluR': 'TL StelluR',
            'Liquid Eco': 'TL Eco HCS',
            'Danoxide HCS' : 'TL Danoxide'
            }
for i in alias.keys():
    if (i in kills):
        kills[alias[i]]   += kills[i]
        kills1[alias[i]]  += kills1[i]
        deaths[alias[i]]  += deaths[i]
        deaths1[alias[i]] += deaths1[i]
        assists[alias[i]] += assists[i]

        del kills[i]
        del deaths[i]
        del kills1[i]
        del deaths1[i]
        del assists[i]

Player_names = [
            'CLG Royal 2',
            'CLG Frosty HCS',
            'CLG Snake Bite',
            'CLG LethuL HCS',

            'E6 Huke HCS',
            'E6 Shooter',
            'E6 Cratos HCS',
            'E6 bubu dubu',

            'nV Mikwen HCS',
            'nV eL ToWn',
            'nV RayneHCS',
            'nV Pistola HCS',

            'RNG Penguin HCS',
            'RNG Victory X',
            'RNG Ninja HCS',
            'RNG Commonly',

            'ALG RyaNoob',
            'ALG Heinz HCS',
            'ALGPredevonator',
            'ALG ContrA HCS',

            'EG SuspectorHCS',
            'EG Snip3downHCS',
            'EG Lunchbox HCS',
            'EG Roy HCS',

            'OG ACE HCS',
            'OG Str8 SickHCS',
            'OG Maniac HCS',
            'OG APG HCS',

            'TL Eco HCS',
            'TL StelluR',
            'TL Spartan HCS',
            'TL Danoxide',

            'Rammyy'
           ]

kd1 = dict()
battle_1v1_percent = dict()
k1_k = dict()
d1_d = dict()
kd_lone = dict()
events_1v1 = dict()
battles_1v1 = dict()
team_work = dict()
bat_1v1_game = dict()
kda = dict()

alg_games = 54
e6_games = 51
clg_games = 44
eg_games = 50
nv_games = 60
rng_games = 53
tl_games = 50
op_games = 45
ram_games = 16

for i in Player_names:
    kd1[i] = float(kills1[i]) / deaths1[i]
    battle_1v1_percent[i] = float((kills1[i] + deaths1[i])) / (kills[i] -
            kills1[i] + deaths[i] - deaths1[i] + assists[i])

    team_work[i] = float(kills[i]-kills1[i]+assists[i]) / (kills1[i] +
            deaths1[i] )
    events_1v1[i] = float(kills1[i] + deaths1[i]) / (kills[i] + deaths[i] -
            kills1[i] - deaths1[i] )

    k1_k[i] = float(kills1[i]) / kills[i]
    d1_d[i] = float(deaths1[i]) / deaths[i]
    battles_1v1[i] = (kills1[i] + deaths1[i])
    kda[i] = float(kills[i] + assists[i]/ 3.0) - deaths[i]
    if 'ALG' in i:
        if ( i == 'ALG RyaNoob'):
            bat_1v1_game[i] = battles_1v1[i] / float(alg_games-8)
            kda[i] = kda[i] / float(alg_games-8)
        elif ( i == 'ALG Heinz HCS' ):
            bat_1v1_game[i] = battles_1v1[i] / (float(alg_games)-22)
            kda[i] = kda[i] / (float(alg_games)-22)
        else:
            bat_1v1_game[i] = battles_1v1[i] / (float(alg_games))
            kda[i] = kda[i] / (float(alg_games))
    elif 'E6' in i:
        bat_1v1_game[i] = battles_1v1[i] / float(e6_games)
        kda[i] = kda[i] / float(e6_games)
    elif 'CLG' in i:
        if ( i != 'CLG Royal 2'):
            bat_1v1_game[i] = battles_1v1[i] / float(clg_games)
            kda[i] = kda[i] / float(clg_games)
        else:
            bat_1v1_game[i] = battles_1v1[i] / (float(clg_games)-8)
            kda[i] = kda[i] / (float(clg_games)-8)
    elif 'EG' in i:
        bat_1v1_game[i] = battles_1v1[i] / float(eg_games)
        kda[i] = kda[i] / float(eg_games)
    elif 'nV' in i:
        bat_1v1_game[i] = battles_1v1[i] / float(nv_games)
        kda[i] = kda[i] / float(nv_games)
    elif 'RNG' in i:
        bat_1v1_game[i] = battles_1v1[i] / float(rng_games)
        kda[i] = kda[i] / float(rng_games)
    elif 'TL' in i:
        if ( i != 'TL Danoxide'):
            bat_1v1_game[i] = battles_1v1[i] / float(tl_games)
            kda[i] = kda[i] / float(tl_games)
        else:
            bat_1v1_game[i] = battles_1v1[i] / float(tl_games-11)
            kda[i] = kda[i] / float(tl_games-11)
    elif 'OG' in i:
        bat_1v1_game[i] = battles_1v1[i] / float(op_games)
        kda[i] = kda[i] / float(op_games)
    elif 'Rammyy' in i:
        bat_1v1_game[i] = battles_1v1[i] / float(ram_games)
        kda[i] = kda[i] / float(ram_games)

