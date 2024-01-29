import sys
input = sys.stdin.readline

# 사람 수, 제거할 사람 번호
N, K = map(int, input().split())

# 사람
people = [i for i in range(1, N + 1)]

# 제거한 사람 순서
remove = []

# 한 명씩 제거
last = 0
for i in range(N):
    last = (last + K - 1) % (N - i)
    remove.append(str(people.pop(last)))

print('<' + ', '.join(remove) + '>')