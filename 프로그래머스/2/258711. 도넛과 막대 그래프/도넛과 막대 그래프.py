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
#     print(edge_dict)
    
#     print(list(edge_dict.items()))
    
    for node in list(edge_dict.items()):
        
        # 들어가는 건 없고 나가는 것만 2개이상 있으면 중간연결정점임
        if node[1][0] >= 2 and node[1][1] == 0:
            answer[0] = node[0]
        
        # 나가는 건 없고 들어오는 것만 1개 존재하는 정점의 개수가 막대그래프의 개수임
        elif node[1][0] == 0 and node[1][1] >= 1:
            answer[2] += 1
            
        # 나가는 거 2개, 들어오는 거 2개인 정점의 개수가 8자그래프의 개수임
        elif node[1][0] == 2 and node[1][1] >= 2:
            answer[3] += 1
            
    answer[1] = edge_dict[answer[0]][0] - answer[2] - answer[3]
        


    return answer







'''
<첫인상>
뭘로 풀어야 하지? 유니온파인드?
O(nlogn) 알고리즘 까지 가능
---------------------------------------------
<정의>
1. 도넛 
  - n개의 정점 / n개의 간선
  - 모든 정점은 들어오는 간선과 나가는 간선을 1개 이상씩 갖고 있음

2. 막대
  - 막대 그래프의 끝부분은 나가는 간선 0개, 들어오는 간선 1개
  - 막대 그래프의 시작부분은 나가는 간선 1개, 들어오는 간선 0개

3. 8자
  - 모든 정점이 나가는 간선과 들어오는 간선을 1개 이상 가지고 있음
  - 2n+1개의 정점, 2n+2개의 정점 (n+1크기의 8자그래프는 n크기의 도넛그래프 2개를 합친 것)

4. 중간 연결정점 
  - 들어오는 간선 0개
  - 나가는 간선 x개 (x는 2이상)
  
<알고리즘>
- 들어가는 건 없고 나가는 것만 2개이상 있으면 중간연결정점임
- 나가는 건 없고 들어오는 것만 1개 존재하는 정점의 개수가 막대그래프의 개수임
- 나가는 거 2개, 들어오는 거 2개인 정점의 개수가 8자그래프의 개수임
- 중간연결정점의 나가는 간선의 개수 - 8자그래프개수 - 막대그래프 개수 = 도넛그래프 개수임

그래서 배열(or 딕셔너리) 만들고 edges 하나씩 돌면서 배열 최신화하고 위 4가지 검사해서 뭐가 뭔지 파악하고 answer 배열에 담어서 return 만 해주면 끝 

그러면 함수가 두 개 필요할 듯. main인 solution 함수와 check 해주는 함수  
'''