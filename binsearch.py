arr = list(map(int, input().split(' ')))
ele = int(input())

start, end = 0, len(arr)-1
first_idx, last_idx = 0, 0

def binSearch(arr, ele, start, end):
    global first_idx, last_idx
    if start > end:
        return

    mid = (start + end) // 2
    
    if arr[mid] == ele:
        if mid > 0 and arr[mid-1] == ele:
            end = mid - 1
            first_idx = end 
            binSearch(arr, ele, start, end)
        if mid < len(arr)-1 and arr[mid+1] == ele:
            start = mid + 1
            last_idx = start
            binSearch(arr, ele, start, end)
        else:
            return
    elif ele > arr[mid]:
        start = mid + 1
    else:
        end = mid - 1
        
    binSearch(arr, ele, start, end)

binSearch(arr, ele, start, end)

print(f'First Occurrence: {first_idx}')
print(f'Last Occurrence: {last_idx}')
print(f'Number of Occurrences: {last_idx-first_idx+1}')
