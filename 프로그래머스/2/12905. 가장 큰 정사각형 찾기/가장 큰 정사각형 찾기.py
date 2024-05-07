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