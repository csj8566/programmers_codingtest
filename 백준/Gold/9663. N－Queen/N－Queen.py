N = int(input())
board = [[0] * N for _ in range(N)] 
answer = 0

def DFS(row, col_check, diag_1, diag_2): # diag_1 : 좌상-우하, diag_2 : 좌하-우상
    global answer

    # 종료조건 : 만약 끝 row 까지 다 돌아서 더 갈 데 없다면 그건 가능한 경우.
    if row == N:
        answer += 1    

    # 시작지점의 col은 N가지 가능 
    else:
        for col in range(N):
            # diag_1 : N=4일때, 인덱스 '1,2,3,4,5,6,7' 을 다루게 됨
            # diag_2 : N=4일때, 인덱스 '0,1,2,3,4,5,6' 을 다루게 됨

            # 만약 퀸이 있는 자리거나, 퀸의 공격을 받을 수 있는 자리라면 다음 탐색으로
            if col_check[col] or diag_1[row - col + N] or diag_2[row + col]:
                continue

            # 퀸을 놓을 수 있는 자리라면 퀸 놓기
            col_check[col] = diag_1[row - col + N] = diag_2[row + col] = True

            # 다음 행으로 (다음 레벨로) 이동
            DFS(row+1, col_check, diag_1, diag_2)

            # 백트래킹
            col_check[col] = diag_1[row - col + N] = diag_2[row + col] = False


    return answer 


# 여유롭게 N * 2 크기로 대각선 따지는 배열 설정함. N=4일때 7칸 필요함.
print(DFS(0, [False] * N, [False] * (N * 2), [False] * (N * 2))) 