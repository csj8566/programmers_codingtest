def solution(number, k):
    
    initial_k = k
    answer = ''
    n = len(number)
    stack = []

    for idx, num in enumerate(number): # (0,1), (1,9), (2,2), (3,4)
        while k and stack and int(stack[-1]) < int(num):
            stack.pop()
            k -= 1
        stack.append(num)
    answer = ''.join(stack)
        
    if len(answer) > n - initial_k:
        return answer[:n-initial_k]
    
    return answer
            
        
    
