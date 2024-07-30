from collections import deque

N, K = list(map(int, input().split()))

def BFS(root,time):
    visited = set()
    queue = deque()

    queue.append((root, time))
    while queue:
        current, c_time = queue.popleft()
        if current == K:
            return c_time
        
        if current not in visited:
            visited.add(current)

            if current-1 >= 0:
                queue.append((current-1, c_time + 1))
            
            if current+1 <= 100000:
                queue.append((current+1, c_time + 1))
            
            if 2 * current <= 100000:
                queue.append((2 * current, c_time + 1))


print(BFS(N, 0))