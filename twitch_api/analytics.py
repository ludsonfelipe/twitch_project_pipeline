import requests

class TwitchAnalytics():
    API_URL = 'https://api.twitch.tv/helix'
    ENDPOINT_GAMES = '/games/top'
    ENDPOINT_STREAMS = '/streams'
    ENDPOINT_CHANNELS = '/channels'
    ENDPOINT_FOLLOWERS = '/followers'
    ENDPOINT_USERS_FOLLOWS = '/users/follows'
    ENDPOINT_USERS = '/users'
    
    def __init__(self, bearer_token, client_id):
        self.client_id = client_id
        self.bearer_token = bearer_token
        self.headers = {'Authorization': self.bearer_token,
                        'Client-Id': self.client_id}

    def _create_params(self, **kwargs):
        params = {}
        for key, value in kwargs.items():
            if value is not None:
                params[key] = value
        return params

    def _make_request(self, endpoint, params=None):
        url = f"{self.API_URL}{endpoint}"
        response = requests.get(url, params=params, headers=self.headers)
        if response.status_code != 200:
            raise ValueError(f"Request failed with status code {response.status_code}")
        return response.json()

    def get_top_games(self, first=100, after=None, before=None):
        
        params = self._create_params(
            first=first, 
            after=after, 
            before=before
            )
        
        return self._make_request(self.ENDPOINT_GAMES, params=params)

    def get_streams(self, game_id='509658', user_login=None, live='all', first=100, after=None, before=None):

        params = self._create_params(
            game_id=game_id, 
            user_login=user_login, 
            live=live, 
            first=first, 
            after=after, 
            before=before
            )

        return self._make_request(self.ENDPOINT_STREAMS, params=params)

    def get_stream_info(self, broadcaster_id=''):

        params = self._create_params(
            broadcaster_id=broadcaster_id
            )

        return self._make_request(f"{self.ENDPOINT_CHANNELS}", params=params)

    def get_stream_followers(self, broadcaster_id='', user_id=None, first=100, after=None):

        params = self._create_params(
            broadcaster_id=broadcaster_id, 
            user_id=user_id, 
            first=first, 
            after=after 
            )

        return self._make_request(f"{self.ENDPOINT_CHANNELS}{self.ENDPOINT_FOLLOWERS}", params=params)

    def get_user_followers(self, from_id=None, to_id=None, first=100, after=None):

        params = self._create_params(
            from_id=from_id, 
            to_id=to_id, 
            first=first, 
            after=after
            )
        return self._make_request(self.ENDPOINT_USERS_FOLLOWS, params=params)

    def get_user(self, id_user=None, login=None):
        params = self._create_params(
            id_user=id_user,
            login=login
            )
        return self._make_request(self.ENDPOINT_USERS, params=params)
