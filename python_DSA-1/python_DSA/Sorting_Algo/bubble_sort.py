## bubble sorting in python

def bubble_sort(array):
    # for i in range(len(array)-1):
    for _ in range(len(array)-1):
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i],array[i+1] = array[i+1],array[i]
    return array

if __name__ == "__main__":
    print(bubble_sort([2,4,6,8,44,3,5,6]))
