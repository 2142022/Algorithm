import sys
input = sys.stdin.readline

# N: 참가자들의 음의 개수, A: 첫 음, D: 공차
N, A, D = map(int, input().split())
# 참가자들의 음을 나타내는 N개의 정수
sound = list(map(int, input().split()))

# 가장 큰 X단 고음
X = 0

# 음을 하나씩 탐색하면서 X단 고음이 되면 다음 음 찾기
for i in sound:
    # 찾는 음이 나온 경우
    if i == A:
        X += 1
        A += D

print(X)