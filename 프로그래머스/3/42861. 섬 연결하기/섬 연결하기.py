def solution(n, costs):
    answer = 0
    root = [i for i in range(n)] # 0, 1, 2, 3 (루트가 처음엔 자기자신. 다 떨어져 있으므로)
    edge = 0
    rank = [0 for _ in range(n)]
    print(rank)
    
    
    
    
# -------------------------------------------------------------------------------------------
    # 두 섬이 연결된 섬인지 아닌지 확인하는 find 코드
    # 근데 find 2번 해서 각각의 루트가 같은지 다른지 비교하는 게 맞는 방법인듯
    # 그렇다면 find() 는 root를 찾는 함수가 돼야겠네
    def find(node):
        # 만약 root 라면 자기자신을 반환
        if root[node] == node:
            return node
        # 만약 root 가 아니라면(자기자신이 아니라면) 부모를 찾아감. -> 본인스스로가 나오면 root니 그때까지
        else:
            root[node] = find(root[node])
            return root[node]
        
# -------------------------------------------------------------------------------------------
    # 두 섬을 연결하는 union 코드
    def union(x_root, y_root):
        nonlocal edge, answer
        if rank[x_root] > rank[y_root]:
            root[y_root] = x_root
            edge += 1
            answer += cost[2]
        elif rank[x_root] < rank[y_root]:
            root[x_root] = y_root
            edge += 1
            answer += cost[2]
        else:
            root[y_root] = x_root
            edge += 1
            rank[x_root] += 1
            answer += cost[2]
# -------------------------------------------------------------------------------------------   
    # costs를 비용에 따라 오름차순 정렬
    costs.sort(key=lambda x:x[2])
    
    
    # costs의 원소 하나씩을 돌면서 확인
    for cost in costs:
        # edge 가 n -1 개가 되면 코드 종료
        if edge == n-1:
            break
        
        # 만약 두 섬이 연결되지 않은 섬이면 -> 두 섬을 연결 -> edge 하나 추가 -> 비용만큼 answer에 더하기
        x_root = find(cost[0])
        y_root = find(cost[1])
        
        if x_root != y_root:
            union(x_root, y_root)

            
    return answer