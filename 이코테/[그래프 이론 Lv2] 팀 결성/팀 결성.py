import sys
input = sys.stdin.readline

# x번 학생이 속한 팀 대표 번호 찾기
def find_parent(x):
    # x번 학생이 대표가 아니라면 재귀로 찾기
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

###############################################

# N: 학생 번호, M: 수행할 연산의 수
N, M = map(int, input().split())

# 각 학생이 속한 팀의 대표 번호
# 처음에는 자기 자신으로 초기화
parent = [i for i in range(N + 1)]

# M개의 연산 수행
for _ in range(M):
    # op: 연산 종류
    # a, b: 학생 번호
    op, a, b = map(int, input().split())

    # 각 팀의 대표찾기
    pa = find_parent(a)
    pb = find_parent(b)

    # 팀 합치기
    if op == 0:
        # 두 팀의 대표가 다르다면 합치기
        if pa != pb:
            parent[pb] = pa

    # 같은 팀 여부 확인
    elif op == 1:
        if pa == pb:
            print("YES")
        else:
            print("NO")