from collections import deque
import sys
input = sys.stdin.readline


n, m = list(map(int, input().split()))
adj = [[] for _ in range(n)]
for i in range(m):
    u, v = list(map(int, input().split()))
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)
    
cnt = 0
visited = [False for _ in range(n)]

for i in range(n):
    if visited[i]:
        continue
        
    cnt += 1
    queue = deque([i])
    visited[i] = True
    
    while queue:
        u = queue.popleft()
        
        for v in adj[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
            
print(cnt)