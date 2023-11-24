import sys, heapq
input = sys.stdin.readline

# 연결된 컴퓨터 중 가장 작은 번호 찾기
def find_represent(x):
    if represent[x] != x:
        represent[x] = find_represent(represent[x])
    return represent[x]

#############################################################

# 컴퓨터 수
N = int(input())

# 기부할 랜선의 길이
total = 0

# 연결 정보를 담은 최소 힙
h = []
for i in range(N):
    info = input().rstrip()
    for j in range(N):
        # 현재 랜선
        alpha = info[j]
        if 'a' <= alpha <= 'z':
            # 현재 랜선의 길이
            l = ord(alpha) - ord('a') + 1
            total += l
            if i != j:
                heapq.heappush(h, (l, i, j))
        elif 'A' <= alpha <= 'Z':
            # 현재 랜선의 길이
            l = ord(alpha) - ord('A') + 27
            total += l
            if i != j:
                heapq.heappush(h, (l, i, j))

# 연결된 컴퓨터 중 가장 작은 번호
represent = [i for i in range(N)]

# 연결한 랜선 개수
cnt = 0

# 가장 작은 길이의 랜선 하나씩 선택
while h and cnt < N:
    # 랜선 길이, 두 컴퓨터 번호
    l, i, j = heapq.heappop(h)

    # 두 컴퓨터와 연결된 컴퓨터 중 가장 작은 번호
    ri = find_represent(i)
    rj = find_represent(j)

    # 두 컴퓨터가 이미 연결되어 있는 경우 패스
    if ri == rj:
        continue

    # 두 컴퓨터 연결하기
    cnt += 1
    total -= l
    if ri < rj:
        represent[rj] = ri
    else:
        represent[ri] = rj

# 모든 컴퓨터가 연결된 경우
if cnt == N - 1:
    print(total)
else:
    print(-1)