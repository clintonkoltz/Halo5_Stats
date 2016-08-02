import matplotlib.mlab as mlab
import numpy as np


teams= {

        'clg' : [
                'CLG Royal 2',
                'CLG Frosty HCS',
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
                'TL Spartan HCS',
                'TL Danoxide' ]
        }

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

def team_histogram(stats, stat_name, team_name):

    mu = {}
    sigma = {}
    y = {}
    f, axarr = plt.subplots(2, 2)

    for i in range(4):
        mu[i] = np.mean(    stats[teams[team_name][i]][stat_name] )
        sigma[i] = np.std(  stats[teams[team_name][i]][stat_name] )

    n, bins, patches = axarr[0,0].hist(stats[teams[team_name][0]][stat_name] )
    axarr[0,0].set_title('{}  Average:{} Std:{}'.format(
        teams[team_name][0], round(mu[0],2), round(sigma[0],2)) )

    n, bins, patches = axarr[0,1].hist(stats[teams[team_name][1]][stat_name] )
    axarr[0,1].set_title('{}  Average:{} Std:{}'.format(
        teams[team_name][1], round(mu[1],2), round(sigma[1],2)) )

    n, bins, patches = axarr[1,0].hist(stats[teams[team_name][2]][stat_name] )
    axarr[1,0].set_title('{}  Average:{} Std:{}'.format(
        teams[team_name][2], round(mu[2],2), round(sigma[2],2)) )

    n, bins, patches = axarr[1,1].hist(stats[teams[team_name][3]][stat_name] )
    axarr[1,1].set_title('{}  Average:{} Std:{}'.format(
        teams[team_name][3], round(mu[3],2), round(sigma[3],2)) )

    plt.suptitle("KDA")
    plt.show()
