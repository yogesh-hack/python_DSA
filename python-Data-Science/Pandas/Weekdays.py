# You continue working with the COVID dataset for California.
# Now, add the weekday names for each row as a new column, named 'weekday'.
# Then, output the last 7 days data of the dataset.
# Do not set any index on the DataFrame.


import pandas as pd

df = pd.read_csv("/usercode/files/ca-covid.csv")

df.drop('state', axis=1, inplace=True)
df['date'] = pd.to_datetime(df['date'], format="%d.%m.%y")

# adding nwe column

# Use the .dt.strftime("%A") function on the date column to convert it into a weekday name.
df["weekday"] = df["date"].dt.strftime("%A")

print(df[-7:])
