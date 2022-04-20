import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
os.chdir('/Users/X412/OneDrive - IE Students/Desktop')
himym = pd.read_csv('himym.csv',
                          parse_dates=['original_air_date']) # To read the date column correctly
himym1 = pd.read_csv('himym1.csv',
                      parse_dates=['original_air_date'])

# Keeping the most important columns from the second dataset
himym1 = himym1[['title', 'original_air_date', 'imdb_rating', 'total_votes', 'desc']]

himym_final = himym.merge(himym1, how='left', on=['title', 'original_air_date'])

sns.lmplot(x="episode_num_overall", y="us_viewers", hue="season", data=himym_final)
plt.xlabel("Episode")
plt.ylabel("Number of viewers")
plt.title("Viewers through different episodes")
plt.show()