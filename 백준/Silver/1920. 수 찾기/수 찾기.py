from collections import Counter

N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
questions = list(map(int,input().split()))

numbers = Counter(numbers)
for i in questions:
    print(int(i in numbers))