def solution(numbers):
    answer = -1
    num_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    print(num_set - set(numbers))
    
    temp = num_set - set(numbers)
    return sum(temp)