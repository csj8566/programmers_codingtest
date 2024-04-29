from collections import deque

def solution(queue1, queue2):
    deque1 = deque(queue1)
    deque2 = deque(queue2)
    total_deque = deque1 + deque2
    sum_1 = sum(deque1)
    sum_2 = sum(deque2)
    
    limit = len(total_deque) * 2
    cnt = 0
    trial = 0
    while True:
        if sum_1 < sum_2:
            target = deque2.popleft()
            deque1.append(target)
            cnt += 1
            sum_1 += target
            sum_2 -= target
            trial += 1
        elif sum_1 > sum_2:
            target = deque1.popleft()
            deque2.append(target)
            cnt += 1
            sum_1 -= target
            sum_2 += target
            trial += 1
        else:
            return cnt
        if trial >= limit:
            return -1