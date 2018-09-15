import tweepy
import time
from textblob import TextBlob

consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'

access_token = 'access_token'
access_token_secret = 'access_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

results = api.search("i love you", count=100)
txtfile = open('tweets.txt', 'w')

for item in results:
    txtfile.write(item.text + '\n')
    print(item.text)
    analysis = TextBlob(item.text)
    print(analysis.sentiment)
