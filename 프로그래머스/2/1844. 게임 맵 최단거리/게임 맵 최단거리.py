from collections import deque

def solution(maps):
    answer = 0
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    num_rows = len(maps)
    num_cols = len(maps[0])
    
    def BFS():
        visited = [[False] * num_cols for _ in range(num_rows)]
        queue = deque()
        visited[0][0] = True
        queue.append((0, 0, 1))
        
        while queue:
            current_row, current_col, count = queue.popleft()
            
            # 종료 조건
            if current_row == num_rows - 1 and current_col == num_cols - 1:
                return count
            
            for row_move, col_move in moves:
                next_row = current_row + row_move
                next_col = current_col + col_move
                
                if 0<=next_row<num_rows and 0<=next_col<num_cols and maps[next_row][next_col] == 1:
                    if visited[next_row][next_col] == False:
                        visited[next_row][next_col] = True
                        queue.append((next_row, next_col, count+1))
                        
        return -1
        
    
    
    return BFS()