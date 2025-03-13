def solution(land):
    answer = 0
    
    # 1. 메모이제이션 배열 만들기 : land 를 그대로 메모이제이션 배열로 활용한다.
    memo = land.copy()
    
    # 2. 시작 조건, 종료 조건 설정하기 : 모든 행을 다 돌면 종료
    # 0번째 행은 어차피 본인 스스로가 가능한 최대값이기 때문에 패스한다.
    # 1번째 행부터는 본인 열에서 가능한 최대값을 기재한다.
    for row_idx, row in enumerate(land):
        for col_idx, col in enumerate(row):
            
            # 0번째 행은 건너뛰기
            if row_idx == 0:
                continue
                
            # 1번째 행부터 본인이 될 수 있는 최대값을 계산
            # 0번째 행에서, 본인과 같은 열을 제외한 나머지 숫자 중 가장 큰 숫자랑 본인을 더함
            for prev_col_idx, prev_col in enumerate(land[row_idx - 1]):
                # print(prev_col_idx, prev_col)
                current_col = col
                
                # 3. 점화식 세우기
                if prev_col + current_col > land[row_idx][col_idx] and (prev_col_idx != col_idx):
                    land[row_idx][col_idx] = prev_col + current_col
                
    return max(land[-1])