K = int(input())

stack = []
for _ in range(K):
    num = int(input())
    if num != 0:
        stack.append(num)
    elif stack and num == 0:
        stack.pop()

print(sum(stack))