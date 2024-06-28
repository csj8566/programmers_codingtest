def solution(cap, n, deliveries, pickups):
    answer = 0
    
    remain_del = 0
    remain_pick = 0
    
    # 뒤에서부터 시작해야 최소한의 거리로 왔다갔다 할 수 있음
    # 만약 앞에서부터 고려한다면 쓸데없는 반복이 추가됨
    
    # deliveries와 pickups 배열을 반대로 뒤집으셈
    deliveries.reverse()
    pickups.reverse()
    
    # 이제 집 하나씩 돌 건데
    for i in range(n):
        
        # 한 집 당 해결해야하는 남은배달량, 수거량
        remain_del += deliveries[i]
        remain_pick += pickups[i] 
       
        # remain_del 이나 remain_pick 둘 중 하나라도 0 초과인 경우 계속 왔다갔다 해야함
        while (remain_del > 0) or (remain_pick > 0):
            
            # 트럭에는 최대 cap만큼 택배를 실어서 출발할 수 있음. 
            # remain_del 과 remain_pick은 음수여도 괜찮음. 음수인 동안은 answer에 거리안더함
            # 변수가 음수인 동안, i번째 집까지 오는 동안의 택배 업무를 한번에 모두 처리할수있단뜻 
            remain_del -= cap # 2
            remain_pick -= cap # 3
            answer += (n-i) * 2
    
    return answer