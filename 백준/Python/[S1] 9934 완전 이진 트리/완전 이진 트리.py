import sys
input = sys.stdin.readline

# 트리 깊이
K = int(input())

# 빌딩 방문 순서
order = list(map(int, input().split()))

# 빌딩 방문했으면 1, 아니면 0
flag = [0] * (len(order))

# 중간 빌딩을 저장하고 중간 빌딩을 기준으로 나눠서 반복
result = []
for i in range(1,K):
    j = 1
    while j * (len(order) // (2**i) + 1) - 1 < len(order):
        if flag[j * (len(order) // (2**i) + 1) - 1] == 0:
            flag[j * (len(order) // (2**i) + 1) - 1] = 1
            result.append(order[j * (len(order) // (2**i) + 1) - 1])
        j += 1

# 단말 노드
for i in range(len(order)):
    if flag[i] == 0:
        result.append(order[i])

# 출력
for i in range(K):
    for j in range(2**i):
        if len(result) != 0:
            print(result.pop(0), end = ' ')
    print()
        

