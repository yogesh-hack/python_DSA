# The given array represents the daily number of infections for 30 days.
# Find out how many days exceeded the average number of infections.


import numpy as np

data = np.array([120, 98, 150, 65, 42, 100, 190, 220, 140, 110, 88, 89, 100, 120, 50, 180, 155, 42, 89, 77, 200, 190, 125, 98, 77, 40, 39, 59, 30, 67])

#  find average

avg = np.mean(data)

days = 0

for i in data:
    if(i > avg ):
        days += 1

# got it days 
print(days)
