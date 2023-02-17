## Merge Sort

# In merge sorting technique, use divide and conquer technique which divide the original array into sub-array and then merge with compare each elements.
# time complexity : O(logn)
# Space complexity : O(n)

def merge_sort(array):
    if len(array)>0:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i<len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

            while i<len(left):
                array[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1
    return array

if __name__ == "__main__":
    print(merge_sort([2,4,6,8,44,3,5,6]))
