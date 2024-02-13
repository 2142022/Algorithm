# 이동하기
# i: 위치, s: 크기, t: 시간
def dfs(i, s, t):
    global max_size

    # 제한 시간이거나 끝 지점까지 도달한 경우 끝내기
    if t == M or i == N:
        max_size = max(max_size, s)
        return

    # 밀기
    dfs(i + 1, s + v[i + 1], t + 1)

    # 차기
    if i + 2 <= N:
        dfs(i + 2, s // 2 + v[i + 2], t + 1)

#######################################################

# 테스트케이스 개수
T = int(input())
for tc in range(1, T + 1):
    # 구간 길이, 제한 시간
    N, M = map(int, input().split())

    # 각 칸의 값
    v = [0] + list(map(int, input().split()))

    # M초 내에 만들 수 있는 최대 크기
    max_size = 1

    # 이동하기
    dfs(0, 1, 0)

    print(f'#{tc} {max_size}')