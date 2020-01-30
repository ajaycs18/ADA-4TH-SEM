testcases = int(input())

for _ in range(testcases):
    n, ele = map(int, input().split(" ")) 
    arr = list(map(int, input().split(" ")))

    # sort if required
    arr = sorted(arr)
    
    start, end = 0, len(arr) 
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == ele:
           print(1)
           break
        elif arr[mid] > ele:
           end = mid - 1
        else:
            start = mid + 1

    if start > end:
        print(-1)

