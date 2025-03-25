from collections import deque

def solution(queue1, queue2):
    deque1 = deque(queue1)
    deque2 = deque(queue2)
    
    limit = (len(deque1) + len(deque2)) * 2
    sum1 = sum(deque1)
    sum2 = sum(deque2)
    
    count = 0
    
    while True:
        if sum1 < sum2:
            temp = deque2.popleft()
            deque1.append(temp)
            
            # sum() 연산을 다시 하는 건 시간복잡도 손해
            sum2 -= temp
            sum1 += temp
            
            count += 1
            
        elif sum1 > sum2:
            temp = deque1.popleft()
            deque2.append(temp)
            
            sum1 -= temp
            sum2 += temp
            
            count += 1
            
        else:
            return count
        
        # 만약 두 deque 를 합친 길이만큼 넣었다 뺐다를 반복했는데도 안된다면
        # 그건 불가능한 경우
        if count >= limit:
            return -1