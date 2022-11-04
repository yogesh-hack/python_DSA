## Merge Sort algo using recusion in python

# To analyse the comlexity of merge sort by using recusion

def merged(left, right):
    print('merge:',left,right)
    i, j ,merge = 0, 0, []
    while i< len(left) and j<len(right):
        if left[i] <= right[j]:
            merge.append(left[i])
            i += 1
        else:
            merge.append(right[j])
            j += 1
    return merge + left[i:] + right[j:]

def merged_sort(array):
    print('merge_sort:', array)
    if len(array) < 2:
        return array
    mid = len(array)//2
    return merged(merged_sort(array[:mid]),merged_sort(array[mid:]))

print(merged_sort([2,4,6,8,44,3,5,6]))

# =============== Output ============================

# merge_sort: [2, 4, 6, 8, 44, 3, 5, 6]
# merge_sort: [2, 4, 6, 8]
# merge_sort: [2, 4]
# merge_sort: [2]
# merge_sort: [4]
# merge: [2] [4]
# merge_sort: [6, 8]
# merge_sort: [6]
# merge_sort: [8]
# merge: [6] [8]
# merge: [2, 4] [6, 8]
# merge_sort: [44, 3, 5, 6]
# merge_sort: [44, 3]
# merge_sort: [44]
# merge_sort: [3]
# merge: [44] [3]
# merge_sort: [5, 6]
# merge_sort: [5]
# merge_sort: [6]
# merge: [5] [6]
# merge: [3, 44] [5, 6]
# merge: [2, 4, 6, 8] [3, 5, 6, 44]
# [2, 3, 4, 5, 6, 6, 8, 44]