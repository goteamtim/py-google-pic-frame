import base64
import hashlib
import random
import http.server
import socketserver
import requests
import credentials
import webbrowser
import google.oauth2.credentials as google_credentials
from flask import Flask
from flask import request

class google_auth(object):
    def __init__(self):
        self.auth_url = 'https://accounts.google.com/o/oauth2/v2/auth'
        self.token_endpoint = 'https://www.googleapis.com/oauth2/v4/token'
        #self.code_challenge = base64.b64encode(generate_random_string(100))
        self.c = credentials.credentials()
        

    def generate_code_challenge(self, seed_string):
        seed_string = generate_random_string(100)
        code_challenge = ''
        md5hash = hashlib.md5()
        code_challenge = base64.b64encode(md5hash.update(seed_string))
        self.code_challenge = code_challenge
        return code_challenge

    def login(self):
        # https://accounts.google.com/o/oauth2/v2/auth?
        # scope=email%20profile&
        # response_type=code&
        # state=
        # redirect_uri=http://127.0.0.1:9004&
        # client_id=client_id
        payload = {'client_id': self.c.get_client_id(), 'redirect_uri': 'http://127.0.0.1:5000', 'state': 'slideshow-access',
                   'response_type': 'code', 'scope': 'https://www.googleapis.com/auth/photoslibrary.readonly'}
        r = requests.get(self.auth_url, params=payload)
        webbrowser.open_new(r.url)
        self.start_callback_server()
        print('scope is hardcoded')
        #print(r.text)
        #raise NotImplementedError

    def start_callback_server(self):
        # PORT = 8006
        # Handler = http.server.SimpleHTTPRequestHandler
        # Handler.parse_request()
        # httpd = socketserver.TCPServer(("", PORT), Handler)
        # print ("serving at port", PORT)
        # httpd.serve_forever()

        app = Flask(__name__)

        @app.route('/')
        def hello_world():
            client_code = request.args.get('code', '')
            # Take the code and get a token here
            #auth_client = google_credentials.Credentials()
            print(client_code)
            return 'You may continue back to your app'

        @app.route('/refresh')
        def refresh_token():
            self.credentials = google_credentials.Credentials(token=request.args.get('access_token',''),refresh_token=request.args.get('refresh_token',''),id_token=request.args.get('id_token',''),expires_in=request.args.get('expires_in',''),client_id=self.c.get_client_id(),client_secret=self.c.get_client_secret())

        app.run()


    def generate_access_token(self,code):
        # code=4/P7q7W91a-oMsCeLvIaQm6bTrgtp7&
        # client_id=your_client_id&
        # client_secret=your_client_secret&
        # redirect_uri=https://oauth2.example.com/code&
        #grant_type=authorization_code
        parameters = {
            'code': code,
            'client_id': self.c.get_client_id(),
            'client_secret': self.c.get_client_secret(),
            'redirect_uri': 'http://localhost:5000/refresh',
            'grant_type': 'authorization_code'
        }
        r = requests.get(self.token_endpoint, params=parameters)
        print('Access token ')
        print(r.json())
        return r.json()

def generate_random_string(length):
    seed = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_.~0987654321'
    generated_string = ''
    counter = 0
    while (counter < length):

        generated_string += seed[random.randint(0, len(seed)-1)]
        counter += 1
    print(generated_string)
    return generated_string
