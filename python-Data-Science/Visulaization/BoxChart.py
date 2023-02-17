import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://www.sololearn.com/uploads/ca-covid.csv")
df.drop('state', axis=1, inplace=True)
df['date'] = pd.to_datetime(df['date'], format="%d.%m.%y")
df['month'] = df['date'].dt.month
df.set_index('date', inplace=True)

# create a box plot for the cases in June:

df[df["month"]==6]["cases"].plot(kind="box")

plt.savefig('plot.png')

# box chart is used when distributed of columns
