def solution(money):
    max_money = 0
    
    # 1. dp 배열
    # dp[i] 의 의미 : 현재 인덱스의 집까지 털었을 때 얻을 수 있는 최대 금액
    dp1 = [0 for _ in range(len(money))]
    dp2 = [0 for _ in range(len(money))]
    
    # 2. 시작 / 종료 조건 : 모든 마을을 한 번씩 시작포인트로 삼는다.
    # 2-1. 시작 집을 터는 경우 : 마지막 집과 인덱스 1번째 집을 털 수 없다.
    dp1[0] = money[0]
    dp1[1] = money[0] # 어차피 인덱스 1번째 집은 털 수 없음
    
    # 3-1. 점화식
    for i in range(2, len(money) - 1): # 인덱스 2번째 집 ~ 마지막에서 두 번째 집
        # 인덱스 2번째 집부터 판단 시작
        # 지금 집을 터는 게 이득임? 아니면 여기 안털고 이전 집 터는 게 이득임?
        dp1[i] = max(money[i] + dp1[i - 2], dp1[i - 1])
        
    max1 = max(dp1)
    
    # 2-2. 첫 번째 집을 안 턴다 : 마지막 집을 털 수 있는 옵션이 생긴다
    dp2[0] = 0
    dp2[1] = money[1] # 첫 번째 집을 안털었으니까 두 번째 집은 터는 게 최대값임
     
    for i in range(2, len(money)):
        # 지금 집을 털고 이전 집을 안 터는 게 나음? 아니면 지금 집을 안 털고 이전 집을 터는 게 나음?
        dp2[i] = max(money[i] + dp2[i - 2], dp2[i - 1])
        
    max2 = max(dp2)
    
    
    return max(max1, max2)
