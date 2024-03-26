import sys
input = sys.stdin.readline

# 대표 서버 구하기
def find(x):
    if ref[x] >= 0:
        ref[x] = find(ref[x])
        return ref[x]
    else:
        return x

#############################################################################

# 두 서버 a, b 연결하기
def connect(a, b):
    # 두 서버의 대표 서버
    a = find(a)
    b = find(b)

    # 이미 연결되어 있는 경우
    if a == b:
        return 0

    # 더 작은 서버로 연결
    if a < b:
        ref[a] += ref[b]
        ref[b] = a
    else:
        ref[b] += ref[a]
        ref[a] = b
    return 1

#############################################################################

# 최소 통신망 설치 비용 구하기
def get_cost():
    # 연결한 통신망 개수
    cnt = 0

    # 최종 설치 비용
    cost = 0

    # 최소 비용인 통신망 설치
    for c in range(1, 5):
        for a, b in edges[c]:
            # 연결하기
            if connect(a, b):
                cnt += 1
                cost += c

                # 모든 서버를 연결한 경우 끝내기
                if cnt == R * C - 1:
                    return cost

#############################################################################

# 테스트 케이스
for _ in range(int(input())):
    # 통신망 크기
    R, C = map(int, input().split())

    # 연결된 서버들의 개수 / 대표 서버
    # 대표 서버(연결된 서버들 중 가장 작은 번호)인 경우 연결된 서버들의 개수 (-)
    # 대표 서버가 아닌 경우, 대표 서버의 번호
    ref = [-1] * (R * C)

    # 연결 비용과 두 서버 번호 (비용은 1 ~ 4)
    edges = [list() for _ in range(5)]
    for i in range(R):
        for j, cost in enumerate(list(map(int, input().split()))):
            edges[cost].append((C * i + j, C * i + j + 1))
    for i in range(R - 1):
        for j, cost in enumerate(list(map(int, input().split()))):
            edges[cost].append((C * i + j, C * (i + 1) + j))

    # 최소 통신망 설치 비용
    print(get_cost())



