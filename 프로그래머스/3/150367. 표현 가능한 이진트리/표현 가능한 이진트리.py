def solution(numbers):
    answer = []
 
    # 분할 정복으로 자신의 부모를 나타내는 배열을 만들자
    def build_parents(lenght):
        
        if lenght == 1:
            return [-1]
        
        parents_lst = [-1 for _ in range(lenght)]
        mid = lenght // 2 
         
        def set_parents(start, end, parent):
            if start > end:
                return 
            
            mid = (start + end) // 2
            parents_lst[mid] = parent
            
            set_parents(start, mid-1, mid)
            set_parents(mid+1, end, mid)
            
        set_parents(0, lenght-1, -1)
        return parents_lst
    
    
    for number in numbers:
        binary = bin(number)[2:]
        
        # if 문을 통한 하드코딩 없이 더미코드 채워넣는 방법
        max_lenght = 1
        while max_lenght < len(binary):
            max_lenght = max_lenght * 2 + 1
        
        binary = binary.zfill(max_lenght)
        # print('binary', binary)
        
#         if 1 < len(binary) < 3:
#             binary = '0' + binary

#         elif 3 < len(binary) < 7:
#             binary = '0' * (7-len(binary)) + binary

#         elif 7 < len(binary) < 15:
#             binary = '0' * (15-len(binary)) + binary

#         elif 15 < len(binary) < 31:
#             binary = '0' * (31-len(binary)) + binary

#         elif 31 < len(binary) < 63:
#             binary = '0' * (63-len(binary)) + binary
           
        node = [int(i) for i in binary]    
        parents = build_parents(len(node))

        
        # 루트인 경우 빼먹어서 틀렸음! 추가해주니까 정답처리됨.
        for idx, num in enumerate(node):
            if num == 1 and node[parents[idx]] == 0 and parents[idx] != -1:
                answer.append(0)
                break
        else:
            answer.append(1)
                         
            
    return answer