def solution(numbers):

    # -1 로만 구성된 배열 만들고 시작함.
    answer = [-1 for _ in range(len(numbers))]
    
    # 근데 이거 stack 문제같지 않음?
    stack = []
    # 조건이 만족되기 전까지는 다 stack에 보관해뒀다가
    # 조건이 만족되는 순간 stack 에서 pop 시키면 될 것 같은데.
    
    # numbers의 원소 하나씩 순회하면서
    for idx, number in enumerate(numbers):
        while stack and stack[-1][1] < number: # (만약 본인보다 큰 원소가 처음 나오면)
            # 그 '뒷 큰수'를 answer의 본인의 인덱스 자리에 넣어주셈
            temp_idx, temp_number = stack.pop()
            answer[temp_idx] = number
        # while stack 에서부터 틀려먹은 놈들은 여기부터 실행될듯
        stack.append((idx, number)) # 첫 원소는 무조건 여기부터 실행되겠네요.
        
    
    
    
    
    return answer
    