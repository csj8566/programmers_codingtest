from collections import deque

def solution(maps):
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상 하 좌 우
    rows = len(maps) # 세로 길이
    cols = len(maps[0]) # 가로 길이
    
    def BFS():
        visited = set()
        # visited.add((0,0)) # 첫번째 위치를 방문처리 하고 시작하는지 아닌지 헷갈리네..아마 아닌듯
        queue = deque()
        queue.append( ((0,0), 1) ) 
        
        while queue:
            current_state, move_count = queue.popleft()
            current_row, current_col = current_state
            if (current_row, current_col) == (rows - 1, cols - 1):
                return move_count
            
            for row_move, col_move in moves:
                next_row, next_col = current_row + row_move, current_col + col_move
                
                # maps를 벗어나지 않고, 벽이 아닌 경우에만
                if (0 <= next_row < rows) and (0 <= next_col < cols) and (maps[next_row][next_col]) == 1:
                    if (next_row, next_col) not in visited:
                        visited.add((next_row, next_col))
                        queue.append( ((next_row, next_col), move_count + 1) )
                    
        return -1
        
    
    return BFS()