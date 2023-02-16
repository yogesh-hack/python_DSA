# You are given an array that represents the occupancy of seats in a movie theater. A seat marked with 1 is occupied, while one marked 0 means the seat is free.
# However, the array is flat and 1-dimensional. Transform it into a 2-dimensional array, representing the rows of the seats.
# Each row in the theater has 5 seats and there are a total of 30 seats.
# Reshape the array into the corresponding shape and output the row at the given index, which is taken from user input.


import numpy as np

data = np.array([1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0])

row = int(input())

# 5 X 6 => 30

data = data.reshape(6,5)

print(data[row])

