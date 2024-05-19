def solution(edges):
    answer = [0, 0, 0, 0]
    edge_dict = {}
    
    for start, end in edges:  # [2, 3]
        if start not in edge_dict:
            edge_dict[start] = [0, 0]
        if end not in edge_dict:
            edge_dict[end] = [0, 0]
        
        edge_dict[start][0] += 1 # 2에서 뻗어나간 간선 하나 추가
        edge_dict[end][1] += 1 # 3으로 들어오는 간선 하나 추가
    
    # print(edge_dict)
    
    for node in list(edge_dict.items()):
        
        # 들어가는 건 없고 나가는 것만 2개이상 있으면 중간연결정점임
        if node[1][0] >= 2 and node[1][1] == 0:
            answer[0] = node[0]
        
        # 나가는 건 없고 들어오는 것만 0~1개 존재하는 정점의 개수가 막대그래프의 개수임
        # 만약 중간연결정점이 size1의 막대로 들어오면 node[1][1] == 1, size1이 아닌 막대로 들어오면 node[1][1] == 2
        elif node[1][0] == 0 and (2 >= node[1][1] >= 1):
            answer[2] += 1
            
        # 나가는 거 2개, 들어오는 거 2개인 정점의 개수가 8자그래프의 개수임
        # 만약 중간연결정점이 8자그래프의 가운데부분으로 들어오면 node[1][1] == 3
        elif node[1][0] == 2 and (3 >= node[1][1] >= 2):
            answer[3] += 1
            
    answer[1] = edge_dict[answer[0]][0] - answer[2] - answer[3]
        


    return answer