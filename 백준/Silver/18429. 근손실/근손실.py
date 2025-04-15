N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

answer = 0

def DFS(start, depth, visited):
  # 루트가 없는 DFS 
  global answer

  # 종료 조건 : N-1까지 내려왔을 때. 이 때는 무조건 되는 거니까 answer 에 + 1 한다, 그리고 return
  if depth == N-1:
    answer += 1
    return 

  # 만약 3, 7, 5 중에 visited 안 된 원소 있다면 걔로만 탐색 ㄱㄱ, 근데 탐색 안하는 경우는 start + 원소 - K 했는데 500보다 작아지는 경우
  for idx, i in enumerate(A): # 3, 7, 5
    # 이미 방문된 원소면 제낌
    if idx not in visited:
      next_state = start + i - K
      # 방문 안 된 원소인데 걔를 사용한 다음 상태가 500이상이면 걔로는 진행
      if next_state >= 500:
        visited.add(idx)
        # 다음 호출 진행
        DFS(next_state, depth + 1, visited)
        # 여기가 호출되는 순간은 백트래킹 해 줄 때임
        visited.remove(idx)


DFS(500, 0, set())
print(answer)