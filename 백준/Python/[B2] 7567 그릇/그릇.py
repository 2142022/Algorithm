import sys
input = sys.stdin.readline

# 그릇 방향
dishes = input().rstrip()

# 최종 높이
h = 10

# 그릇의 방향이 이전과 같다면 +5, 다르다면 +10
for i in range(1, len(dishes)):
    if dishes[i] == dishes[i - 1]:
        h += 5
    else:
        h += 10

print(h)
