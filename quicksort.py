import time

def partition(arr, lo, hi):
    pivot = arr[lo]
    i, j = lo, hi
    while i < j:
        while i <= hi and arr[i] <= pivot:
            i += 1
        while i >= lo and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[i], arr[j]
    arr[lo], arr[j] = arr[j], arr[lo]
    return j

def quickSort(arr, lo, hi):
    if lo < hi:
        j = partition(arr, lo, hi)
        quickSort(arr, lo, j)
        quickSort(arr, j + 1, hi)

arr = list(map(int, input('enter array: ').split())) 
start = time.time()
quickSort(arr, 0, len(arr) - 1)
end = time.time()
print(f'sorted array: {arr}     time taken: {end - start}')
