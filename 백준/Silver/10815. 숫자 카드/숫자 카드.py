N = int(input())
cards = list(map(int, input().split()))
M = int(input())
questions = list(map(int, input().split()))

cards = set(cards)
answer = []
for card in questions:
    if card in cards:
        answer.append(1)
    else:
        answer.append(0)

print(' '.join(map(str, answer)))