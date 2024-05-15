from itertools import combinations, product
from bisect import bisect_left, bisect_right

def solution(dice):
    answer = []
    n = len(dice)
    dic = {}

    dice_num = [i for i in range(n)] # [0,1,2,3]
    comb = list(combinations(dice_num, int(n/2)))
    # print(comb)
    
    for a_dice in comb: # (0, 1), (0, 2), ,,,,, (3,4)
        b_dice = tuple(set(dice_num) - set(a_dice)) # a_dice 를 제외한 나머지
        # print(a_dice, b_dice)
        
        # 눈의 합을 저장하기 위한 배열
        A = [] 
        B = []
        
        # 주사위의 눈의 인덱스를 구하는 거임
        for die in product([0,1,2,3,4,5], repeat=int(n/2)): # (0,0)
            # A라는 배열에다가 주사위 눈의 합을 저장해주셈. : 0번주사위의 0번째눈 + 1번주사위의 0번째 눈... 
            A.append(sum(dice[i][j] for i, j in zip(a_dice, die)))
            B.append(sum(dice[i][j] for i, j in zip(b_dice, die)))
            
        B.sort() # bisect를 하기 위해선 B가 오름차순 정렬돼있어야함
        # print(A, len(A))
        # print(B, len(B))
        
        # A에 들어있는 원소가 몇 번이나 B에 들어있는 원소를 이길 수 있는지를 전부 더한 변수 victory
        victory = sum(bisect_left(B, num) for num in A)
        dic[victory] = a_dice
    
    # A의 승률 가장 승률이 높은 경우를 찾아와야 함
    max_key = max(dic.keys()) 
    # print(dic[max_key]) # (0,3_     
            

    return [i+1 for i in dic[max_key]]



'''
n 은 주사위 개수
6**10=6천만;;; O(n)도 2천민까지임 ->log시간알고리즘 필요

이 문제는 걍 주사위 뽑고(itertools?) 비교만 하면 되는 문제임
근데 시간복잡도를 어떻게 줄이느냐가 문제-> 필요없는 연산을 줄일 수 있느냐 -> 이거 스택 문제에서 똑같은 내용 적었던 것 같은데?



bisect 사용

1. 주사위를 일단 나눠야 함 -> 반반 나누기 (이 반반도 combinations 써서)
2. 

'''