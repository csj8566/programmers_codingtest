def solution(number, k):
    stack = []
    for num in number:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    
    # 아직 제거해야 할 숫자가 남아있는 경우 뒤에서부터 제거
    while k > 0:
        stack.pop()
        k -= 1

    return ''.join(stack)