def solution(brown, yellow):
    # answer = []
    common = []
    
    for i in range(1, yellow+1):
        if yellow % i == 0:
            if i > (yellow / i):
                break
            common.append((i, int(yellow/i)))
    print(common)
    
    
    for j in common:
        height, width = j
        if height * 2 + width * 2 + 4 == brown:
            return [width+2, height+2]



'''
- yellow 가 너무 큼 -> yellow 가 시간복잡도에 만약에 관여한다면, O(N) 안에 풀어야 함.
-> yellow 가 2백만인 이유 : 가로길이가 세로 길이보다 크기 때문에 탐색을 절반만 하면 됨. 즉, 2백만 다 할 필요 없고 100만까지만 하면 됨. 그러면 NlogN 도 가능할듯?



- 정사각형이거나, 가로로 긴 직사각형임

- brown + yellow 해가지고 만들 수 있는 사각형 다 해보기
ex) 10 + 2 = 12 -> 1x12, 2x6, 3x4 (여기까지!)

48

1x48, 2x24, 3x16, 4x12, 6x8

(brown 개수) == (yello 직사각형의 (가로x2 + 세로x2 + 꼭다리 4개)) 
'''