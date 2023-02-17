
# You are given a task to find all of the whole numbers below 100 that are multiples of both 3 and 5.
# Create an array of numbers below 100 that are multiples of both 3 and 5, and output it.

import numpy as np

data = np.arange(1,100)

print(data[(data % 3 == 0)  & (data % 5 == 0 )])
