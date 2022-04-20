import pandas as pd
import os
import matplotlib.pyplot as plt
os.chdir('/Users/X412/OneDrive - IE Students/Desktop')
df = pd.read_csv("netflix.csv", on_bad_lines='skip')
print(df)
gdp = pd.read_csv("gdp.csv", on_bad_lines='skip')
print(gdp)

# Clean the gdp dataframe
for col in gdp.columns:
    print(col)
gdp.drop(gdp.iloc[:, 2:64], axis=1, inplace=True)
print(gdp)
gdp.dropna(subset=["2020"], inplace=True)
print(gdp)

# Merge dataframes to have country matching with gdp per capita
df = pd.merge(df, gdp, how='left', left_on='Country',
              right_on='Country Name').drop(['Country Name', 'Country Code'], axis=1)
print(df)
for col in df.columns:
    print(col)
# Check dataframe and remove any naN values from the merge
check = df.isnull().values.any()
print(check)
df.dropna(subset=["2020"], inplace=True)
check2 = df.isnull().values.any()
print(check2)
df.rename(columns={'2020': 'gdp per capita'}, inplace=True)
print(df)

# Plotting basic cost per month
plt.figure()
netflix = df['Country'][:20]
chart = df.groupby(netflix)['Cost Per Month - Basic ($)'].sum().sort_values(ascending=False).plot(kind='bar', color="lightblue")
chart.set_xticklabels(chart.get_xticklabels())
plt.title("Cost Per Month - Basic ($)\n Top 20 Countries")
plt.xlabel('Country name')
plt.ylabel('Cost Per Month - Basic ($)')
plt.show()

plt.scatter(df['gdp per capita'], df['Cost Per Month - Basic ($)'], color='lightblue')
plt.title('GDP Per Capita vs Cost Per Month - Basic', fontsize=14)
plt.xlabel('GDP Per Capita ($)', fontsize=14)
plt.ylabel('Cost Per Month - Basic ($)', fontsize=14)
plt.grid(True)
plt.show()


# Plotting standard cost per month
plt.figure()
netflix = df['Country'][:20]
chart1 = df.groupby(netflix)['Cost Per Month - Standard ($)'].sum().sort_values(ascending=False).plot(kind='bar', color="blue")
chart1.set_xticklabels(chart1.get_xticklabels())
plt.title("Cost Per Month - Standard ($)\n Top 20 Countries")
plt.xlabel('Country name')
plt.ylabel('Cost Per Month - Standard ($)')
plt.show()

plt.scatter(df['gdp per capita'], df['Cost Per Month - Standard ($)'], color='blue')
plt.title('GDP Per Capita vs Cost Per Month - Standard', fontsize=14)
plt.xlabel('GDP Per Capita ($)', fontsize=14)
plt.ylabel('Cost Per Month - Standard ($)', fontsize=14)
plt.grid(True)
plt.show()

# Plotting premium cost per month
plt.figure()
netflix = df['Country'][:20]
chart2 = df.groupby(netflix)['Cost Per Month - Premium ($)'].sum().sort_values(ascending=False).plot(kind='bar', color="darkblue")
chart2.set_xticklabels(chart2.get_xticklabels())
plt.title("Cost Per Month - Premium ($)\n Top 20 Countries")
plt.xlabel('Country name')
plt.ylabel('Cost Per Month - Premium ($)')
plt.show()

plt.scatter(df['gdp per capita'], df['Cost Per Month - Premium ($)'], color='darkblue')
plt.title('GDP Per Capita vs Cost Per Month - Premium', fontsize=14)
plt.xlabel('GDP Per Capita ($)', fontsize=14)
plt.ylabel('Cost Per Month - Premium ($)', fontsize=14)
plt.grid(True)
plt.show()

# GDP per capita figure
netflix = df['Country'][:20]
chart3 = df.groupby(netflix)['gdp per capita'].sum().sort_values(ascending=False).plot(kind='bar', color="green")
chart3.set_xticklabels(chart3.get_xticklabels())
plt.title("GDP per capita\n Top 20 Countries")
plt.xlabel('Country name')
plt.ylabel('GDP per capita')
plt.show()

# Regression
from sklearn import linear_model
import statsmodels.api as sm

X = df[['Total Library Size', 'No. of TV Shows', 'No. of Movies', 'gdp per capita']]
Y = df['Cost Per Month - Premium ($)']
regression = linear_model.LinearRegression()
regression.fit(X, Y)

model = sm.OLS(Y, X).fit()
predictions = model.predict(X)

print_model = model.summary()
print(print_model)
