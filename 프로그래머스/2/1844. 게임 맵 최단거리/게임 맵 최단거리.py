from collections import deque

def solution(maps):
    answer = 0
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상 하 좌 우
    num_row = len(maps)
    num_col = len(maps[0])
    
    def BFS():
        visited = [[False] * num_col for _ in range(num_row)]
        queue = deque()
        visited[0][0] = True
        queue.append((0, 0, 1)) 
        
        while queue:
            current_row, current_col, cost = queue.popleft()
            # 종료 조건
            if current_row == (num_row - 1) and current_col == (num_col - 1):
                return cost
            
            for row_move, col_move in moves:
                next_row = current_row + row_move
                next_col = current_col + col_move
                
                # 갈 수 있는 칸인 경우
                if 0<=next_row<num_row and 0<=next_col<num_col and maps[next_row][next_col] == 1:
                    
                    # visited 절대 까먹지마!
                    if visited[next_row][next_col] == False:
                        visited[next_row][next_col] = True
                        queue.append((next_row, next_col, cost + 1))
                        
        return -1
                    
            
    
    return BFS()