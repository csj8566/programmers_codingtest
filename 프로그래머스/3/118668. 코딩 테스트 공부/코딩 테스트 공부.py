def solution(alp, cop, problems):
    answer = 0
    max_alp = 0
    max_cop = 0
    
    for row in problems:
        max_alp = max(max_alp, row[0])
        max_cop = max(max_cop, row[1])
        
    # 최댓값 넘어가는 건 최대값으로 되돌려줘야함
    # 시간 초과, 런타임 에러 방지 위함
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
            
    dp = [[999] * (max_cop+1) for _ in range(max_alp+1)]
    dp[alp][cop] = 0
    print(dp)
    
    for algo in range(alp, max_alp+1):
        for coding in range(cop, max_cop+1):
            # 같은 경우에는 끝 인덱스라 인덱싱 에러
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
                    dp[new_algo][new_coding] = min(dp[algo][coding] + cost, dp[new_algo][new_coding])

    return dp[max_alp][max_cop]

