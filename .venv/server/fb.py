from decouple import config
import pyrebase
import requests


FIREBASE_APIKEY = config('FIREBASE_APIKEY')
AUTH_DOMAIN = config('AUTH_DOMAIN')
STORAGE_BUCKET = config('STORAGE_BUCKET')


def setup_fb():
    try:
        config = {
          "apiKey": FIREBASE_APIKEY,
          "authDomain": AUTH_DOMAIN,
          "databaseURL":  '',
          "storageBucket": STORAGE_BUCKET
        }

        firebase = pyrebase.initialize_app(config)
        return firebase
    except Exception as error:
        print(error)
        return False
    
def signed_in(email, password):
    try: 
      fb = setup_fb()
      if email == 'ecleaver@live.com' and fb != False:
          auth = fb.auth()
          
          user = auth.sign_in_with_email_and_password(email, password)
          
          return True
      else: 
          return False
    except ArithmeticError as error:
        print(error)
        return False
    except SyntaxError as error:
        print(error)
        return False
    except requests.exceptions.HTTPError as error:
      response = error.args[0].response
      error = response.json()['error']
      print(response, error)
      return False



