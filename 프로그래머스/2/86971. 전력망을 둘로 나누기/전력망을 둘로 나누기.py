def solution(n, wires):
   
    # 트리 만들기 : 인덱싱 편의를 위해 n+1 의 길이로 만듦
    tree = [[] for _ in range(n+1)]
    for start, end in wires:
        tree[start].append(end)
        tree[end].append(start)
    # print('initial_tree : ', tree)
    
    # DFS 함수 만들기
        #cnt를 handle 하려면 재귀가 편할거임
    def DFS(node, parent):
        # 필요한 변수가 있는가
        cnt = 1
        # 조기반환 로직이 필요한가
        
        for child in tree[node]:
            # 절대 방문하면 안되는 것은 막아야 한다. 부모로 역류하는 거 막아야 함
            if child != parent:
            # 재귀호출을 통해 원하는 것을 실행
                cnt += DFS(child, node) # 본인을 기준으로 하는 서브트리 총노드수
            # 백트래킹 할 필요가 있다면 여기서
            
        return cnt
    
    
    minimum_difference = 99999
    # 하나씩 끊어가면서 두 개의 트리의 노드 개수를 파악해서 비교    
    for a, b in wires:
        tree[a].remove(b)
        tree[b].remove(a)
        
        # DFS(node, parent) 에서 b는 잘린 반대쪽 서브트리의 루트->이러면 첫실행 if문에 안걸림
        cnt_a = DFS(a, b) # a를 루트로 가지는 트리의 노드 총 개수
        cnt_b = n - cnt_a # b를 루트로 가지는 트리의 노드 총 개수
        
        minimum_difference = min(minimum_difference, abs(cnt_a - cnt_b))
        
        # 한 과정 끝났으면 현재 끊었던 간선은 다시 이어줘야 한다.
        tree[a].append(b)
        tree[b].append(a)
    
    return minimum_difference