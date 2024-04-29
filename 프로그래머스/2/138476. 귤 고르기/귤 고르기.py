from collections import Counter

def solution(k, tangerine):
    tang_dict = Counter(tangerine)
    tang_length = []
    
    for i in tang_dict.values():
        tang_length.append(i)
        
    tang_length = sorted(tang_length, reverse = True)
    
    cnt = 0
    for idx, num in enumerate(tang_length, start = 1):
        cnt += num
        if cnt >= k:
            return idx
