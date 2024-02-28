import sys
input = sys.stdin.readline

# 문자열 S[0][l0:r0]을 문자열 S[1][l1:r1]으로 바꾸는데 필요한 최소 편집 거리 구하기
# k: 문자열 뒤집은 여부
def get_dist(k, l0, r0, l1, r1):
    # 초기화
    for i in range(l1 - 1, r1):
        dp[k][i] = i - l1 + 1

    for i in range(l0, r0):
        dp[k + 1][l1 - 1] = i - l0 + 1
        for j in range(l1, r1):
            # 같은 문자인 경우
            if S[k][i] == S[k + 1][j]:
                dp[k + 1][j] = dp[k][j - 1]
            # 다른 문자인 경우
            else:
                dp[k + 1][j] = min(dp[k][j - 1], dp[k][j], dp[k + 1][j - 1]) + 1
        dp[k][l1 - 1:r1] = dp[k + 1][l1 - 1:r1]

##########################################################################################################

# 문자열 S[0][l0:r0]을 문자열 S[1][l1:r1]으로 바꾸는데 필요한 최소 편집 스크립트 구하기
def get_script(l0, r0, l1, r1):
    # S[0]의 탐색 구간이 없는 경우, 필요한 만큼 글자 추가
    if l0 == r0:
        for i in range(l1, r1):
            print("a", S[1][i])
        return

    # S[0]의 탐색 구간이 한 글자인 경우
    elif l0 + 1 == r0:
        # S[1]의 탐색 구간이 없는 경우, 삭제
        if l1 == r1:
            print("d", S[0][l0])
            return

        # S[0]의 한 글자가 S[1]에 있는 경우 위치 찾기
        idx = -1
        for i in range(l1, r1):
            if S[0][l0] == S[1][i]:
                idx = i
                break

        # 편집 스크립트 작성
        for i in range(l1, r1):
            # 수정
            if idx == -1 and i == l1:
                print("m", S[1][i])
            # 복사
            elif i == idx:
                print("c", S[1][i])
            # 추가
            else:
                print("a", S[1][i])
        return

    # S[0]의 탐색 구간 줄이기
    m0 = (l0 + r0) // 2

    # 두 문자열의 최소 편집 거리 구하기
    get_dist(0, l0, m0, l1, r1)

    # 거꾸로 뒤집은 두 문자열의 최소 편집 거리 구하기
    get_dist(2, N - r0 + 1, N - m0 + 1, M - r1 + 1, M - l1 + 1)

    # S[1]의 탐색 구간 줄이기
    m1 = l1 - 1
    for i in range(l1, r1):
        if dp[0][m1] + dp[2][M - m1 - 1] > dp[0][i] + dp[2][M - i - 1]:
            m1 = i
    m1 += 1

    # 히르쉬버그 분할 정복
    get_script(l0, m0, l1, m1)
    get_script(m0, r0, m1, r1)

##########################################################################################################

# 두 문자열과 두 문자열을 거꾸로 나타낸 문자열
S = [' ', ' ', ' ', ' ']
S[0] += input().rstrip()
S[1] += input().rstrip()
S[2] += S[0][1:][::-1]
S[3] += S[1][1:][::-1]

# 두 문자열의 크기
N, M = len(S[0]), len(S[1])

# S[0]를 S[1]으로 바꾸는데 필요한 최소 편집 거리
dp = [[0] * (max(N, M) + 1) for _ in range(4)]

# S[0]를 S[1]으로 바꾸는데 필요한 최소 편집 스크립트 구하기
get_script(1, N, 1, M)