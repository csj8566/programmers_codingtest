import re

def solution(user_id, banned_id):
    # lst = [[] for i in range(len(banned_id))]
    lst = []

    for idx_ban, ban in enumerate(banned_id): # "fr*d*", "abc1**"
        pattern = ban.replace('*','.')
        pattern = re.compile(pattern)
        # print(pattern)
        
        matched = [i for i in user_id if len(ban) == len(i) and re.fullmatch(pattern, i)]
        # lst[idx_ban].append(matched)
        lst.append(matched)
    print(lst)
    
    def DFS(depth, path, visited):
        if depth == len(lst):
            answer.add(tuple(sorted(path))) #set에는 tuple은 추가 가능하지만 list는 안됨
            return
        for user in lst[depth]:
            if user not in visited:
                visited.add(user)
                DFS(depth+1, path + [user], visited)
                visited.remove(user)
            
        
    answer = set()
    DFS(0, [], set())
    print(lst)
    return len(answer)
