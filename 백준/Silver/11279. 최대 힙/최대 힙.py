import sys
input = sys.stdin.readline

def insert(heap, num):
    heap.append(num)
    i = len(heap) - 1
    while i > 1 and heap[i] > heap[i // 2]:
        heap[i], heap[i // 2] = heap[i // 2], heap[i]
        i = i // 2

def delete(heap):
    if len(heap) > 1:
        max_value = heap[1]
        heap[1] = heap[-1]
        heap.pop()
        i = 1
        while True:
            max_index = i
            if 2 * i < len(heap) and heap[2 * i] > heap[max_index]:
                max_index = 2 * i
            if 2 * i + 1 < len(heap) and heap[2 * i + 1] > heap[max_index]:
                max_index = 2 * i + 1
            if max_index == i:
                break
            heap[i], heap[max_index] = heap[max_index], heap[i]
            i = max_index
        return max_value
    else:
        return 0

n = int(input())
heap = [0]

for _ in range(n):
    num = int(input())
    if num > 0:
        insert(heap, num)
    else:
        print(delete(heap))