def linSearchRecursive(arr, ele, i):
    if i == len(arr):
        print("Element not found")
        return

    if arr[i] == ele:
        print("Element found at", i)
        return
    else:
        linSearchRecursive(arr, ele, i+1)

arr = list(map(int, input().split()))
ele = int(input())

linSearchRecursive(arr, ele, 0)
