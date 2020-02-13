def binSearchRecursive(arr, ele, high, low):
    if low > high:
        print("Element not found")
        return

    mid = (high + low) // 2
    
    if arr[mid] == ele:
        print("Element found at", mid)
        return
    elif arr[mid] > ele:
        high = mid - 1
    else:
        low = mid + 1

    binSearchRecursive(arr, ele, high, low)

arr = list(map(int, input().split()))
ele = int(input())
binSearchRecursive(arr, ele, len(arr)-1, 0)
