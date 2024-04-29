def solution(keymap, targets):
    answer = []
    alphabet_number = dict()

    for row in keymap:  # 'ABACD'부터 'BCEFD' 까지
        for idx, alphabet in enumerate(row): # 0, 'A' / 1, 'B' / 2, 'A' / 3, 'C' / 4, 'D'
            if alphabet in alphabet_number and (idx+1) > alphabet_number[alphabet]:
                continue
            alphabet_number[alphabet] = idx+1 # {'A':1, 'B':1, 'C':2','D':5, 'E':3, 'F':4}

    for row in targets:  # "ABCD"부터 "AABB"까지
        cnt = 0
        for alphabet in row: #'A', 'B','C','D' / 'A','A','B','B'
            if alphabet in alphabet_number:
                cnt += alphabet_number[alphabet]
            else:
                cnt = -1
                break
        answer.append(cnt)        
    return answer