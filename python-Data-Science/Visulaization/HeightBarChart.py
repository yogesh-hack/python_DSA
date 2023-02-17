#  Create a bar chart to show the average height of each ages

import pandas as pd
import matplotlib.pyplot as plt

# read the people.csv file
df = pd.read_csv("people.csv")

# set age as index
df.set_index("age", inplace = True)

# show average height by group of age
df = df.groupby("age")["height"].mean()

# set in Bar ploy
df.plot(kind = "bar")

# save the bar chart
plt.savefig("height.png")
