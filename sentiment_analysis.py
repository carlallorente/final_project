#Importing libraries
import tweepy
import re #To provide regular expression support.
import pandas as pd
from textblob import TextBlob # A library for processing textual data

#Defining the credentials
API_KEY = "QY6a4RckRfDgKDezclFr9IBcc"
API_SECRET = "BORwcgpPpoenadRDQUqmvTozutGZgvlc6BvlA1fzr9Fq4TuTnO"
ACCESS_TOKEN = "1550691355-VPMmM9DMahNNkeolwnaPWfMICjfnquJaznABozm"
ACCESS_SECRET = "3qgaQrWUzV4TdQiTf6DB2OXSfW4VAXTW5YUT5SEOWGDjN"
twitter_auth=tweepy.OAuthHandler(API_KEY, API_SECRET)
api=tweepy.API(twitter_auth)

#To find Netflix word
t=api.search("Netflix", count=100)

#Creating a chart with different features (using pd.DataFrame function)
netflixchart = pd.DataFrame(columns=('TWEET', 'SENTIMENT', 'SUBJECTIVITY',
                          'NUMBER_OF_RTS'))

#To get rid of duplicates
netflixchart.sort_values("TWEET", inplace = True)
netflixchart.drop_duplicates(subset ="tweet_text", keep = False, inplace = True)

#Apply TextBlob
for tweet in t:
  if tweet.lang == "en":
    sentimentText = TextBlob(tweet.text)
    netflixchart = netflixchart.append({'TWEET': re.sub(r'http\S+', '', tweet.text),
                    'SENTIMENT': sentimentText.sentiment.polarity,
                    'SUBJECTIVITY': sentimentText.sentiment.subjectivity,
                    'NUMBER_OF_RTS': tweet.retweet_count,},
                   ignore_index=True)

netflixchart.head(15)