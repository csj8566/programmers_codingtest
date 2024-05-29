# from heapq import heappush, heappop

def solution(number, k):
    initial_k = k
    
    answer = ''
    n = len(number)
    hq = []

    for idx, num in enumerate(number): # (0,1), (1,9), (2,2), (3,4)
        while k and hq and int(hq[-1]) < int(num):
            hq.pop()
            k -= 1
        hq.append(num)
    answer = ''.join(hq)
        
    if len(answer) > n - initial_k:
        return answer[:n-initial_k]
    
    return answer