# idx행 탐색
def dfs(idx, sum):
    global N, min_sum

    # 모든 행을 탐색한 경우 끝내기
    if idx == N:
        min_sum = min(min_sum, sum)
        return

    # 현재까지의 합이 min_sum 이상인 경우 끝내기
    if sum >= min_sum:
        return

    # 현재 행에서 숫자 고르기
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(idx + 1, sum + nums[idx][i])
            visited[i] = 0

########################################################################

# 테스트 케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 배열 크기
    N = int(input())

    # 배열
    nums = [list(map(int, input().split())) for _ in range(N)]

    # N개의 숫자의 최소 합
    min_sum = 9 * N

    # 사용한 세로 줄(열) 체크
    visited = [0] * N

    # 한 줄씩 탐색
    dfs(0, 0)

    print(f'#{t} {min_sum}')