from itertools import combinations

N, M = list(map(int, input().split()))

lst = [i+1 for i in range(N)]
# print(lst)

comb = combinations(lst, M)
# print(list(comb))

comb_list = list(comb)

for element in comb_list: #(1, 2)
    print(' '.join(list(map(str, element))))