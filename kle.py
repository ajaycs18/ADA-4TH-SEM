import time
import random

def selSort(arr):
	for i in range(len(arr)-1):
		pos = i
		for j in range(i+1, len(arr)):
			if arr[j] < arr[i]:
				pos = j
		arr[i], arr[pos] = arr[pos], arr[i]

arr = list(map(int, input().split()))
k = int(input())
selSort(arr)
print(arr)
print(f"{k} largest elements: {arr[-1:-1-k:-1]}")


