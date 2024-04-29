import math

def solution(arrayA, arrayB):
    answer = 0
    
    def compare(A, B, answer):
        temp_A = A[0]
        for i in A:
            temp_A = math.gcd(temp_A, i)

        if 0 in [elem % temp_A for elem in B]:
            pass
        else:
            answer = max(answer, temp_A)
        
        return answer
    
    answer = compare(arrayA, arrayB, answer)
    answer = compare(arrayB, arrayA, answer)
    

    return answer