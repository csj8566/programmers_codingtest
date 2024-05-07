def solution(board):
    memoization = board
    height = len(board)
    width = len(board[0])
    maximum = 0
    
    for i in range(1, height):
        for j in range(1, width):
            if memoization[i][j] >= 1 and memoization[i-1][j] >= 1 and memoization[i][j-1] >= 1 and memoization[i-1][j-1] >= 1:
                memoization[i][j] = min(memoization[i-1][j], memoization[i][j-1], memoization[i-1][j-1]) + 1
                
    for row in memoization:
        for col in row:
            if col > maximum:
                maximum = col

    
    return maximum**2
    

'''
어떻게 접근해야하지? BFS/DFS?, 그리디? -> DP!

넓이가 1 -> 4 -> 9 -> 16 이런식으로 늘어날것
(한 변의 길이가 1 -> 2 -> 3 -> 4 이런식으로 늘어날것)


DP 3step

1. 메모이제이션 배열 초기화 : board 그 자체를 메모이제이션 배열로 사용
2. 종료 조건 설정(더 이상 쪼개지지 않는 경우) : 맨 마지막 인덱스까지 도닥
3. 점화식 세우고 반복문 or 재귀 구현 : ~~

첫번째 행과 첫번째 열은 1이면 1x1 정사각형 생성 가능, 0이면 정사각형 생성 불가능

(1,1) 부터 왼쪽, 위쪽, 왼쪽위대각선 다 체크해서 1 이상이면 1x1보다 더 큰 정사각형 생성 가능. 이때 크기가 얼마인지는 왼쪽, 위쪽, 왼쪽위대각선 중 가장 작은 것 + 1이다. 
'''