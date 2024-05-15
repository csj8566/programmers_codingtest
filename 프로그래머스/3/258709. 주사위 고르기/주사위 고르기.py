from itertools import product, combinations
from bisect import bisect_left

def solution(dice):
    n = len(dice) # 4
    
    # 최대 승률을 뽑아내는 주사위 조합을 고르기 위해 key가 승리회수고, value가 그때의 A의 주사위 조합인 딕셔너리를 만듦
    dic = {}
    
    # 주사위를 고르는 경우의 수를 전부 쪼개주셈
    for dice_of_A in combinations([i for i in range(n)], n//2): # 이제 그 모든 경우의 수를 하나씩 돌건데
        dice_of_B = list(set([i for i in range(n)]) - set(dice_of_A)) # A의 주사위와 b 주사위 상태 확인
        
        # 이제 주사위들별로 나온 눈을 고려해서 A가 갖고 있는 주사위 눈의 합 vs B~~~ 를 비교해야 함
        # 근데 그러기 위해선 주사위 눈의 경우의 수도 구해야 함
        # 두 개씩 나눠가졌으니 6x6 = 36가지가 나오겠네, 한사람당!
        
        # A가 가진 주사위로 나올 수 있는 주사위 눈의 총 합의 경우의 수, B~~~~~
        A = []
        B = []
        
        for die in product([0,1,2,3,4,5], repeat=n//2): # 한 주사위당 경우의 수 6가지 & 한 사람당 주사위 2번씩
            A.append(sum(dice[i][j] for i, j in zip(dice_of_A, die))) # A라는 배열에 36개의 원소가 들어감.
            B.append(sum(dice[i][j] for i, j in zip(dice_of_B, die))) # B도 마찬가지  
        
        # print(A)
        # print(B)
        # break
        
        # bisect 쓰기 위해서 B를 오름차순 정렬
        B.sort()
        
        # A에서 원소 하나씩 꺼내면서 걔는 승률이 얼마나 되는지를 구해서 A가 이기는 경우의 수를 구한다
        victory = sum(bisect_left(B, num) for num in A)
        
        dic[victory] = dice_of_A # (0,1)
        
    max_key = max(dic.keys())
         
        
    return [i+1 for i in dic[max_key]]