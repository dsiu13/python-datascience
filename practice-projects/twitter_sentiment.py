import tweepy
from textblob import TextBlob

# sentiment analysis - Understanding and extracing feelings from data
# Polarity, measures how positive or negative some text is
# Subjectivity, How much of an opinion is vs how factual it is

# Keys
consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'

access_token = 'access_token'
access_token_secret = 'access_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
