import sys
input = sys.stdin.readline

# 로프의 수
N = int(input())

# N개의 로프가 버틸 수 있는 각각의 최대 중량
w = [0] * N
for i in range(N):
    w[i] = int(input())

# 오름차순 정렬
w.sort()

# 로프를 이용하여 들어올릴 수 있는 물체의 최대 중량
result = 0

# 사용할 로프의 개수
cnt = N

# 로프를 하나씩 빼가면서 최댓값 찾기
for i in range(N):
    result = max(result, cnt * w[i])
    cnt -= 1

print(result)