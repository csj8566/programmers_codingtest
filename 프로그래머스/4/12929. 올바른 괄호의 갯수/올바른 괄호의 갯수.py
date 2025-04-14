def solution(n):
    answer = []
    
    def DFS(current_state, num_open, num_closed):
        
        # 종료 조건 : 열린 거 n개, 닫힌 거 n개 정상적으로 다 썼을 때
        if num_open == n and num_closed == n:
            answer.append(current_state)
            return
        
        # 만약 열린 괄호 개수보다 닫힌 괄호 개수가 더 많다면 그건 안됨
        # 만약 열린 괄호가 더 많은 경우에는 그 다음에는 열린 괄호든, 닫힌 괄호든 올 수 있음
        # 근데 열린 괄호는 최대 n개까지밖에 올 수 없음
        if num_open < n:
            DFS(current_state + '(', num_open + 1, num_closed)
            
        if num_closed < num_open:
            DFS(current_state + ')', num_open, num_closed + 1)
            
    
    # 모든 탐색을 다 끝내구 가능한 경우의 수를 return 하면 그게 정답
    DFS('', 0, 0)
    
    
    return len(answer)