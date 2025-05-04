N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sorted_A = sorted(A)
sorted_B = sorted(B, reverse=True)


def func1(A, B):
  
  answer = 0
  for idx, num in enumerate(A):
    answer += A[idx] * B[idx]
  
  return answer


answer = func1(sorted_A, sorted_B)
print(answer)