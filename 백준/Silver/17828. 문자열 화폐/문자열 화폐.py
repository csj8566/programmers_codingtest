N, X = list(map(int, input().split()))

lst = [1] * N
total = 1 * N
alp = []

def num_alp(num):
    if 1 <= num <= 26:
        return chr(num + 64)


if (X < N) or X > (26 * N):
    print('!')

else:
    for i in range(N): # 0~5 (총 6번)
        remaining = X - total
        if remaining <= 0:
            break

        add_value = min(25, remaining)
        total += add_value
        lst[i] += add_value
        

    # print(lst)
    for letter in lst:
        alp.append(num_alp(letter))

    alp.sort()
    print(''.join(alp))