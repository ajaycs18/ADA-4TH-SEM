def heapify(heap, i, n):
    max, left, right = i, 2*i + 1, 2*i + 2
    if left < n and heap[left] > heap[max]:
        max = left
    if right < n and heap[right] > heap[max]:
        max = right
    if max != i:
        heap[max], heap[i] = heap[i], heap[max]
        heapify(heap, max, n)

def buildHeap(arr):
    n = len(arr)
    for i in range(len(arr)//2 - 1, -1, -1):
        heapify(arr, i, n)
    return arr

def heapSort(heap):
    max, n = 0, len(heap) - 1
    while n > 0:
        heap[max], heap[n] = heap[n], heap[max]
        heapify(heap, 0, n)
        n -= 1
    return heap

arr = list(map(int, input('enter array: ').split()))
heap = buildHeap(arr)
print('maxHeap', heap)
sortedArr = heapSort(heap) 
print('sortedArr', sortedArr)
