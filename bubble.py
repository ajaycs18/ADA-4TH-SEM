import time

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# arr = list(map(int, input().split()))
inp = open('input.txt', 'r')
arr = list(map(int, inp.read().split()))
start_t = time.time()
bubbleSort(arr)
end_t = time.time()
print(len(arr))
print("Time taken", end_t - start_t)
    
