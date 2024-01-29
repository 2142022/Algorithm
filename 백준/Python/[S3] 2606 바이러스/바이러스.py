from collections import deque
import sys
input = sys.stdin.readline

# 컴퓨터 수
N = int(input())

# 연결 수
M = int(input())

# 각 컴퓨터에서 연결된 컴퓨터 번호
connect = [list() for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)

# 1번 컴퓨터를 통해 바이러스에 걸리는 컴퓨터 수
cnt = 0

# 방문 체크
visited = 1 << 1

# 1번 컴퓨터를 통해 바이러스에 걸리는 컴퓨터를 담은 큐
q = deque([1])
while q:
    # 현재 컴퓨터
    c = q.popleft()

    # 현재 컴퓨터에 연결된 컴퓨터 확인
    for nc in connect[c]:
        # 아직 탐색하지 않은 컴퓨터인 경우 추가
        if not visited & 1 << nc:
            cnt += 1
            visited |= 1 << nc
            q.append(nc)

print(cnt)