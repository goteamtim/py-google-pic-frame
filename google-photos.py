import requests

class google_photos():
    def __init__(self,api_key):
        self.base_url = 'https://photoslibrary.googleapis.com/v1/'
        self.api_key = api_key
    
    def get_album_list():
        # Returns a dictionary of album names/URLs?  Maybe see what else the API grants access to
        return []