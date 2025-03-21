def solution(cap, n, deliveries, pickups):
    answer = 0
    
    d_remain = 0 # 배달할 거 얼마나 남았는지
    p_remain = 0 # 반납할 거 얼마나 남았는지
    
    for i in range(n-1, -1, -1): # 맨 뒤에서 처음까지
        d_remain += deliveries[i] # 현재 집에서는 배달할 거 얼마나 있는지 더해주기
        p_remain += pickups[i] # 현재 집에서는 반납할 거 얼마나 있는지 더해주기
        
        while (d_remain > 0) or (p_remain > 0): # 만약 배달할 거 / 반납할 거 -> 하나라도 남았다면
            d_remain -= cap
            p_remain -= cap
            answer += ((i + 1) * 2)
        
    
    return answer