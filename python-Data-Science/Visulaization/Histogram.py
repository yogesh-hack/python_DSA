import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://www.sololearn.com/uploads/ca-covid.csv")
df.drop('state', axis=1, inplace=True)
df['date'] = pd.to_datetime(df['date'], format="%d.%m.%y")
df['month'] = df['date'].dt.month
df.set_index('date', inplace=True)

# Visually histograms are similar to bar charts, however, histograms display frequencies for a group of data rather than an individual data point; 
# therefore, no spaces are present between the bars.

df[df["month"]==6]["cases"].plot(kind="hist") 

plt.savefig('plot.png')
