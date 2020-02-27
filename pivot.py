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

def binarySearch(arr, low, high, key): 
  mid = int((low + high)/2) 
  if high < low: 
    return
  elif key == arr[mid]: 
    print("found at", mid)
    return
  if key > arr[mid]: 
    return binarySearch(arr, (mid + 1), high, key) 
  else:
      return binarySearch(arr, low, (mid -1), key); 

arr = list(map(int, input().split()))
pivot = findPivot(arr, 0, len(arr) - 1)
print("pivot ele:", arr[pivot])
ele = int(input("enter ele to find: "))

if pivot == -1: 
  binarySearch(arr, 0, len(arr)-1, ele)
if arr[pivot] == ele: 
  print("Found at", pivot)
if arr[0] <= ele: 
  binarySearch(arr, 0, pivot-1, ele) 
binarySearch(arr, pivot+1,len(arr)-1, ele)
