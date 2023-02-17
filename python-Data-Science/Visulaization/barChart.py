import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://www.sololearn.com/uploads/ca-covid.csv")
df.drop('state', axis=1, inplace=True)
df['date'] = pd.to_datetime(df['date'], format="%d.%m.%y")
df['month'] = df['date'].dt.month
df.set_index('date', inplace=True)


# For bar plots, provide kind="bar".

# make a bar plot for the monthly infection cases:

# We first group the data by the month column, then calculate the sum of the cases in that month.

(df.groupby('month')['cases'].sum()).plot(kind="bar")

plt.savefig('plot.png')
