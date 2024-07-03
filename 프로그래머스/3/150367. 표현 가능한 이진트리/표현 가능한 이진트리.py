def solution(numbers):
    answer = []
    # print(len(bin(10**15)) - 2)
    # print(bin(95))
    # print(bin(5))
    # print(len(bin(10**15)))
    
    
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
        # print(binary)
        # print()
        
        
        if 1 < len(binary) < 3:
            binary = '0' + binary

        elif 3 < len(binary) < 7:
            binary = '0' * (7-len(binary)) + binary

        elif 7 < len(binary) < 15:
            binary = '0' * (15-len(binary)) + binary

        elif 15 < len(binary) < 31:
            binary = '0' * (31-len(binary)) + binary

        elif 31 < len(binary) < 63:
            binary = '0' * (63-len(binary)) + binary
        
        # print('binary', binary)

        # 이제 더미 노드가 다 채워짐.    
    
        node = [int(i) for i in binary]    
        parents = build_parents(len(node))
        # print('node', node)
        # print('parents', parents)
        
        # node를 하나씩 돌면서 node == 1인데 node[parents[node의 인덱스]] == 0 이면 만들 수 없는거임 (자식은 더미가 아닌데 부모가 더미다? 안되는거지)
        for idx, num in enumerate(node):
            if num == 1 and node[parents[idx]] == 0 and parents[idx] != -1:
                answer.append(0)
                break
        else:
            answer.append(1)
                
                
            
    return answer


'''
중위 순회

5는 왜안됨? -> 루트가 0이 돼서. 
만약 이진수 숫자 부분의 길이가 짝수면 맨앞에 0을 다음과 같은 길이로 만들 수 있어야 함
1(1), 3(1+2), 7(1+2**2), 15(2**0 + 2**1 + 2**2 + 2**3), 31, 63
트리가 이 길이들이 되도록 어떻게 검사하지?
10**15 를 이진법으로 표현하면 50자리가 필요 -> 63자리까지만 있으면 되네

리프가 1인데 걔의 부모가 0이면 만들 수 없음

높이 3인 포화완전이진트리의 경우 0, 2, 4, 6번째가 리프노드
1이 0과 2의 부모, 5가 4와6의 부모, 3이루트

node =    [0, 1, 0, 1, 0, 1, 0]
parents = [1, 3, 1, -1, 5, 3, 5]

node를 하나씩 돌면서 node == 1인데 node[parents[node의 인덱스]] == 0 이면 만들 수 없는거임 (자식은 더미가 아닌데 부모가 더미다? 안되는거지) 

node 배열은 완성했는데 parents 배열은 어떻게 만들지?
-> 분할 정복으로 완성할 수 있겠다!
'''