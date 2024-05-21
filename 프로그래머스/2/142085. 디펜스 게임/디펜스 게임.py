from heapq import heappop, heappush

def solution(n, k, enemy):
    answer = 0
    enemy_sum = 0
    hq = []
    
    for i in enemy:
        heappush(hq, -i)
        enemy_sum += i
        
        if n < enemy_sum:
            if k:
                k -= 1
                mzq = heappop(hq)
                enemy_sum += mzq
            else:
                break
        
        answer += 1
        
    
    
    return answer


'''
평상시에는 그냥 진행을 하고 -> 만약에 계산 한 뒤에 enemy_sum 이 n보다 커지면 그때 무적권을 고려함
'''