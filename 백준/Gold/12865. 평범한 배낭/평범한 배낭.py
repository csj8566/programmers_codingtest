N, K = list(map(int, input().split())) # 4, 7
dp = [0 for _ in range(K+1)]

for _ in range(N):
    W, V = list(map(int, input().split())) # 6, 13 / 4, 8 / 3, 6 / 5, 12
    new_dp = dp[:]  # 기존 dp 배열을 복사하여 새로운 배열 생성

    for i in range(W, K+1):
        new_dp[i] = max(dp[i], dp[i-W] + V)

    dp = new_dp  # 새로운 dp 배열로 갱신

print(max(dp))
