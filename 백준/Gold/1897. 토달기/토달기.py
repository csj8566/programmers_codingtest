import sys
input = sys.stdin.readline

from collections import deque

#  입력 받기
d, start = input().strip().split()
d = int(d)

# 사전 만들기
dic = set()

for _ in range(d):
    word = input().rstrip()
    dic.add(word)

# 알파벳 탐색용
alphabet = 'abcdefghijklmnopqrstuvwxyz'


def next_word(word, dic, alphabet):
    possible_list = []

    for i in range(len(word) + 1): # 4
        if i == 0:
            for letter in alphabet:
                next = letter + word
                if next in dic:
                    possible_list.append(next)
        elif i == len(word): # 3
            for letter in alphabet:
                next = word + letter
                if next in dic:
                    possible_list.append(next)
        else: # 1, 2
            for letter in alphabet:
                next = word[:i] + letter + word[i:]
                if next in dic:
                    possible_list.append(next)           


    return possible_list


def BFS(start):
    queue = deque()
    queue.append(start)
    visited = set()
    # visited.add(start)

    answer = ''

    while queue:
        word = queue.popleft()
        if word not in visited:
            visited.add(word)
            answer = word
            queue.extend(next_word(word, dic, alphabet))

    else:
        return answer
    
print(BFS(start))

