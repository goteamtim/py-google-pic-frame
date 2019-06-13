import requests
import json
import credentials as creds
import time
import threading
# https://accounts.google.com/o/oauth2/device/code  Call this URL to get a device to show the user.
class google_photos(object):
    base_photos_url = 'https://photoslibrary.googleapis.com/v1/'
    def __init__(self,api_key):
        self.api_key = api_key
        self.c = creds.credentials()
    # AUTH
    def login(self):
        # credentials = gce.AppAssertionCredentials(
        #     scope='https://www.googleapis.com/auth/devstorage.read_write')
        #     http = credentials.authorize(httplib2.Http())
        data = {'client_id':'224611185406-ln4f75s9vh77ckd9bicds121271k5lj8.apps.googleusercontent.com', 
                'scope':'paste'} 
        url = 'https://accounts.google.com/o/oauth2/device/code'
        r = requests.post(url,data = data)
        r.post
    
    def get_token(self):
    #           {
    #     "device_code" : "4/4-GMMhmHCXhWEzkobqIHGG_EnNYYsAkukHspeYUk9E8",
    #     "user_code" : "GQVQ-JKEC",
    #     "verification_url" : "https://www.google.com/device",
    #     "expires_in" : 1800,
    #     "interval" : 5
    #   }
        data = {'client_id': '224611185406-ln4f75s9vh77ckd9bicds121271k5lj8.apps.googleusercontent.com', 
                'scope':'profile,email'} 
        url = 'https://accounts.google.com/o/oauth2/device/code'
        r = requests.post(url,data = data)
        json_response = json.loads(r.text)
        print(r.text)
        t = threading.Thread(target=self.listen_for_response('224611185406-ln4f75s9vh77ckd9bicds121271k5lj8.apps.googleusercontent.com','wbYU3iPXRztKZ9j870hH65p-', json_response['device_code'] ,json_response['interval'],json_response['expires_in']),args=())
        t.start()
        if t.isAlive():
            pass
        return json_response
    
    def refresh_token():
        pass
    
    def listen_for_response(self,client_id,client_secret,device_code,interval,expires):
        # Need to implement the timeout here as well.  Im thining wrap the current while loop in another that checks a timer you start at the begining of the function
        start = time.time()
        end = time.time()
        bad_response = True
        counter = 0
        data = {'client_id': client_id,
                'client_secret':client_secret,
                'code':device_code,
                'grant_type':'http://oauth.net/grant_type/device/1.0'}
        while ( start - end ) < expires :
            counter += 1
            r = requests.post("https://www.googleapis.com/oauth2/v4/token",data)
            body = json.loads(r.text)
            print(r.text)
            print(r.status_code)
            print('count: ' + str(counter) )
            if r.status_code == 428:
                print(body['error'])
                print('sleeping for ' + str(interval))
                time.sleep(interval)
                #break
            if r.status_code == 403:
                interval += 10
                print('slowing interval to: ' + str(interval))
            if r.status_code == 200:
                #return true
                self.c.set_access_token(body.access_token)
                self.c.set_refresh_token(body.refresh_token)
                break
            
            else:
                time.sleep(interval)
            
            end = time.time()
        

    def logout(self):
        pass
    # PHOTOS
    def get_album_list(self):
        # Returns a dictionary of album names/URLs?  Maybe see what else the API grants access to
        return []

    def load_album(self):
        pass