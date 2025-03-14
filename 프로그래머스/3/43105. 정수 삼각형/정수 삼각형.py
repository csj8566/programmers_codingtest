from copy import deepcopy

def solution(triangle):
    answer = 0
    
    # 1. 메모이제이션 배열 
    # 이 문제는 깊은 복사된 별도의 배열이 필요하다!
    memo = deepcopy(triangle)
    
    # 2. 시작 / 종료 조건 : 맨 마지막 행까지 내려가는 것
    # 왼쪽 아래로 내려가는 것 : 행 하나 더하기
    # 오른쪽 아래로 내려가는 것 : 행 하나 더하기 + 열 하나 더하기
    for row_idx, row in enumerate(triangle):
        for col_idx, col in enumerate(row):
            
            # 만약 마지막 행이면 볼 게 없으니까 그만
            if row_idx == len(triangle) - 1:
                break
            
            # 3. 점화식
            # 왼쪽 아래의 memo 값은 현재 왼쪽 아래의 memo 값과, 
            # memo의 지금 값 + triangle의 왼쪽 아래 값을 합한 값 중 큰 값으로 가야 한다
            memo[row_idx + 1][col_idx] = max(memo[row_idx + 1][col_idx], memo[row_idx][col_idx] + triangle[row_idx + 1][col_idx])
            
            # 오른쪽 아래도 마찬가지 방식
            # 근데 오른쪽 끝이면 지나쳐야 함
            if col_idx == len(triangle[-1]) -1:
                continue
            memo[row_idx + 1][col_idx + 1] = max(memo[row_idx + 1][col_idx + 1], memo[row_idx][col_idx] + triangle[row_idx + 1][col_idx + 1])
                
    # 거쳐간 숫자의 최댓값 return
    # 마지막 행만 보면 되겠지?             
    return max(memo[-1])