def team_check(match_players):

    team1 = 'None'
    team2 = 'None'

    Teams = {

        'clg' : [
                'CLG Royal 2',
                'CLG Frosty HCS',
                'CLG Snake Bite',
                'CLG LethuL HCS' ],
        'clgr': [
                'CLG Frosty HCS',
                'CLG Snake Bite',
                'Rammyy',
                'CLG LethuL HCS' ],
        'e6'  : [
                'E6 Huke HCS',
                'HukE6',
                'E6 Shooter',
                'E6 Cratos HCS',
                'bubu dubu',
                'E6 bubu dubu' ],
        'nv'  : [
                'nV Mikwen HCS',
                'nV eL ToWn',
                'nV RayneHCS',
                'Rayne nV',
                'nV Pistola HCS' ],
        'rng' : [
                'RNG Penguin HCS',
                'Peng',
                'RNG Victory X',
                'RNG Ninja HCS',
                'HAMY',
                'RNG Commonly' ],
        'alg' : [
                'ALG RyaNoob',
                'ALG Heinz HCS',
                'ALGPredevonator',
                'ALG Goofy HCS',
                'ALG ContrA HCS'],
        'algr': [
                'ALG Heinz HCS',
                'ALGPredevonator',
                'Rammyy',
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
                'aPG',
                'OG APG HCS' ],
        'tl'  : [
                'TL Eco HCS',
                'Liquid Eco',
                'TL StelluR',
                'SStelluR',
                'TL Spartan HCS',
                'Danoxide HCS',
                'TL Assault HCS',
                'TL Danoxide' ]
        }


    for i in Teams.keys():
        if ( len( set(Teams[i]).intersection(match_players) ) == 4 ):
            if ( team1 == 'None' ):
                team1 = i
            else:
                team2 = i

    return [team1, team2]
