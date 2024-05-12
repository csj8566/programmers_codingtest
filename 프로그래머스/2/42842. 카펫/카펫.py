def solution(brown, yellow):
    common = []
    
    for i in range(1, yellow+1):
        if yellow % i == 0:
            if i > (yellow / i):
                break
            common.append((i, int(yellow/i)))
    
    
    for j in common:
        height, width = j
        if height * 2 + width * 2 + 4 == brown:
            return [width+2, height+2]
