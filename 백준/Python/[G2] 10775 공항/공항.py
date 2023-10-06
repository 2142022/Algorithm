import sys
input = sys.stdin.readline

# n번 이하의 게이트 중 도킹 가능한 게이트 번호
def find_gate(n):
    if visited[n] != n:
        visited[n] = find_gate(visited[n])
    return visited[n]

#########################################################################################

# 도킹된 게이트는 더 작은 게이트로 바꾸기
def change_gate(a, b):
    a = find_gate(a)
    b = find_gate(b)
    visited[b] = a

#########################################################################################

# 게이트 수
G = int(input())

# 비행기 수
P = int(input())

# 도킹가능한 최대 비행기 수
cnt = 0

# 각 게이트가 도킹 되었는지 체크
# visited[i] = i라면, i번째 게이트는 아직 도킹되지 않음
# ex) 4번 게이트에 비행기가 도킹하면, 다음 비행기가 3번 게이트에 도킹하도록 하기 위해서
#     visited[4] = 3으로 바꾸기
#     => 다음 비행기가 4번 게이트로 들어오면 3번 게이트에 도킹하게 되고 visited[3] = 2가 됨
#     하지만 visited[3] = 0라면 이미 다른 비행기가 도킹했으므로 도킹 불가능
visited = [i for i in range(G + 1)]

# 비행기 도킹하기
for _ in range(P):
    # 현재 비행기가 도킹 가능한 게이트의 최대 번호
    n = int(input())

    # n번 이하의 게이트 중 도킹 가능한 게이트 번호
    gate = find_gate(n)

    # 도킹 가능한 게이트가 없는 경우
    if gate == 0:
        break

    # 도킹하기
    cnt += 1
    change_gate(gate - 1, gate)

print(cnt)
