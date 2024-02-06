# i번째 점원 탐색
# s: 현재까지의 탑 높이
def dfs(i, s):
    global N, B, top

    # 현재까지의 탑이 선반 이상인 경우 최솟값 비교
    if s >= B:
        top = min(top, s)
        return

    # 모든 점원을 탐색한 경우 끝내기
    if i == N:
        return

    # 현재 점원 선택
    dfs(i + 1, s + H[i])

    # 현재 점원 선택 X
    dfs(i + 1, s)

########################################################

# 테스트 케이스 수
T = int(input())
for t in range(1, T + 1):
    # 점원 수, 선반 높이
    N, B = map(int, input().split())

    # 점원들의 키 (정렬)
    H = sorted(list(map(int, input().split())))

    # 선반 높이 이상의 최소 탑 높이
    top = N * 10000

    # 점원 한 명씩 탐색
    dfs(0, 0)

    # (최소 탑 높이 - 탑 높이) 출력
    print(f'#{t} {top - B}')