import time
import json
import tweepy
# import credentials
from os import environ

# consumer_key = credentials.api_key #API key
# consumer_secret = credentials.api_key_secret #API key scret
# key = credentials.access_token #Access token
# secret = credentials.access_token_secret #Access token secret

consumer_key = environ['api_key'] #API key
consumer_secret = environ['api_key_secret'] #API key scret
key = environ['access_token'] #Access token
secret = environ['access_token_secret'] #Access token secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) # Authentication
auth.set_access_token(key, secret) # Grant access to API

api = tweepy.API(auth) # Connect to API
# api.update_status('Everybody Lies 2') # Update status

def get_quote():
    url = 'https://programming-quotes-api.herokuapp.com/Quotes/random' #'http://quotes.stormconsultancy.co.uk/random.json'
    response = requests.get(url)
    data = json.loads(response.text)
    data = data['en']+'\n--'+data['author']
    return data

def tweet_quote():
    interval = 60 * 20 # 20 minutes

    while True:
        quote = get_quote()
        api.update_status(quote)
        time.sleep(interval)

if __name__ == "__main__":
    tweet_quote()
