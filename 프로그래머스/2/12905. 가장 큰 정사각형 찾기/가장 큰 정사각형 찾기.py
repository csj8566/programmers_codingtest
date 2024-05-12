def solution(board):
    answer = 0
    memo = board
    height = len(memo)
    width = len(memo[0])
    maximum = 0
    
    for row in range(1, height):
        for col in range(1, width):
            if memo[row][col] == 1 and memo[row][col-1] >= 1 and memo[row-1][col] >= 1 and memo[row-1][col-1] >= 1:
                memo[row][col] = min(memo[row][col-1], memo[row-1][col], memo[row-1][col-1]) + 1

    for i in memo:
        for j in i:
            if j > maximum:
                maximum = j

    return maximum ** 2
