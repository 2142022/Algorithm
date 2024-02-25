from collections import deque
import sys
input = sys.stdin.readline

# 원을 트리 구조로 나타내기
# i: 현재 원
# prev: 현재 원의 바깥쪽 원
def tree(i, prev):
    # 현재 추가하려는 원이 i원의 내부 원들 중 그 내부에 있는 경우
    for j in connect[i]:
        # 바깥원 패스
        if j == prev:
            continue

        # 내부에 있는 경우
        x1, r1 = circles[j]
        if abs(x - x1) <= abs(r - r1):
            tree(j, i)
            break

    # 현재 원의 내부에 추가하기
    else:
        connect[i].append(k)
        connect[k].append(i)

#########################################################################################################################

# 원i에서 원B까지 이동하기
def go(i):
    # 도착 원인 경우 끝내기
    if i == B:
        return 1

    # 현재 원에서 갈 수 있는 원 탐색
    for j in connect[i]:
        # 방문 체크
        if visited[j]:
            continue

        # 다음 원 탐색
        visited[j] = 1
        route.append(j)
        if go(j):
            return 1

        # 초기화
        visited[j] = 0
        route.pop()

    return 0

#########################################################################################################################

# 원 개수
N = int(input())

# 원 번호, 원 x좌표, 반지름 (반지름 기준 내림차순 정렬)
info = [(0, 0, 1100000)]
# 원 번호별 좌표, 반지름
circles = [list() for _ in range(N + 1)]
circles[0] = [0, 1100000]
for _ in range(N):
    k, x, r = map(int, input().split())
    info.append((k, x, r))
    circles[k] = [x, r]
info.sort(key = lambda x: -x[2])

# 원을 트리 구조로 나타냈을 때, 연결 정보 (좌표 평면: 0)
connect = [list() for _ in range(N + 1)]

# 원 하나씩 트리에 붙이기
for i in range(1, N + 1):
    k, x, r = info[i]
    tree(0, -1)

# 출발 원, 도착 원
A, B = map(int, input().split())

# 방문 체크
visited = [0] * (N + 1)
visited[A] = 1

# 도착 원까지 방문한 원
route = [A]
go(A)

print(len(route))
print(*route)
