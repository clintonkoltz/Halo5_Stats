import cPickle as pickle
import numpy as np
import os

execfile("match_breakdown.py")

match_details = []

teams= {

        'clg' : [
                'CLG Royal 2',
                'CLG Frosty HCS',
                'Rammyy',
                'CLG Snake Bite',
                'CLG LethuL HCS' ],
        'e6'  : [
                'E6 Huke HCS',
                'E6 Shooter',
                'E6 Cratos HCS',
                'E6 bubu dubu' ],
        'nv'  : [
                'nV Mikwen HCS',
                'nV eL ToWn',
                'nV RayneHCS',
                'nV Pistola HCS' ],
        'rng' : [
                'RNG Penguin HCS',
                'RNG Victory X',
                'RNG Ninja HCS',
                'RNG Commonly' ],
        'alg' : [
                'ALG RyaNoob',
                'ALG Goofy HCS',
                'ALG Heinz HCS',
                'ALGPredevonator',
                'ALG ContrA HCS'],
        'eg'  : [
                'EG SuspectorHCS',
                'EG Snip3downHCS',
                'EG Lunchbox HCS',
                'EG Roy HCS' ],
        'op'  : [
                'OG ACE HCS',
                'OG Str8 SickHCS',
                'OG Maniac HCS',
                'OG APG HCS' ],
        'tl'  : [
                'TL Eco HCS',
                'TL StelluR',
                'TL Assault HCS',
                'TL Spartan HCS',
                'None',
                'TL Danoxide' ]
        }

# Create nested dictionary to hold stats per player per game
per_game_stats = dict()
for team_name in teams.keys():
    for player in teams[team_name]:
        per_game_stats[player] = { 'kills':np.array([]), 'deaths':np.array([]),
                'kills1':np.array([]), 'deaths1':np.array([]),
                'assists':np.array([]), 'kda':np.array([]),
                'kd':np.array([]),'kd1':np.array([]) }

for file in os.listdir("./ProL_matches"):
    match_pickle = pickle.load( open("./ProL_matches/" + file, "rb") )
    match_details.append(match_pickle)

breakdown = []

for i in range( len(match_details) ):
    breakdown.append(match_details[i])

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

for bd in breakdown:
    kills = bd.get_total_kills()
    kills1 = bd.get_1v1_kills()
    deaths = bd.get_total_deaths()
    deaths1 = bd.get_1v1_deaths()
    assists = bd.get_total_assists()

    for i in alias.keys():
        if (i in kills):
            kills[alias[i]]   = kills[i]
            kills1[alias[i]]  = kills1[i]
            deaths[alias[i]]  = deaths[i]
            deaths1[alias[i]] = deaths1[i]
            assists[alias[i]] = assists[i]

            del kills[i]
            del deaths[i]
            del kills1[i]
            del deaths1[i]
            del assists[i]

    for i in kills:
        per_game_stats[i]['kills'] = np.append(per_game_stats[i]['kills'],kills[i])

        try:
            kd = float( kills[i] ) / deaths[i]
        except:
            kd = float( kills[i] )
        per_game_stats[i]['kd'] = np.append(per_game_stats[i]['kd'],kd)

        kda = kills[i] + (assists[i]/3.0) - deaths[i]
        per_game_stats[i]['kda'] = np.append(per_game_stats[i]['kda'],kda)

    for i in kills1:
        per_game_stats[i]['kills1'] = \
            np.append(per_game_stats[i]['kills1'],kills1[i])

        try:
            kd1 = float( kills1[i] ) / deaths1[i]
        except:
            kd1 = float( kills1[i] )
        per_game_stats[i]['kd1'] = \
            np.append(per_game_stats[i]['kd1'],kd1)

    for i in deaths:
        per_game_stats[i]['deaths'] = \
            np.append(per_game_stats[i]['deaths'],deaths[i])

    for i in deaths1:
        per_game_stats[i]['deaths1'] = \
            np.append(per_game_stats[i]['deaths1'],deaths1[i])

    for i in assists:
        per_game_stats[i]['assists'] = \
            np.append(per_game_stats[i]['assists'],assists[i])



def get_team(player_name):
    if   ('TL' in player_name):
        team_name = 'tl'
    elif ('ALG' in player_name):
        team_name = 'alg'
    elif ('CLG' in player_name):
        team_name = 'clg'
    elif ('E6' in player_name):
        team_name = 'e6'
    elif ('EG' in player_name):
        team_name = 'eg'
    elif ('nV' in player_name):
        team_name = 'nv'
    elif ('RNG' in player_name):
        team_name = 'rng'
    elif ('OG' in player_name):
        team_name = 'op'

    return team_name
