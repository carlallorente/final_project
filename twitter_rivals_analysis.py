from tweepy import API, OAuth1UserHandler
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

count = 100

def TwitterClient():
    API_KEY = "QY6a4RckRfDgKDezclFr9IBcc"
    API_SECRET = "BORwcgpPpoenadRDQUqmvTozutGZgvlc6BvlA1fzr9Fq4TuTnO"
    ACCESS_TOKEN = "1550691355-VPMmM9DMahNNkeolwnaPWfMICjfnquJaznABozm"
    ACCESS_SECRET = "3qgaQrWUzV4TdQiTf6DB2OXSfW4VAXTW5YUT5SEOWGDjN"
    auth = OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    api = API(auth)
    return api
if __name__ == '__main__':
    twitter_api = TwitterClient()
    people = ["netflix", "hbo", "primevideo", "disneyplus"]
    tweets = {}
    for ppl in people:
        tweets[ppl] = twitter_api.user_timeline(screen_name=ppl, count=count)
    dfs = {}
    for ppl in people:
        dfs[ppl] = pd.DataFrame()
        texts = []
        favs = []
        rets = []
        for tweet in tweets[ppl]:
            texts.append(tweet.text)
            favs.append(tweet.favorite_count)
            rets.append(tweet.retweet_count)

        dfs[ppl]["Text"] = texts
        dfs[ppl]["Favorites"] = favs
        dfs[ppl]["Retweets"] = rets

    y_pos = np.arange(len(people))
    average = []
    for ppl in people:
        average.append(np.average(dfs[ppl]['Favorites'].values))
        print(f"\b\n{ppl} most liked tweet: \n {dfs[ppl]['Text'][np.argmax(dfs[ppl]['Favorites'])]}\n Number of favorites {np.max(dfs[ppl]['Favorites'])}")

    plt.bar(y_pos, average, alpha=0.8, color=['red', 'purple', 'lightblue', 'darkblue'])
    plt.xticks(y_pos, people)
    plt.ylabel('Number of favorites')
    plt.title('Most famous streaming platform on Twitter\n based on the number of favs')
    plt.show()