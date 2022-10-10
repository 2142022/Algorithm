import sys
input = sys.stdin.readline

# 상점에서 사는 물병을 최소로 하는 방법:
# N = 2^a + 2^b + ... + 2^K - x
# 즉, x를 최소로 해야 함
# N을 2의 제곱승의 합으로 나타내기 위해서는 이진법으로 바꾸면 됨
# ex) 13 = 1101 (2) -> 1의 개수가 K
# 1의 개수가 K보다 크면 1씩 더해주기

N, K = map(int, input().split())

# 물병의 수
cnt = 0

# N을 이진법으로 바꿨을 때, 1의 개수가 K보다 크다면 물병 한개 구입
while bin(N).count('1') > K:
    cnt += 1
    N += 1

print(cnt)
