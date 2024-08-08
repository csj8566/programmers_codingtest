from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
questions = list(map(int, input().split()))

cards = Counter(cards)
answer = []

for card in questions:
    if card in cards:
        answer.append(cards[card])
    else:
        answer.append(0)

print(' '.join(map(str, answer)))