def solution(alp, cop, problems):
    max_alp = 0
    max_cop = 0
    
    for row in problems:
        max_alp = max(max_alp, row[0])
        max_cop = max(max_cop, row[1])
        
    # 최댓값 넘어가는 건 최대값으로 되돌려줘야함
    # 시간 초과, 런타임 에러 방지 위함
    # 그러니까 시작부터 모든 문제를 풀기 위한 알고력이나 코딩력보다 큰 힘을 가지고 시작한다면, 가장 높은 알고력/코딩력 요구수치로 바꿔줌
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    
    # 999는 해당 상태에 도달할 수 없음을 의미. 큰 값으로 초기화
    dp = [[999] * (max_cop+1) for _ in range(max_alp+1)] # max_alp=20, max_cop=20 인 경우 21x21 배열
    dp[alp][cop] = 0 # 초기 알고력과 코딩력의 상태가 되기 위해 필요한 cost 는 0임 (시작지점이니까)
    # print(dp)
    
    for algo in range(alp, max_alp+1): # 10 ~ 20 
        for coding in range(cop, max_cop+1): # 10 ~ 20
            
            # 같은 경우에는 끝 인덱스라 인덱싱 에러 (+1 할 수가 없음)
            # cost 1 들여서 알고력이나 코딩력을 1 증가시키는 경우를 고려하는 부분
            if algo < max_alp:
                dp[algo+1][coding] = min(dp[algo+1][coding], dp[algo][coding] + 1)
            if coding < max_cop:
                dp[algo][coding+1] = min(dp[algo][coding+1], dp[algo][coding] + 1)
            
            # 같은 문제를 여러 번 풀 수 있음. 그러므로 매 (algo, coding) 상태마다 problems를 for문 돌려 판단.
            for problem in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
                
                # 문제를 풀 수 있는 상황
                if algo >= alp_req and coding >= cop_req:
                    # 최댓값 넘어가는 건 최대값으로 되돌려줘야함
                    new_algo = min(algo+alp_rwd, max_alp)
                    new_coding = min(coding+cop_rwd, max_cop)
                    
                    # dp[algo][coding] + cost는 원래 상태에서 주어진 문제를 푸는 경우
                    # dp[new_algo][new_coding]은 바뀐알고력/코딩력까지 도달하기 위한, 여태까지 계산된 최소 비용 
                    dp[new_algo][new_coding] = min(dp[algo][coding] + cost, dp[new_algo][new_coding])

    return dp[max_alp][max_cop]

