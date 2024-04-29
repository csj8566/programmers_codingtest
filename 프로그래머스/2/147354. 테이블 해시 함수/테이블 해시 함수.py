def solution(data, col, row_begin, row_end):
    data = sorted(data, key=lambda x:(x[col-1], -x[0]))
    hash_list = [[] for _ in range(row_end-row_begin+1)]

    for idx, row_idx in enumerate(range(row_begin-1, row_end)): # 1, 2
        for elem in data[row_idx]: # 2, 2, 6 / 1, 5, 10
            hash_list[idx].append(elem % (row_idx+1)) #[[0,0,0], [1,2,1]]
    
    hash_list = [sum(i) for i in hash_list]
    xor = 0
    
    for num in hash_list: # 0 , 4
        xor = xor ^ num
    
    return xor

# 	[[4, 2, 9], 
#    [2, 2, 6], 
#    [1, 5, 10], 
#    [3, 8, 3]]


'''
[[2,2,6],          [[4,2,9],
 [1,5,10],  -->     [2,2,6],  -> 2로 나누면 나머지가 0 0 0 -> 0
 [4,2,9],           [1,5,10], -> 3으로 나누면 나머지가 1 2 1 -> 4
 [3,8,3]]           [3,8,3]]


[2,
 1,
 4,
 3] 이 튜플끼리의 중복을 피하게 하는 '기본키'


'''