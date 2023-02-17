import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://www.sololearn.com/uploads/ca-covid.csv")
df.drop('state', axis=1, inplace=True)
df['date'] = pd.to_datetime(df['date'], format="%d.%m.%y")
df['month'] = df['date'].dt.month
df.set_index('date', inplace=True)

# A scatter plot is used to show the relationship between two variables(x & y).

# For example, we can visualize how the cases/deaths are related:

df[df["month"]==6][["cases", "deaths"]].plot(kind="scatter", x='cases', y='deaths')
plt.savefig('plot.png')
