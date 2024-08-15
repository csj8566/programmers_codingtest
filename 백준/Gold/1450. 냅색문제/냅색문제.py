from itertools import combinations
from bisect import bisect_right 

# array 넣으면 부분집합 구하고 부분집합의 합의 list 반환하는 함수
# 두 부분에 대해서 가능한 모든 부분집합의 무게 합 구하기
def split_list(lst):
    result = []

    for i in range(len(lst) + 1): 
        for comb in combinations(lst, i):
            result.append(sum(comb))

    return result


def solution():

    # 입력 받기
    N, max_weight = list(map(int, input().split()))
    weights = list(map(int, input().split()))

    # 물건 리스트 두 부분으로 나누기
    left_weights = weights[:N//2]
    right_weights = weights[N//2:]

    left_weights = split_list(left_weights)
    right_weights = split_list(right_weights)

    # 오른쪽 배열은 이진탐색(bisect)을 위해서 정렬돼있어야 함
    right_weights.sort()

    # 왼쪽 부분집합의 합을 하나씩 탐색하면서
    count = 0
    
    for left in left_weights:
        if left <= max_weight:
            # 오른쪽 부분집합에서 c를 넘지 않는 최대 가능한 값 찾기
            count += bisect_right(right_weights, max_weight - left)
    
    return count

    
print(solution())