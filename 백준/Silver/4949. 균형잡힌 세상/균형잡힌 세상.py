import sys
input = sys.stdin.read

lst = input().splitlines()

for line in lst:
    if line == '.':
        break
    stack = []
    for i in line:
        if i == '(' or i == '[':
            stack.append(i)
        elif stack and stack[-1] == '(' and i == ')':
            stack.pop()
        elif stack and stack[-1] == '[' and i == ']':
            stack.pop()
        elif not stack and (i == ')' or i == ']'):
            print('no')
            break
        elif stack and stack[-1] == '(' and i == ']':
            print('no')
            break
        elif stack and stack[-1] == '[' and i == ')':
            print('no')
            break
    else:
        if not stack:
            print('yes')
        else:
            print('no')
