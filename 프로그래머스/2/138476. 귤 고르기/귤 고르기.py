from collections import Counter, deque 

def solution(k, tangerine):
    answer = 0
    tan_counter = Counter(tangerine)
    # print(tan_counter)
    
    sorted_counter = tan_counter.items()
    # print(sorted_counter)
    
    sorted_counter = sorted(sorted_counter, key = lambda x : x[1], reverse=True)
    # print(sorted_counter)
    
    count = 0
    temp_list = []
    queue = deque(sorted_counter)
    while k > count:
        if not queue:
            continue
        tan, num = queue.popleft()
        for _ in range(num):
            temp_list.append(tan)
            count += 1
            
    temp_set = set(temp_list)
    
    return len(temp_set)


'''
한 박스에 들어가는 귤의 종류가 "최소"가 되게끔 -> 그리디

한 종류의 귤을 담는다 했을 때 최대한 그 같은 크기는 다 담는 게 좋음
그렇다면 정렬을 하는 게 좋겠네? key 는 개수로!

'''