N, X = list(map(int, input().split()))

lst = [1] * N
total = N  # 초기값은 모두 1로 채워져 있으므로 total은 N과 같음
alp = []

def num_alp(num):
    if 1 <= num <= 26:
        return chr(num + 64)

if X < N or X > 26 * N:
    print('!')
else:
    for i in range(N):
        remaining = X - total  # 남은 값을 계산
        if remaining <= 0:
            break
        
        # 현재 위치에서 더할 수 있는 최대 값은 25(현재 1이 들어가 있으므로)
        add_value = min(25, remaining)
        lst[i] += add_value
        total += add_value  # total을 갱신
    
    for letter in lst:
        alp.append(num_alp(letter))
    
    alp.sort()
    print(''.join(alp))
