import sys
input = sys.stdin.readline

# 듣도 못한 사람 수, 보도 못한 사람 수
N, M = map(int, input().split())

# 듣도 못한 사람
A = set([input().rstrip() for _ in range(N)])

# 듣보잡
result = []
for _ in range(M):
    name = input().rstrip()
    if name in A:
        result.append(name)

# 정렬 후 출력
print(len(result))
print(*sorted(result), sep='\n')