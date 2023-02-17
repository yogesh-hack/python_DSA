## Binary Search alogorithms

def binary_search(array,target):
    low , high = 0,len(array)
    while low <= high:
        mid = (low+high)//2
        mid_number = array[mid]

        if mid_number == target:
            return mid+1
        elif mid_number < target:
            # if order of array is decreasing;
            high = mid - 1
            ## if order f array is increasing;
            # low = mid + 1
        elif mid_number > target:
            # if order of arrray is decraesing
            low = mid +1
            ## if order of array is increasing
            # high = mid - 1
    return "Not found."

print("Output -> ",binary_search([23,12,9,6,3,1],9))
print("Output -> ",binary_search([12,9,9,9,5,1],9))
print("Output -> ",binary_search([23,12,9,6,3,3],20))