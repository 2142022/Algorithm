import sys
input = sys.stdin.readline

# idx번째 숫자 하나씩 선택
# prev: 이전 숫자
# result: 현재까지의 식의 결과
def dfs(idx, prev, result):
    global max_result

    # 최종 식이 정해졌다면 최댓값 비교
    if idx == N:
        max_result = max(max_result, result)
        return

    # 다음 수 선택
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            now = A[i]
            if idx == 0:
                dfs(idx + 1, now, 0)
            else:
                dfs(idx + 1, now, result + abs(now - prev))
            visited[i] = 0

####################################################################

# 정수 개수
N = int(input())

# 배열
A = list(map(int, input().split()))

# 얻을 수 있는 식의 최댓값
max_result = 0

# 배열에서 선택한 값 체크
visited = [0] * N

# 숫자 하나씩 선택
dfs(0, 0, 0)

print(max_result)