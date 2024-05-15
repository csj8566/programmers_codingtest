from itertools import combinations, product
from bisect import bisect_left, bisect_right

def solution(dice):
    answer = []
    n = len(dice)
    dic = {}

    dice_num = [i for i in range(n)] # [0,1,2,3]
    comb = list(combinations(dice_num, int(n/2)))
    
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
        
        # A에 들어있는 원소가 몇 번이나 B에 들어있는 원소를 이길 수 있는지를 전부 더한 변수 victory
        victory = sum(bisect_left(B, num) for num in A)
        dic[victory] = a_dice
    
    # A의 승률 가장 승률이 높은 경우를 찾아와야 함
    max_key = max(dic.keys()) 
            

    return [i+1 for i in dic[max_key]]
