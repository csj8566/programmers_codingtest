N, K = list(map(int, input().split()))
lst = list(map(int, input().split()))

# 초기 K개의 합을 구합니다.
current_sum = sum(lst[:K])
max_sum = current_sum

# 슬라이딩 윈도우를 이용하여 다음 합들을 구합니다.
for i in range(1, N-K+1):
    current_sum = current_sum - lst[i-1] + lst[i+K-1]
    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)
