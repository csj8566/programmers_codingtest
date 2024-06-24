def find(root, node): # root는 각 원소의 루트를 담은 배열 / node는 현재 검사할 노드
    if root[node] == node: # 만약 본인이 root라면
        return node # 본인 반환
    root[node] = find(root, root[node]) # 만약 본인이 root 가 아니라면 재귀로 root를 찾아감
    return root[node]

def union(root, rank, x_root, y_root):
    if x_root != y_root:
        if rank[x_root] > rank[y_root]:
            root[y_root] = x_root
        elif rank[x_root] < rank[y_root]:
            root[x_root] = y_root
        else:
            root[y_root] = x_root
            rank[x_root] += 1


def solution(n, costs):
    answer = 0
    edge = 0
    root = [i for i in range(n)] # [0,1,2,3]
    rank = [0] * n 
    costs.sort(key=lambda x:x[2]) # 크루스칼 알고리즘을 사용하기 위한 가중치 오름차순
    
    
    for cost in costs: # [0,1,1]
        if edge == n-1:
            break
        x_root = find(root, cost[0])
        y_root = find(root, cost[1])
        if x_root != y_root:
            union(root, rank, x_root, y_root)
            edge += 1
            answer += cost[2]               
    
    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))