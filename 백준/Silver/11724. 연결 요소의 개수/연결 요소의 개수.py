from collections import deque
import sys
input = sys.stdin.readline

# 입력 받기
n, m = map(int, input().split())

# 그래프 인접 리스트 초기화
adj = [[] for _ in range(n)]

# 간선 입력 받기
for _ in range(m):
    u, v = map(int, input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

cnt = 0
visited = [False for _ in range(n)]

# BFS를 이용한 연결 요소 세기
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
