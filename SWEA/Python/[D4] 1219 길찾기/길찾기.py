# 노드 x에 연결된 노드 탐색
def dfs(x):
    # 이미 도착지점까지 방문한 경우 끝내기
    if visited[99]:
        return

    # 다음 노드 탐색
    for nx in connect[x]:
        if not visited[nx]:
            visited[nx] = 1
            dfs(nx)

########################################################3

# 10개의 테스트 케이스
for _ in range(10):
    # 테스트케이스 번호, 길의 총 개수
    t, E = map(int, input().split())

    # 모든 순서쌍
    info = list(map(int, input().split()))

    # 연결 정보
    connect = [list() for _ in range(100)]
    for i in range(E):
        a, b = info[2 * i], info[2 * i + 1]
        connect[a].append(b)

    # 방문 체크
    visited = [0] * 100
    visited[0] = 1

    # 연결된 노드 하나씩 방문
    dfs(0)

    print(f'#{t} {visited[99]}')