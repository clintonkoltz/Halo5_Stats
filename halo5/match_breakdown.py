import numpy as np

class match_breakdown(object):

    def __init__(self, details):
        self.details = details

    def get_kill_events(self):

        # Gives a list of GameEvents where someone died 

        kill_events = []
        for i in range(len(self.details['GameEvents'])):
            if (self.details['GameEvents'][i]['EventName'] == 'Death'):
                kill_events.append(self.details['GameEvents'][i])
        return kill_events

    def get_kill_list(self):

        # Gives chronilogically ordered list of name of thoses who got kills

        kill_events = self.get_kill_events()
        kills = []

        for i in range( len( kill_events) ):

        # Catches when a suicide happens and there is no Killer
            if ( kill_events[i]['Killer'] == None ):
                kill_events[i]['Killer'] = {'Gamertag': 'None' }
            kills.append( kill_events[i]['Killer']['Gamertag'] )

        return kills

    def get_death_list(self):

        # Gives chronilogically ordered list of name of thoses died

        kill_events = self.get_kill_events()
        deaths= []

        for i in range( len( kill_events) ):

        # Catches when strange event happends where No one Died
            if ( kill_events[i]['Victim'] == None ):
                kill_events[i]['Victim'] = {'Gamertag': 'None' }
            deaths.append( kill_events[i]['Victim']['Gamertag'] )

        return deaths

    def get_assist_list(self):

        # Gives chronilogically ordered list people who assisted kills

        kill_events = self.get_kill_events()
        assistants = []
        assists= []

        for i in range( len( kill_events) ):

            for j in range( len( kill_events[i]['Assistants'] ) ):

                assistants.append( kill_events[i]['Assistants'][j]['Gamertag'] )

            assists.append(assistants)
            assistants = []

        return assists
    def get_total_kills(self):

        kills = self.get_kill_list()
        deaths = self.get_death_list()
        total_kills = {}
        players = set(kills).difference(set(['None']))

        for i in players:
            total_kills[i] = 0

        for i in range( len(kills) ):
            if ( deaths[i] != 'None' ):
                try:
                    total_kills[kills[i]] = total_kills[kills[i]] + 1
                except:
                    pass

        return total_kills

    def get_total_deaths(self):

        deaths = self.get_death_list()
        kills = self.get_kill_list()
        total_deaths = {}
        players = set(deaths).difference(set(['None']))

        for i in players:
            total_deaths[i] = 0

        for i in range( len(deaths) ):
            if ( kills[i] != 'None'):
                try:
                    total_deaths[deaths[i]] = total_deaths[deaths[i]] + 1
                except:
                    pass

        return total_deaths

    def get_total_assists(self):

        assists = self.get_assist_list()
        deaths = self.get_death_list()
        total_assists = {}
        players = set(deaths)
        a_list = np.array([])

        for i in players:
            total_assists[i] = 0

        for i in assists:
            a_list = np.append(a_list,i)

        for i in a_list:
            total_assists[i] = total_assists[i] + 1

        return total_assists

    def get_kill_position(self):

        # Give [x, y, z] coordinates of where kills occured

        kill_zone = []
        kill_events = self.get_kill_events()

        for i in range( len(kills) ):
            kill_zone.append( [ kill_events[i]['KillerWorldLocation']['x'],
                                kill_events[i]['KillerWorldLocation']['y'],
                                kill_events[i]['KillerWorldLocation']['z'] ] )

        return kill_zone

    def get_death_position(self):

        # Give [x, y, z] coordinates of where deaths occured

        death_zone = []
        kill_events = self.get_kill_events()

        for i in range( len(kills) ):
            death_zone.append( [ kill_events[i]['VictimWorldLocation']['x'],
                                 kill_events[i]['VictimWorldLocation']['y'],
                                 kill_events[i]['VictimWorldLocation']['z'] ] )

        return death_zone

    def get_1v1_kills(self):

        # Give amount of unassisted kills for each player

        kills = self.get_kill_list()
        death = self.get_death_list()
        assists = self.get_assist_list()
        players = np.unique(kills)
        kills_1v1 = {}

        for i in  players:
            kills_1v1[i] = 0

        for i in range( len(kills) ):
            if ( assists[i] == [] ):
                if( death[i] != 'None' ):
                    kills_1v1[kills[i]] = kills_1v1[kills[i]] + 1

        try:
            del kills_1v1['None']
        except:
            pass

        return kills_1v1


    def get_1v1_deaths(self):

        # Give amount of unassisted deaths for each player
        deaths = self.get_death_list()
        kills = self.get_kill_list()
        assists = self.get_assist_list()
        players = np.unique(deaths)
        deaths_1v1 = {}

        for i in  players:
            deaths_1v1[i] = 0

        for i in range( len(deaths) ):
            if ( assists[i] == [] ):
                if ( kills[i] != 'None' ):
                    deaths_1v1[deaths[i]] = deaths_1v1[deaths[i]] + 1

        try:
            del deaths_1v1['None']
        except:
            pass

        return deaths_1v1


    def get_spawn_order(self):

        # Gives inital spawning order and difference is spawn times
        # only get the first 8 spawns

        all_spawns = []
        spawn_times = {}

        for i in range( len(self.details["GameEvents"]) ):
            if ( self.details['GameEvents'][i]['EventName'] == 'PlayerSpawn' ):
               all_spawns.append( self.details['GameEvents'][i] )

        initial_time = float( all_spawns[0]['TimeSinceStart'][2:-1] )
        for i in range(0,8):
            spawn_times[all_spawns[i]['Player']['Gamertag']] = \
                    float(all_spawns[i]['TimeSinceStart'][2:-1]) - initial_time
        return spawn_times

    def get_spawn_v_1v1_kd(self):

        spawns = self.get_spawn_order()
        kills = self.get_1v1_kills()
        deaths = self.get_1v1_deaths()
        svkd = {}

        for i in spawns.keys():
            try:
                svkd[i] = [spawns[i], float(kills[i])/deaths[i] ]
            except:
                pass

        return svkd


