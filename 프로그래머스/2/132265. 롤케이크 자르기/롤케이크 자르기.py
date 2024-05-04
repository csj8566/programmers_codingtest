from collections import Counter

def solution(topping):
    answer = 0
    
    right_counter = dict(Counter(topping))
    left_counter = {}
    
    right_unique = len(set(topping))
    left_unique = 0
    
    for i in topping:
        if i not in left_counter:
            left_counter[i] = 1
            left_unique += 1
            right_counter[i] -= 1
            
            if right_counter[i] == 0:
                right_unique -= 1
            
            if left_unique == right_unique:
                answer += 1
        
        else:
            left_counter[i] += 1
            right_counter[i] -= 1
            
            if right_counter[i] == 0:
                right_unique -= 1
                
            if left_unique == right_unique:
                answer += 1
            

    return answer