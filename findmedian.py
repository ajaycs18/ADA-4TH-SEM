from statistics import median

def getMedian(arr1, arr2):
    n = len(arr1)
    m = n // 2

    if not n:
        return -1
    elif n == 1:
        return (arr1[0] + arr2[0]) // 2
    elif n == 2:
        return (max(arr1[0], arr2[0]) + min(arr1[1], arr2[1])) // 2
    else:
        m1, m2 = median(arr1), median(arr2)
        
        if m1 > m2:
            if n % 2 == 0:
                return getMedian(arr1[:m + 1], arr2[m - 1:])
            else:
                return getMedian(arr1[:m + 1], arr2[m:])
        else: 
            if n % 2 == 0:
                return getMedian(arr2[:m + 1], arr1[m - 1:])
            else:
                return getMedian(arr2[:m + 1], arr1[m:])
            
print("Enter arr1: ")
arr1 = [int(n) for n in input().split()]
print("Enter arr2: ")
arr2 = [int(n) for n in input().split()]
print(getMedian(arr1, arr2))
