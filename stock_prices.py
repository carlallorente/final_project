from matplotlib import pylab as plt
import pandas as pd
import os
os.chdir('/Users/X412/OneDrive - IE Students/Desktop')
df1 = pd.read_csv("NFLX.csv")
print(df1.head())
df1['Date'] = pd.to_datetime(df1.Date)

df2 = pd.read_csv("DIS.csv")
print(df2)
df2['Date'] = pd.to_datetime(df2.Date)

df3 = pd.read_csv("AMZN.csv")
print(df3)
df3['Date'] = pd.to_datetime(df3.Date)

mean = df1["Close"].mean()
plt.figure("Visual Media Stock Prices")
plt.plot(df1["Date"], df1["Close"],linewidth=0.6, label="Netflix Stock price, mean="+str(mean),color = 'red')

mean2 = df2["Close"].mean()
plt.plot(df2["Date"], df2["Close"],linewidth=0.6, label="DISNEY+ Stock price, mean="+str(mean2), color = 'blue')

mean3 = df3["Close"].mean()
plt.plot(df3["Date"], df3["Close"], linewidth=0.6, label="Amazon Stock price, mean="+str(mean3), color = 'orange')

plt.xlabel("Dates")
plt.legend(loc="upper left")

plt.show()


