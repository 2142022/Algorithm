from collections import deque
import sys
input = sys.stdin.readline

# 학생 x보다 작거나 큰 학생 수 구하기
# connect: 작거나 큰 학생의 연결 정보
def get_cnt(x, connect):
    # 학생 x보다 작거나 큰 학생 수
    cnt = 0

    # 방문 체크
    visited = [0] * (N + 1)
    visited[x] = 1

    # 탐색 학생을 담은 큐
    q = deque([x])
    while q:
        i = q.popleft()

        # 연결된 학생 탐색
        for ni in connect[i]:
            if not visited[ni]:
                cnt += 1
                visited[ni] = 1
                q.append(ni)

    return cnt

#####################################################################################

# 학생 수, 비교 횟수
N, M = map(int, input().split())

# 각 학생을 기준으로 더 작은 학생
smaller = [list() for _ in range(N + 1)]
# 각 학생을 기준으로 더 큰 학생
taller = [list() for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    smaller[b].append(a)
    taller[a].append(b)

# 자신의 키가 몇 번째인지 알 수 있는 학생 수
cnt = 0

# 기준 학생
for i in range(1, N + 1):
    # 본인보다 작은 학생 수와 큰 학생 수의 합이 N - 1이라면 자신의 키가 몇 번째인지 알 수 있음
    if get_cnt(i, smaller) + get_cnt(i, taller) == N - 1:
        cnt += 1

print(cnt)