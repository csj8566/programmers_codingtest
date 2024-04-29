def solution(park, routes):
    
    # S 의 위치 찾기
    row = [park.index(r) for r in park if 'S' in r] #[0]
    row = row[0]  # 0
    
    col = park[row].index('S') # 0
    
    first_row = row
    first_col = col
    
    # 명령문마다
    for i in routes:
        direction, n = i.split() # E, 2
        n = int(n)
        
        if direction == 'E':
            if len(park[row]) < col + n + 1:
                continue
            for _ in range(n): # 2칸 동쪽으로
                if park[row][col+1] == 'X':
                    col = first_col
                    break
                else:
                    col += 1
            first_col = col
            
        elif direction == 'W':
            if col - n < 0:
                continue
            for _ in range(n):
                if park[row][col-1] =='X':
                    col = first_col
                    break
                else:
                    col -= 1
            first_col = col
            
        elif direction == 'N':
            if row - n < 0:
                continue
            for _ in range(n):
                if park[row-1][col] == 'X':
                    row = first_row
                    break
                else:
                    row -= 1
            first_row = row
                    
        elif direction == 'S':
            if row + n + 1 > len(park):
                continue
            for _ in range(n):
                if park[row+1][col] == 'X':
                    row = first_row
                    break
                else:
                    row += 1
            first_row = row
                  
        
    return [row, col]


# n 의 숫자만큼 반복
#    알파벳 방향만큼 S를 한칸씩 옮기면서 O인지 x인지 확인
#    인덱스 벗어나면 그 반복문 continue / pass ? 하고 다음 알파벳 및 숫자 보기