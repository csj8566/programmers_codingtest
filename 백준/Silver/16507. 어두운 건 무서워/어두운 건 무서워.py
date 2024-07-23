import sys
input = sys.stdin.readline

R, C, Q = list(map(int, input().split()))

# print(R, C, Q)
photo = [[0] * C for _ in range(R)]
psum = [[0] * C for _ in range(R)]

for row_idx in range(R):
    temp_list = list(map(int, input().split()))

    for col_idx, col in enumerate(temp_list):
        photo[row_idx][col_idx] = col

for row_idx in range(R):
    for col_idx in range(C):
        if col_idx == 0:
            psum[row_idx][col_idx] = photo[row_idx][col_idx]

        else:
            psum[row_idx][col_idx] = psum[row_idx][col_idx-1] + photo[row_idx][col_idx]
            

for _ in range(Q):
    r1, c1, r2, c2 = list(map(int, input().split())) # 2, 2, 4, 5
    temp = 0
    for i in range(r1-1, r2):
        if c1 >= 2:
            temp += (psum[i][c2-1] - psum[i][c1-2])  # (1,4) (1, 1)
        else: # c1 이 1인 경우
            temp += psum[i][c2-1]

    temp = temp // ((r2-r1+1) * (c2-c1+1))

    print(temp)