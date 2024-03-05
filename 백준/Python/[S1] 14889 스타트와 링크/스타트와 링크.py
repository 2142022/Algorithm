import sys
input = sys.stdin.readline

# 스타트 팀과 링크 팀의 능력치 차이 구하기
def get_diff():
    # 스타트 팀, 링크 팀
    s, l = [], []
    for i in range(N):
        if T[i]:
            s.append(i)
        else:
            l.append(i)

    # 능력치 차이
    diff = 0
    for i in s:
        for j in s:
            diff += S[i][j]
    for i in l:
        for j in l:
            diff -= S[i][j]

    return abs(diff)

##################################################################

# cnt번째 스타트 팀원 뽑기
# start: 현재 뽑을 수 있는 사람의 시작 번호
def select(cnt, start):
    global min_diff

    # 모두 뽑은 경우
    if cnt == N // 2:
        # 스타트 팀과 링크 팀의 능력치 차이
        min_diff = min(min_diff, get_diff())

        # 차이가 0이라면 무조건 끝내기
        if min_diff == 0:
            return 1
        return 0

    # 현재 팀원 뽑기
    for i in range(start, N // 2 + cnt + 1):
        T[i] = 1
        if select(cnt + 1, i + 1):
            return 1
        T[i] = 0

    return 0

##################################################################

# 사람 수
N = int(input())

# 능력치
S = [list(map(int, input().split())) for _ in range(N)]

# 스타트 팀과 링크 팀의 능력치의 차이의 최솟값
min_diff = 40000

# 스타트 팀 체크
T = [0] * N

# 스타트 팀 한 명씩 뽑기
select(0, 0)

print(min_diff)