
# The given code includes a list of heights for various basketball players.
# You need to calculate and output how many players are in the range of one standard deviation from the mean.
# players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]


players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]

import numpy as np

mean = np.mean(players)
std_dev = np.std(players)
variance = np.var(players)

ans = 0
low = mean - std_dev
high = mean + std_dev

for i in players:
    if(i >= low and i <= high):
        ans += 1

print(ans)

