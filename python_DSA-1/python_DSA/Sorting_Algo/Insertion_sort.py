## Insertion Sort 

# In insertion sorting technique, let first element is sorted and remaining right portion element sorted one by one.
# Time Complexity : O(n^2)

def Insertion_sort(array):
    for i in range(len(array)):
        current = array.pop(i);
        j = i-1
        while j>=0 and array[j] > current:
            # array[j],current = current,array[j]
            j -= 1
        array.insert(j+1,current)
    return array

if __name__ == "__main__":
    print(Insertion_sort([2,4,6,8,44,3,5,6]))
    
