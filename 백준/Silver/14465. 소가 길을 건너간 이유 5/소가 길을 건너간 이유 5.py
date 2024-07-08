# import sys
# input = sys.stdin.readline

N, K, B = list(map(int, input().split()))
broken = [0] * N
for _ in range(B):
    broken[int(input()) - 1] = 1

psum = [0] * N
psum[0] = broken[0]
for i in range(1, N):
    psum[i] = psum[i-1] + broken[i]

# minimum = psum[K-1] # 3
min_lst = []

for i in range(0, N-K+1):
    if i == 0:
        min_lst.append(psum[K-1])
    else:
        min_lst.append(psum[K-1+i] - psum[i-1])
        # print(psum[K-1+i], psum[i-1])
print(min(min_lst))