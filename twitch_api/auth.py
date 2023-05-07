import requests

class TwitchAuthenticate():
    def __init__(self, client_id, client_secret, auth_url='https://id.twitch.tv/oauth2/token'):
        self.client_id = client_id
        self.client_secret = client_secret
        self.auth_url = auth_url
        self.access_token = None 


    def authenticate_api(self):
        params={'client_id':self.client_id,
                'client_secret':self.client_secret,
                'grant_type':'client_credentials'}
        
        response = requests.post(self.auth_url, params=params)

        try:
            data = response.json()
            self.access_token = data['access_token']
            print('Authenticated In Twitch API')
        except (ValueError, KeyError):
            raise ValueError('Invalid API response')
        

    def validate_bearer_token(self, validate_url='https://id.twitch.tv/oauth2/validate'):
        if self.access_token: 
            self.bearer_token = f'Bearer {self.access_token}'
            headers = {'Authorization':self.bearer_token}
            validate = requests.get(validate_url, headers=headers)
            if validate.status_code == 200:
                print('Validated Bearer Token')
                return self.bearer_token       
        else:
            print('Authentication Required')