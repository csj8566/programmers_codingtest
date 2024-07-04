def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    print(graph)
    
    def dfs(node, parent):
        cnt = 1 
        for child in graph[node]:
            if child != parent:
                cnt += dfs(child, node)
        return cnt
    
    min_diff = float('inf')
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        print(graph)
        
        cnt_a = dfs(a,b)
        cnt_b = n - cnt_a
        print(cnt_a)
        print(cnt_b)
        
        min_diff = min(min_diff, abs(cnt_a - cnt_b))
        
        # 끊었던 것 원상복구
        graph[a].append(b)
        graph[b].append(a)
    
    return min_diff