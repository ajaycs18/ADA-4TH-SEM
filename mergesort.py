import time

def merge(arr1, arr2):
    arr = []
    i = j = k = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
        k += 1
    while i < len(arr1):
        arr.append(arr1[i]) 
        i += 1
        k += 1
    while j < len(arr2): 
        arr.append(arr2[j]) 
        j += 1
        k += 1
    return arr

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2;
    left, right = arr[:mid], arr[mid:]
    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left, right)

arr = [1, 5, 4, 6, 3, 2]
start = time.time()
sorted_arr = mergeSort(arr)
end = time.time()
print(f'Sorted Array: {sorted_arr}  Time Taken: {end - start}')
