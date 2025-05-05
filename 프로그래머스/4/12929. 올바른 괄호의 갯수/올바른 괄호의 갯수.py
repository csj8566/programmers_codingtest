def solution(n):
    answer = 0
    
    def DFS(stack, num_open, num_closed):
        nonlocal answer
        
        # 종료조건 
        # 열린 괄호랑 닫힌 괄호의 숫자의 합이 예외에 안걸리고 2n이 되면 정답
        if len(stack) == (2 * n):
            answer += 1
            return 
        
        # 백트래킹 조건을 여기서?
        if num_open > n:
            return 
        
        elif num_open < num_closed:
            return
        
        
        for i in ['(', ')']:
            if (i == '(') and (num_open < n):
                stack.append(i)
                num_open += 1
                DFS(stack, num_open, num_closed)
                num_open -= 1
                stack.pop()
                
            elif (i == ')') and (num_open > num_closed):
                stack.append(i)
                num_closed += 1
                DFS(stack, num_open, num_closed)
                num_closed -= 1
                stack.pop()
                
        
        
    DFS([], 0, 0)
        
    return answer



'''
(1. 닫힌 괄호로 시작하면 올바르지 않은 괄호임) -> 2번에 포함되는 내용임
2. 닫힌 괄호의 수가 열린 괄호보다 많아지면 올바르지 않은 괄호임.
3. 열린 괄호의 수가 N개보다 많을 수는 없음

visited 가 필요없을 것 같은데? 중복이 있을 수가 없음
그리고 visited 는 왼쪽 오른쪽중에 거르는 건데 거를 필요가 없음
'''