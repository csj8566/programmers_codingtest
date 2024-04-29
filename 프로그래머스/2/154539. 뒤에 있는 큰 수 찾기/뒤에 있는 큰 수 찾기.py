def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stack = []
    
    for idx, number in enumerate(numbers):
        while stack and numbers[stack[-1]] < number:
            temp = stack.pop()
            answer[temp] = number
        stack.append(idx)
        
    
    
    return answer