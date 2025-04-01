from copy import deepcopy

N = int(input())
tri = []

for _ in range(N):
  row = list(map(int, input().split()))
  tri.append(row)

dp = deepcopy(tri)


for row_idx, row in enumerate(tri):
  for col_idx, col in enumerate(row):
    
    # 맨 마지막 행
    if row_idx == N-1:
      break

    dp[row_idx + 1][col_idx] = max(dp[row_idx][col_idx] + tri[row_idx + 1][col_idx], dp[row_idx + 1][col_idx])
    dp[row_idx + 1][col_idx + 1] = max(dp[row_idx][col_idx] + tri[row_idx + 1][col_idx + 1], dp[row_idx + 1][col_idx + 1])

print(max(dp[-1]))  