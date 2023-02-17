# You are given an array that holds the square footage data for houses on a particular street.
# A new house has just been constructed on that street.
# Modify your program to take the new house value as input, add it to the array, and output the array sorted in ascending order.


import numpy as np

data = np.array([1000, 2500, 1400, 1800, 900, 4200, 2200, 1900, 3500])

# Take a input of new house's data
new_house = int(input())

# append new house data in array
data = np.append(data,new_house)

# Sort the array in ascending order
print(np.sort(data))
