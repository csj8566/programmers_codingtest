from collections import Counter

N = int(input())
tang = list(map(int, input().split()))

start = 0
max_length = 0
current_count = Counter()

for end in range(N):
    current_count[tang[end]] += 1

    while len(current_count) > 2:
        current_count[tang[start]] -= 1
        if current_count[tang[start]] == 0:
            del current_count[tang[start]]
        start += 1
    
    max_length = max(max_length, end - start + 1)

print(max_length)