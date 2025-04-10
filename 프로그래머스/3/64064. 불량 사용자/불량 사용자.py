import re

def solution(user_id, banned_id):
    # lst = [[] for i in range(len(banned_id))]
    lst = []

    for idx_ban, ban in enumerate(banned_id): # "fr*d*", "abc1**"
        pattern = ban.replace('*','.')
        pattern = re.compile('^'+pattern+'$')
        print(pattern)
        print(type(pattern))
        
        # matched = [i for i in user_id if len(ban) == len(i) and re.fullmatch(pattern, i)]
        matched = [i for i in user_id if re.findall(pattern, i)]
        # lst[idx_ban].append(matched)
        lst.append(matched)
    print(lst)
    
    def DFS(depth, path, visited):
        ### 루트가 없는 백트래킹 DFS ###
        
        # 1. visited 에 없으면 visited 에 추가해주고 자식을 돌도록 need_visited에 추가(혹은 그에 준)
        # 2. 종료조건 세팅 : depth가 최대치일때 
        # 3. 백트래킹 
        
        if depth == len(banned_id):
            answer.add(tuple(sorted(path)))
            return
        for name in lst[depth]:
            if name not in visited:
                visited.append(name)
                DFS(depth+1, path+[name], visited)
                visited.pop()
    
    answer = set()
    DFS(depth=0, path=[], visited=[])

    print()
    print((answer))
    return len(answer)
