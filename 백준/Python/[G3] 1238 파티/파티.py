from collections import deque
import sys
input = sys.stdin.readline

# 각 학생이 파티 마을에서 집까지 돌아오는데 걸리는 시간 구하기
# X: 파티 마을
def comeback(X):
    global N

    # 각 학생이 파티 마을에서 집까지 돌아오는데 걸리는 시간
    time1 = [sys.maxsize] * (N + 1)

    # 현재 마을 번호와 현재까지 걸린 시간을 담은 큐
    q = deque([(X, 0)])
    time1[X] = 0

    # 연결된 도로 탐색
    while q:
        # 현재 마을 번호, 현재까지 걸린 시간
        i, t = q.popleft()

        # 더 적게 걸리는 경로를 찾았다면 패스
        if time1[i] < t:
            continue

        # 연결된 마을 탐색
        for ni, nt in connect[i]:
            # 현재 저장된 시간보다 적게 걸리는 경우, 큐에 추가
            if t + nt < time1[ni]:
                time1[ni] = t + nt
                q.append((ni, t + nt))

    return time1

################################################################

# 학생S가 파티까지 가는데 걸리는 시간 구하기
# X: 파티 마을
def go_party(S, X):
    global N

    # 학생S가 각 마을까지 가는데 걸리는 시간
    time2 = [sys.maxsize] * (N + 1)

    # 현재 마을 번호와 현재까지 걸린 시간을 담은 큐
    q = deque([(S, 0)])
    time2[S] = 0

    # 연결된 도로 탐색
    while q:
        # 현재 마을 번호, 현재까지 걸린 시간
        i, t = q.popleft()

        # 더 적게 걸리는 경로를 찾았다면 패스
        if time2[i] < t:
            continue

        # 연결된 마을 탐색
        for ni, nt in connect[i]:
            # 현재 저장된 시간보다 적게 걸리는 경우, 큐에 추가
            if t + nt < time2[ni]:
                time2[ni] = t + nt
                q.append((ni, t + nt))

    return time2[X]

################################################################

# N: 학생 수, M: 도로 수, X: 파티 마을
N, M, X = map(int, input().split())

# 도로 정보
connect = [list() for _ in range(N + 1)]
for _ in range(M):
    start, end, time = map(int, input().split())
    connect[start].append((end, time))

# 각 학생이 파티 마을에서 집까지 돌아오는데 걸리는 시간
time = comeback(X)

# 최대 왕복 시간
max_time = 0

# 각 학생의 왕복 시간 구하기
for i in range(1, N + 1):
    t = go_party(i, X) + time[i]
    max_time = max(max_time, t)

print(max_time)