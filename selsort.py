import time
import random

def selSort(arr):
	for i in range(len(arr)-1):
		pos = i
		for j in range(i+1, len(arr)):
			if arr[j] < arr[i]:
				pos = j
		arr[i], arr[pos] = arr[pos], arr[i]

# arr = list(map(int, input().split()))
n = 10
time_data = []
for _ in range(1000):
	arr = [random.randint(1, n) for i in range(n)]
	start = time.time()
	selSort(arr)
	end = time.time()
	# print(f'Time taken: {end-start} for size: {n}')	
	time_data.append((n,end-start))
	n += 50
print(time_data)

