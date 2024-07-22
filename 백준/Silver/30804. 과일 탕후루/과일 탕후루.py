from collections import Counter

N = int(input())
tang = list(map(int, input().split()))

start = 0
max_length = 0
types_dict = Counter()

for end in range(N):
    types_dict[tang[end]] += 1

    # 현재 윈도우에 포함된 과일 종류가 2를 초과하면 윈도우를 축소
    while len(types_dict) > 2:
        types_dict[tang[start]] -= 1
        if types_dict[tang[start]] == 0:
            del types_dict[tang[start]]
        start += 1

    # 최대 길이를 갱신
    max_length = max(max_length, end - start + 1)

print(max_length)
