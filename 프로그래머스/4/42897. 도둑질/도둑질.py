def solution(money):
    
    # 1.메모이제이션 : 현재 인덱스의 집까지 고려했을때 돈의 최댓값
    memo = [0 for _ in range(len(money))]
    
    
    # 2. 초기상태, 종료조건
    # 2-1. 첫 집을 터는 경우
    
    # 첫집 털음
    memo[0] = money[0]
    
    # 두번째집 못털음
    memo[1] = memo[0] 
    
    # 마지막집 못털음
    for i in range(2, len(money)-1):
        # 3. 점화식
        # 직전집을 털고 지금집을 못터는게 나은지, 지지난집을 털고 직전집 안털고 지금집 터는게 나은지
        memo[i] = max((memo[i-2] + money[i]), memo[i-1])
    temp_1 = max(memo)

    
    # 2-2. 첫 집 안터는 경우
    memo = [0 for _ in range(len(money))]
    memo[1] = money[1]
    for i in range(1, len(money)):
        # 3. 점화식
        memo[i] = max((memo[i-2] + money[i]), memo[i-1])
    temp_2 = max(memo)
        
    
    return max(temp_1, temp_2)