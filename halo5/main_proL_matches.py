import time
import cPickle as pickle
import numpy as np

homedir = '/home/clinton/python/halo5'

players = [
                'CLG Royal 2',
                'CLG Frosty HCS',
                'CLG Snake Bite',
                'CLG LethuL HCS' ,
                'Rammyy',
                'E6 Huke HCS',
                'E6 Shooter',
                'E6 Cratos HCS',
                'E6 bubu dubu' ,
                'nV Mikwen HCS',
                'nV eL ToWn',
                'nV RayneHCS',
                'nV Pistola HCS' ,
                'RNG Penguin HCS',
                'RNG Victory X',
                'RNG Ninja HCS',
                'RNG Commonly' ,
                'ALG RyaNoob',
                'ALG Heinz HCS',
                'ALGPredevonator',
                'ALG ContrA HCS',
                'ALG Goofy HCS' ,
                'EG SuspectorHCS',
                'EG Snip3downHCS',
                'EG Lunchbox HCS',
                'EG Roy HCS' ,
                'OG ACE HCS',
                'OG Str8 SickHCS',
                'OG Maniac HCS',
                'OG APG HCS' ,
                'TL Eco HCS',
                'TL StelluR',
                'TL Spartan HCS',
                'TL Danoxide'
          ]

execfile('Halo5.py')
execfile('match_breakdown.py')
execfile('get_map_gtype.py')
execfile('team_check.py')

h = Halo5(apikey)


matches = np.array([['a','a','a','a']])

for i in players:

    match_results =  h.player_matches(i, modes='custom', start = 25)
    time.sleep(1)

    for j in np.array(match_results['Results']):
        try:
            append = np.append( np.array(get_map_gtype(j)),
                                            np.array(j['Id']['MatchId']) )
            matches = np.append(matches, [append], axis=0 )
        except:
            pass

matches = np.delete(matches, 0, axis=0)
uniques = np.vstack( {tuple(row) for row in matches} )

match_details = []

for i in range( len(uniques) ):
    match_details.append( h.match_details(uniques[i,3]) )
    time.sleep(1)

breakdown = []

for i in range( len(match_details) ):
    breakdown.append( match_breakdown(match_details[i]) )

teams = []

for i in range( len(breakdown) ):
    teams.append( team_check(breakdown[i].get_total_deaths().keys()) )

games = []
for i in range(len(teams)):
    if (teams[i][1] != 'None'):
        games.append([uniques[i],teams[i],breakdown[i]])

os.chdir('./ProL_matches')

for i in range( len(games) ):
    date = games[i][0][0]
    map_name = games[i][0][1]
    gtype = games[i][0][2]
    match_id = games[i][0][3]
    bd = games[i][2]
    team1 = games[i][1][0]
    team2 = games[i][1][1]
    fname = '{}_{}_vs_{}_{}_{}'.format(date, team1, team2, map_name, gtype)
    pickle.dump(bd,open(fname, "w+"))

os.chdir(homedir)
