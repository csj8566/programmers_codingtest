n = int(input())
nums = list(map(int, input().split()))
dp = [1] * n  # 모든 위치에서 최소 길이 1로 초기화

for i in range(n):
    for j in range(i):
        # 현재 값이 이전 값보다 크고, 더 긴 부분 수열을 만들 수 있는 경우
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
