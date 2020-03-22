def mergeTwo(arr1, arr2):
    arr = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
           arr.append(arr1[i]) 
           i += 1
        else:
            arr.append(arr2[j])
            j += 1
    while i < len(arr1):
        arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        arr.append(arr2[j])
        j += 1
    return arr

def merge(arr1, arr2, arr3):
    arr = []
    i, j, k = 0, 0, 0
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] < arr2[j] and arr1[i] < arr3[k]:
            arr.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i] and arr2[j] < arr3[k]:
            arr.append(arr2[j])
            j += 1
        else:
            arr.append(arr3[k])
            k += 1
    if i == len(arr1):
        arr += mergeTwo(arr2, arr3)
    elif j == len(arr2):
        arr += mergeTwo(arr1, arr3)
    else:
        arr += mergeTwo(arr1, arr2)
    return arr

def merge3Sort(arr):
    if len(arr) <= 1:
        return arr
    n = len(arr)
    arr1 = merge3Sort(arr[:n//3]) 
    arr2 = merge3Sort(arr[n//3: 2*n//3]) 
    arr3 = merge3Sort(arr[2*n//3:])
    arr = merge(arr1, arr2, arr3)
    return arr

arr = list(map(int, input("enter array to merge sort: ").split()))
arrSorted = merge3Sort(arr)
print(f'sorted array: {arrSorted}')
