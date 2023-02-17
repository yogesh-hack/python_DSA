## Selection Sort 

# In selection sorting technique, Let first element is minimum and compare with second element.

def selection_sort(array):
    for i in range(len(array)):
        minimum = i
    for j in range(i+1):
        if(array[j] < minimum):
            minimum = j
    array[i],array[minimum] = array[minimum],array[i]
    return array

if __name__ == "__main__":
    print(selection_sort([2,4,6,8,44,3,5,6]))

    