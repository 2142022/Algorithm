import sys
input = sys.stdin.readline

# 추의 개수
N = int(input())

# 모든 추의 무게
W = list(map(int, input().split()))

# 추를 이용해서 확인할 수 있는 무게
possible = set()

# 추의 무게
for w in W:
    # 기존에 확인할 수 있는 추의 무게에서 현재 추의 무게를 빼거나 더하기
    for p in list(possible):
        possible.add(abs(p - w))
        possible.add(p + w)
    possible.add(w)

# 구슬 수
M = int(input())

# 구슬의 무게가 확인이 가능한지 불가능한지 체크
print(*list(map(lambda x: 'Y' if int(x) in possible else 'N', input().split())))