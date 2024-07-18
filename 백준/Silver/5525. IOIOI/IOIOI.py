N = int(input())
M = int(input())
S = input()
count = 0

# Pn 은 I 뒤에 OI 가 n 번 붙는 형태
Pn = 'I' + 'OI' * N
slide = len(Pn)  # 몇 칸씩 보면서 슬라이딩 해 갈지

# 해시 연습
mod = int(1e9 + 7)
base = 31

# 자리수 배열 생성
digit = [0] * slide
digit[0] = 1
for i in range(1, slide):
    digit[i] = digit[i-1] * base % mod

# Pn 해시 계산
Pn_hash = 0
for i in range(slide):
    if Pn[i] == 'I':
        Pn_hash = (Pn_hash + 9 * digit[i]) % mod
    elif Pn[i] == 'O':
        Pn_hash = (Pn_hash + 15 * digit[i]) % mod

# 첫 번째 슬라이딩 윈도우 해시 계산
S1 = 0
for i in range(slide):
    if S[i] == 'I':
        S1 = (S1 + 9 * digit[slide-1-i]) % mod
    elif S[i] == 'O':
        S1 = (S1 + 15 * digit[slide-1-i]) % mod

if S1 == Pn_hash:
    count += 1

current = S1  # 14308803.0

# 슬라이딩 윈도우를 이용한 해시 계산
for i in range(1, M - slide + 1):
    # 이전 수에서 가장 높은 자리수 빼주기
    current = (current - ((ord(S[i-1]) - ord('A') + 1) * digit[slide-1]) % mod + mod) % mod
    # 자리수 하나씩 앞으로 땡기기
    current = (current * base) % mod
    # 새로운 친구 더하기
    current = (current + (ord(S[i + slide - 1]) - ord('A') + 1)) % mod
    
    if current == Pn_hash:
        count += 1

print(count)
