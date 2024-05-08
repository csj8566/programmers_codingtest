from collections import Counter

def solution(topping):
    answer = 0
    n = len(topping) # 8
    
    right_counter = dict(Counter(topping)) # 쪼개기 전 전체 topping 을 Counter 객체로 만든 걸로 초기화
    left_counter = {}
    
    unique_right = len(right_counter) # 4
    unique_left = 0
    
    for i in topping:
        if i not in left_counter: # 왼쪽에 새로운 토핑 등장
            left_counter[i] = 1
            unique_left += 1
            right_counter[i] -= 1
            
            if right_counter[i] == 0: # 왼쪽에 토핑 할당하느라 오른쪽에 더이상 그 토핑 존재하지 않는다면
                unique_right -= 1
                
            if unique_left == unique_right: # 정답이 되는 경우의 수라면
                answer += 1
          
        else: # 왼쪽에게 있어서 새로운 토핑은 아니지만
            left_counter[i] += 1
            right_counter[i] -= 1
            
            if right_counter[i] == 0:
                unique_right -= 1
                
            if unique_left == unique_right:
                answer += 1
            
                     
    return answer