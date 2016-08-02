import requests, json

apikey = "2336650f744d485481c99a91b6d0c7b5"

class Halo5(object):

    def __init__(self, api_key):

        self.api_key = api_key # "2336650f744d485481c99a91b6d0c7b5"
        self.root_url = "https://www.haloapi.com/stats/h5"

    def _haloapi_request(self, url, params=None):

        headers = {'Ocp-Apim-Subscription-Key': self.api_key}
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response

    def player_stats(self, player, seasonId=None):

        url = "{root}/servicerecords/arena?players={players}".format(
                root=self.root_url,
                players=player,
                )
        response = self._haloapi_request(url)
        return response.json()

    def player_matches(self, player, modes=None, start=None, count=None):

        url = "{root}/players/{players}/matches".format(
                root=self.root_url,
                players=player,
                )

        params = dict()
        if (start is not None):
            params['start'] = start
        if (count is not None):
            params['count'] = count
        if (modes is not None):
            params['modes'] = modes

        response = self._haloapi_request(url,params=params)
        return response.json()

    def player_match_ids(self, player, modes=None, start=None, count=None):

        url = "{root}/players/{players}/matches".format(
                root=self.root_url,
                players=player,
                )
        params = dict()
        if (start is not None):
            params['start'] = start
        if (count is not None):
            params['count'] = count
        if (modes is not None):
            params['modes'] = modes

        response = self._haloapi_request(url,params=params)
        response = response.json()
        matchIds = []

        for i in range(len(response['Results'])):
            matchIds.append(response['Results'][i]['Id']['MatchId'])

        return matchIds

    # matchIds are found in player_matches
    # matches['Results'][i]['Id]['MatchId']
    def match_details(self, matchId):

        url = '{root}/matches/{matchId}/events'.format(
                root=self.root_url,
                matchId=matchId
                )
        response = self._haloapi_request(url)
        return response.json()
