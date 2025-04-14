def solution(n):
    answer = []
    
    def DFS(current_state, num_open, num_close):
        if num_open == n and num_close == n:
            answer.append(current_state)
            return
        
        if num_open < n:
            DFS(current_state + '(', num_open + 1, num_close)
            
        if num_close < num_open:
            DFS(current_state + ')', num_open, num_close + 1)
            
    DFS('', 0, 0)
    
    
    return len(answer)