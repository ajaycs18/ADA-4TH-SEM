def inSort(arr):
    for i in range(1, len(arr) - 1):
        ele = arr[i]
        j = i - 1
        while j > -1 and arr[j] > ele:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = ele


arr = list(map(int, input().split())) 
inSort(arr)
print(arr)
