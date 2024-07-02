import sys
input = sys.stdin.readline

N = int(input())
parents = list(map(int, input().split()))
erase = int(input())

for i in range(N):
    if parents[i] == -1:
        root = i

# 지워지는 애 및 자손 전부 삭제
black = [0 for _ in range(N)]
for i in range(N):
    node = i
    
    while True:
        if node == erase:
            black[i] = 1
            break
            
        if node == root:
            break
            
        node = parents[node]
            
# 자식 있는 애 전부 삭제
red = [0 for _ in range(N)]
for i in range(N):
    if black[i] == 1:
        continue
    if i == root:
        continue
    red[parents[i]] = 1
    
# 리프 개수 찾자
cnt = 0
for i in range(N):
    if black[i] == 1 or red[i] == 1:
        continue
    cnt += 1
print(cnt)