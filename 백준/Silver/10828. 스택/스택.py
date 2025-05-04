import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

stack = []

for _ in range(N):
  com = input()

  if com.startswith('push'):
    _, num = com.split()
    stack.append(num)

  elif com.startswith('pop'):
    if stack:
      temp = stack.pop()
      print(temp)

    else:
      print(-1)

  elif com.startswith('size'):
    print(len(stack))

  elif com.startswith('empty'):
    if not stack:
      print(1)

    else:
      print(0)

  elif com.startswith('top'):
    if stack:
      print(stack[-1])

    else:
      print(-1)