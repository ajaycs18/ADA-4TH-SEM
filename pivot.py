def findPivot(arr, low, high): 
    if high < low: 
        return -1
    if high == low: 
        return low 
      
    mid = int((low + high)/2) 
      
    if mid < high and arr[mid] > arr[mid + 1]: 
        return mid 
    if mid > low and arr[mid] < arr[mid - 1]: 
        return (mid-1) 
    if arr[low] >= arr[mid]: 
        return findPivot(arr, low, mid-1) 
    return findPivot(arr, mid + 1, high) 

arr = list(map(int, input().split()))
print(arr[findPivot(arr, 0, len(arr) - 1)])
