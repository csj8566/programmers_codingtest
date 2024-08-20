from heapq import heappop, heappush

N = int(input())
start_end_lst = []

for _ in range(N):
    num, start, end = list(map(int, input().split()))
    start_end_lst.append((start, end))

start_end_lst.sort()

min_heap = []
heappush(min_heap, start_end_lst[0][1])

for i in range(1, N):
    if start_end_lst[i][0] >= min_heap[0]:
        heappop(min_heap)

    heappush(min_heap, start_end_lst[i][1])

print(len(min_heap))