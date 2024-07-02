import sys
from collections import deque

input = sys.stdin.readline


N, M = list(map(int, input().split()))
adj = [[] for _ in range(N)]
for _ in range(M):
    a, b = list(map(int, input().split()))
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)
    
answer = []
# 케빈 베이컨 수가 가장 작은 사람을 출력해야 한다.

# 사람 한 명씩 돌면서 케빈 베이컨 수를 구해야 한다.
# 사람 한 명씩 돌면서 그 사람 기준으로 다른 사람까지 걸리는 거리의 합을 구해야 한다.
for i in range(N):
    distance = [-1 for _ in range(N)]
    visited = [False for _ in range(N)]
    queue = deque()
    queue.append(i)
    distance[i] = 0
    
    while queue:
        node = queue.popleft()
        if not visited[node]:
            visited[node] = True
            # queue.extend(adj[node])
            for j in adj[node]:
                if distance[j] == -1:
                    distance[j] = distance[node] + 1
                    queue.append(j)
    
    total_distance = sum(distance)
    answer.append((total_distance, i+1))
    
answer.sort(key=lambda x:(x[0], x[1]))
print(answer[0][1])