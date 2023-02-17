import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://www.sololearn.com/uploads/ca-covid.csv")
df.drop('state', axis=1, inplace=True)
df['date'] = pd.to_datetime(df['date'], format="%d.%m.%y")
df['month'] = (df['date'].dt.month_name()).str[:3]
df.set_index('date', inplace=True)

df.groupby('month')['cases'].sum().plot(kind="pie")
plt.savefig('plot.png')
