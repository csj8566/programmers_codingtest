EMPTY = 0
AVAILABLE = 1

def solution(board, aloc, bloc):
    ar, ac = aloc
    br, bc = bloc
    _, count = play(board, ar, ac, br, bc)
    return count


# 현재 플레이어 좌표 : r1, c1
# 상대 플레이어 좌표 : r2, c2
def play(board, r1, c1, r2, c2):
    # 만약 현재 위치가 빈 발판이라면 패배
    if board[r1][c1] == EMPTY:
        return False, 0
    
    # 지나간 곳은 빈 발판이 됨
    board[r1][c1] = EMPTY
    
    R = len(board)
    C = len(board[0])
    
    # 이기는 경우 (누가 이기든 상관없음) 최소한의 이동거리로 이겨야 함
    min_win = float('inf')
    
    # 지는 경우 최대한의 이동거리동안 버텨야 함
    max_lose = 0
    
    # 다음 위치를 오프셋으로 구현
    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        nr, nc = r1 + dr, c1 + dc
        
        # board 범위를 벗어나지 않았고 빈 발판이 아니어야 이동 가능
        if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == AVAILABLE:
            
            # 재귀호출 : 상대 플레이어가 이기면 현재 플레이어가 지는 거임
            lose, count = play(board, r2, c2, nr, nc)
            
            # 호출별로 이기고 지는 경우를 따져서 max_lose, min_win을 경우에 따라 최신화
            # 만약 현재 플레이어가 졌다면 -> 최대한 오래버텨야 함.
            if lose:
                max_lose = max(max_lose, count + 1)
            # 만약 현재 플레이어가 이겼다면 -> 최대한 빨리 이겨야 함
            else:
                min_win = min(min_win, count + 1)
    # 백트래킹
    board[r1][c1] = AVAILABLE
    
    # 현재 플레이어 (A가 될 수도 있고 B가 될 수도 있음)
    # 만약 현재 플레이어가 이기는 경우가 하나라도 있다면
    if min_win < float('inf'):
        return True, min_win
    
    # 현재 플레이어가 이길 수 없다면
    else:
        return False, max_lose
                    