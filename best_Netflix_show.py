import tweepy as tweepy


API_KEY = "3PsK3GDCPMT3Zv3NMrpzFJobK"
API_SECRET = "uFvDrTD6PazgtGUIOjVLtc6puflb81wllLI4v4RmNGNjnMfTed"
ACCESS_TOKEN = "1061195078436356101-r4D8HVKp32f0h3wocEaJpDOt1Xu3jh"
ACCESS_SECRET = "LveLP3wTh71M0WZwl1LkjoNn4STtlruobEho0MGKHD8Kl"


auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search_tweets, q="Netflix best show", count=20).items(20):
    if (not tweet.retweeted) and ('RT @' not in tweet.text):
        if tweet.lang == "en":
            print([tweet.text])