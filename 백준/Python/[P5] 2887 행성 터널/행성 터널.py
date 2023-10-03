import sys
input = sys.stdin.readline

# 부모 노드 찾기
def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
    return parent[a]

####################################################################

# 연결하기
def connect(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

####################################################################

# 행성 개수
N = int(input())

# 행성 좌표
x = []
y = []
z = []
for i in range(N):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))
# 오름차순 정렬 (각 좌표에서 제일 적은 비용만 확인하기 위함)
# 오름차순 정렬을 하지 않는다면 N(N-1)/2개의 좌표 차이를 구해야 함
x.sort()
y.sort()
z.sort()

# 터널 정보
# x좌표, y좌표, z좌표를 따로 저장하지 않는다면 이중 for문을 통해 N(N-1)/2개의 터널 정보를 저장 -> 메모리 초과
# x좌표, y좌표, z좌표를 따로 저장하면 3(N-1)개의 터널 정보 저장
tunnel = []
for i in range(N - 1):
    tunnel.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    tunnel.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    tunnel.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))
# 오름차순 정렬
tunnel.sort()
    
# 터널 연결에 필요한 최소 비용
result = 0

# 부모 리스트
parent = [i for i in range(N)]

# 연결한 터널 개수
cnt = 0

# 터널 탐색
for c, a, b in tunnel:
    # 아직 연결되어 있지 않은 경우 연결
    if find_parent(a) != find_parent(b):
        connect(a, b)
        result += c
        cnt += 1

        # 모든 행성을 연결했다면 끝내기
        if cnt == N - 1:
            break

print(result)