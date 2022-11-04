## Quick sort

# - In merge Sort, we optamize only time complexity not space complexity. so, Quick sort are use to optamize the space comlexity with same time complexity.
# It allocate additinal space as large as input itself makes slow it, because memory alloation is more expensve thsn swapping.

# In quick sorting algorithms, 
"""
-> Based on divide and conquer algo.
1. if list is empty or one element , return list, already sorted.
2. let first or last element as pivot.
3. perform partioning operaion -> reorder element with value less or equal to pivot.
4. pivot element divided into two sub array which sorted indepently by using recursion -> quicksort().

"""

def quick_sort(array,start =0, end=None):
    if end is None:
        # copy of an original array
        # array = list(array)
        end = len(array)-1

    # if len(array) <= 1:
    if start >= end:
        return array

    pivot = partition(array,start,end)
    # quick_sort(array[:pivot-1])  -> it makes copy
    # quick_sort(array[pivot+1:])  -> to avoid this, take start and end arguemnt
    quick_sort(array,start,pivot-1)
    quick_sort(array,pivot+1,end)
    return array

def partition(array,start=0,end=None):
    print('partition',array,start,end)
    if end is None:
        end = len(array)-1

    # initialize left and right pointer
    left, right = start, end-1

    while right > left :
        print(' ',array,left,right)
        # if value is smaller or equal than last element(pivot) then, increment left pointer.
        if array[left] <= array[end]:
            left += 1
        # if  value is smaller or equal than last element(pivot) then, decrement right pointer.
        elif array[right] > array[end]:
            right -= 1
        # if left pointer and right pointer is out-of-place, then swap with left and right
        else:
            array[left],array[right] = array[right],array[left]
    print(' ',array,left,right)
    # placed the pivot element between left and right
    if array[left] > array[end]:
        array[left],array[end] = array[end],array[left]
        print(array,left)
        return left
    else:
        print(array,end)
        return end

 # ++++++++++++++++++++++++++++++++++ OUTPUT ++++++++++++++++++++++++++++++++++++++++++++
"""
partition array: [1, 5, 2, 6, 9, 11, 3, 8, 20, 12] start: 0 end: 9
  [1, 5, 2, 6, 9, 11, 3, 8, 20, 12] 0 8
  [1, 5, 2, 6, 9, 11, 3, 8, 20, 12] 1 8
  [1, 5, 2, 6, 9, 11, 3, 8, 20, 12] 2 8
  [1, 5, 2, 6, 9, 11, 3, 8, 20, 12] 3 8
  [1, 5, 2, 6, 9, 11, 3, 8, 20, 12] 4 8
  [1, 5, 2, 6, 9, 11, 3, 8, 20, 12] 5 8
  [1, 5, 2, 6, 9, 11, 3, 8, 20, 12] 6 8
  [1, 5, 2, 6, 9, 11, 3, 8, 20, 12] 7 8
  [1, 5, 2, 6, 9, 11, 3, 8, 20, 12] 8 8
[1, 5, 2, 6, 9, 11, 3, 8, 12, 20] pivot: 8
partition array: [1, 5, 2, 6, 9, 11, 3, 8, 12, 20] start: 0 end: 7
  [1, 5, 2, 6, 9, 11, 3, 8, 12, 20] 0 6
  [1, 5, 2, 6, 9, 11, 3, 8, 12, 20] 1 6
  [1, 5, 2, 6, 9, 11, 3, 8, 12, 20] 2 6
  [1, 5, 2, 6, 9, 11, 3, 8, 12, 20] 3 6
  [1, 5, 2, 6, 9, 11, 3, 8, 12, 20] 4 6
  [1, 5, 2, 6, 3, 11, 9, 8, 12, 20] 4 6
  [1, 5, 2, 6, 3, 11, 9, 8, 12, 20] 5 6
  [1, 5, 2, 6, 3, 11, 9, 8, 12, 20] 5 5
[1, 5, 2, 6, 3, 8, 9, 11, 12, 20] pivot: 5
partition array: [1, 5, 2, 6, 3, 8, 9, 11, 12, 20] start: 0 end: 4
  [1, 5, 2, 6, 3, 8, 9, 11, 12, 20] 0 3
  [1, 5, 2, 6, 3, 8, 9, 11, 12, 20] 1 3
  [1, 5, 2, 6, 3, 8, 9, 11, 12, 20] 1 2
  [1, 2, 5, 6, 3, 8, 9, 11, 12, 20] 1 2
  [1, 2, 5, 6, 3, 8, 9, 11, 12, 20] 2 2
[1, 2, 3, 6, 5, 8, 9, 11, 12, 20] pivot: 2
partition array: [1, 2, 3, 6, 5, 8, 9, 11, 12, 20] start: 0 end: 1
  [1, 2, 3, 6, 5, 8, 9, 11, 12, 20] 0 0
[1, 2, 3, 6, 5, 8, 9, 11, 12, 20] pivot: 1
partition array: [1, 2, 3, 6, 5, 8, 9, 11, 12, 20] start: 3 end: 4
  [1, 2, 3, 6, 5, 8, 9, 11, 12, 20] 3 3
[1, 2, 3, 5, 6, 8, 9, 11, 12, 20] pivot: 3
partition array: [1, 2, 3, 5, 6, 8, 9, 11, 12, 20] start: 6 end: 7
  [1, 2, 3, 5, 6, 8, 9, 11, 12, 20] 6 6
[1, 2, 3, 5, 6, 8, 9, 11, 12, 20] pivot: 7

"""




        