## Linear searching program
def linear_search(array,target):
    position = 0
    #while True:
    while position < len(array): # it use for if array is empty.
        if array[position] == target:
            return position+1;
        else:
            position += 1
        if position == len(array):
            return "Not exist."
    return "array is empty."

print("output -> ",linear_search([5,7,8,2,54,7,35,5,6,2,6,8],8))
print("output -> ",linear_search([],5))
print("output -> ",linear_search([5,5,5,5,5,5],5))