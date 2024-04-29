def solution(wallpaper):
    
    dict_index = {'top':-1, 'left':-1, 'bottom':-1, 'right':999}
    
    for row_idx, row in enumerate(wallpaper):
        
        if '#' in row:
            if dict_index['top'] == -1:
                dict_index['top'] = row_idx
            dict_index['bottom'] = row_idx
            
        elif '#' not in row: # else? -> else로 해도 당연히 정답
            continue # 이러면 쓸데없이 안쪽for문 안돌겠지?
            
        for col_idx, col in enumerate(row):
            if col == '#':
                if dict_index['left'] == -1 or col_idx < dict_index['left']:
                    dict_index['left'] = col_idx
                if dict_index['right'] == 999 or col_idx > dict_index['right']: 
                    dict_index['right'] = col_idx
                
            
    return [dict_index['top'], dict_index['left'], dict_index['bottom']+1, dict_index['right']+1]