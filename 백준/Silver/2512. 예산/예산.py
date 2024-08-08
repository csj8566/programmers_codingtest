N = int(input())
budget = list(map(int, input().split()))
M = int(input())

# 돈의 범위
budget_range = [0, max(budget)] # 0~150

while (budget_range[0] <= budget_range[1]):

    search = (budget_range[0] + budget_range[1]) // 2 

    # 이번 턴에 나눠준 돈의 총합
    total = 0
    for i in budget:

        # 만약 필요한 예산이 search 이상이라면 search 까지만 분배받을 수 있음
        if search <= i:
            total += search
        
        # 필요한 돈이 search 미만이라면, 필요한 돈을 전부 분배받을 수 있음
        else:
            total += i

    # 만약 돈을 다 나눠줬는데도 국가예산이 남는다면
    if total <= M:
        # ex) 0~150 에서 75 나눠줬는데 돈 남음 -> 75~150 에서 search 를 재설정
        answer = search
        budget_range[0] = search + 1

    # 이대로 나눠주면 돈이 부족해.
    elif total > M:
        budget_range[1] = search - 1

print(answer)