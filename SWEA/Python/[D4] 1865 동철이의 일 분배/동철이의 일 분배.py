# 한 사람씩 일 분배
# i: 현재 사람
# p: 현재까지의 성공 확률
def dfs(i, p):
    global maxp

    # 이미 최대 성공 확률보다 적은 경우 패스
    if p < maxp:
        return

    # 모든 일 분배가 끝난 경우, 최대 성공 확률 비교
    if i == N:
        maxp = p
        return

    # 일 선택
    for j in range(N):
        if not visited[j] and success[i][j] != 0:
            visited[j] = 1
            dfs(i + 1, p * success[i][j])
            visited[j] = 0

#################################################################################################

# 테스트 케이스 수
T = int(input())
for t in range(1, T + 1):
    # 직원 및 일 수
    N = int(input())

    # 성공 확률
    success = [list(map(lambda x: int(x) / 100, input().split())) for _ in range(N)]

    # 분배된 일 체크
    visited = [0] * N

    # 최대 성공 확률
    maxp = 0

    # 한 사람씩 일 분배
    dfs(0, 1)

    print(f'#{t} {100 * maxp:.6f}')