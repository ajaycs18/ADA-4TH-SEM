# Max Heap -> Descending Order

def heapifyUp(heap):
    if len(heap) == 1:
        return
    i = len(heap) - 1
    while i > 0:
        if heap[(i-1) // 2] < heap[i]:
            heap[(i-1) // 2], heap[i] = heap[i], heap[(i-1) // 2] 
        i -= 1
    print(heap)

def heapifyDown(heap):
    if len(heap) == 1:
        return
    i = 0
    while i < (len(heap) - 1) // 2:
        if heap[2*i + 1] > heap[i]:
            if heap[2*i + 2] > heap[2*i + 1]:
                heap[i], heap[2*i + 2] = heap[2*i + 2], heap[i]
                i = 2*i + 2
            else:
                heap[i], heap[2*i + 1] = heap[2*i + 1], heap[i]
                i = 2*i + 1

def buildHeap(arr):
    heap = []
    for ele in arr:
        heap.append(ele)
        heapifyUp(heap)
    return heap

def removeMax(heap):
    if len(heap) == 1:
        return heap.pop()
    max = heap[0]
    last = heap.pop()
    heap[0] = last
    heapifyDown(heap)
    return max

arr = list(map(int, input('enter array: ').split()))
maxHeap = buildHeap(arr)
print('maxHeap', maxHeap)
sortedArr = []
while maxHeap:
    sortedArr.append(removeMax(maxHeap))
print('sortedArr', sortedArr)
